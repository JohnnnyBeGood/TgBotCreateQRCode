import os
import sys
from config import TOKEN
import telebot
from message import msg_error, msg_welcome
import middleware


API_TOKEN = TOKEN
bot = telebot.TeleBot(API_TOKEN)

# словарь для хранения данных о точке доступа
wifi_dict = {"ssid": None, "password": None, "security": None}
# словарь для хранения данных о контакте
vCard_dict = {
    "name":         None,
    "displayname":  None,
    "email":        None,
    "url":          None,
    "phone":        None,
}

# /SimpleText - кодирование произвольного текста
# /geo -  кодирование географических координат
# /vCard - кондирование визитной карточки
# /WiFi - кодирование точки доступа WI-Fi
# /site - кодирование интернет адреса

# обработка команд: start и help
@bot.message_handler(commands=["help", "start"])
def send_welcome(message):
    bot.send_message(message.chat.id, msg_welcome)


# блок обработки команды SimpleText
@bot.message_handler(commands=["SimpleText"])
def get_SimpleText_message(message):
    msg = bot.send_message(
        message.chat.id, "Пожалуйста напишите текст, который нужно закодировать:"
    )
    bot.register_next_step_handler(msg, process_smpltext_step)


def process_smpltext_step(message):
    if len(message.text) > 200:
        bot.send_message(
            message.chat.id,
            "К сожалению вы привысили размер сообщения. Повторите команду заново",
        )
    else:
        file_name = middleware.simple_text(message.text)
        img = open(file_name, "rb")
        bot.send_photo(message.chat.id, img, caption="Простой текст")
        os.remove(file_name)
# конец блока SimpleText

# блок обработки команды geo
@bot.message_handler(commands=["geo"])
def get_geo_message(message):
    msg = bot.send_message(
        message.chat.id,
        "Пожалуйста пришлите координаты в формате: широта, долгота (через пробел)",
    )
    bot.register_next_step_handler(msg, process_geo_step)


def process_geo_step(message):
    file_name = middleware.geo(message.text)
    img = open(file_name, "rb")
    bot.send_photo(message.chat.id, img, caption="Географические координаты")
    os.remove(file_name)
# конец блока

# блок обработки команды vCard
@bot.message_handler(commands=["vCard"])
def get_vCard_message(message):
    msg = bot.send_message(
        message.chat.id,
        """Пожалуйста напишите данные о контактном лице, который нужно закодировать:
        (следуйте подсказкам бота)
        введите ФИО:""",
    )
    bot.register_next_step_handler(msg, process_vCard_step_1)


def process_vCard_step_1(message):
    vCard_dict["name"] = message.text
    msg = bot.send_message(message.chat.id, "отображаемые ФИО:")
    bot.register_next_step_handler(msg, process_vCard_step_2)


def process_vCard_step_2(message):
    vCard_dict["displayname"] = message.text
    msg = bot.send_message(message.chat.id, "адрес электронной почты:")
    bot.register_next_step_handler(msg, process_vCard_step_3)


def process_vCard_step_3(message):
    vCard_dict["email"] = message.text
    msg = bot.send_message(message.chat.id, "адрес Web-страницы:")
    bot.register_next_step_handler(msg, process_vCard_step_4)


def process_vCard_step_4(message):
    vCard_dict["url"] = message.text
    msg = bot.send_message(message.chat.id, "номер телефона:")
    bot.register_next_step_handler(msg, process_vCard_step_5)


def process_vCard_step_5(message):
    vCard_dict["phone"] = message.text
    file_name = middleware.v_card(vCard_dict)
    img = open(file_name, "rb")
    bot.send_photo(message.chat.id, img, caption="Контакт")
    os.remove(file_name)
# конец блока vCard


# блок обработки команды WiFi
@bot.message_handler(commands=["WiFi"])
def get_WiFi_message(message):
    msg = bot.send_message(
        message.chat.id,
        """Пожалуйста задайте параметры точки доступа, которые нужно закодировать:
        введите название ssid:""",
    )
    bot.register_next_step_handler(msg, process_wifi_step_1)


def process_wifi_step_1(message):
    wifi_dict["ssid"] = message.text
    msg = bot.send_message(message.chat.id, "введите пароль:")
    bot.register_next_step_handler(msg, process_wifi_step_2)


def process_wifi_step_2(message):
    wifi_dict["password"] = message.text
    msg = bot.send_message(message.chat.id, "введите тип шифрования:")
    bot.register_next_step_handler(msg, process_wifi_step_3)


def process_wifi_step_3(message):
    wifi_dict["security"] = message.text
    file_name = middleware.wifi(wifi_dict)
    img = open(file_name, "rb")
    bot.send_photo(message.chat.id, img, caption="Точка доступа Wi-Fi")
    os.remove(file_name)
# конец блока WiFi

# блок обработки команды site
@bot.message_handler(commands=["site"])
def get_site_message(message):
    msg = bot.send_message(
        message.chat.id, "Пожалуйста напишите web-адрес, который нужно закодировать:"
    )
    bot.register_next_step_handler(msg, process_website_step)


def process_website_step(message):
    file_name = middleware.site(message.text)
    img = open(file_name, "rb")
    bot.send_photo(message.chat.id, img, caption="ссылка на сайт")
    os.remove(file_name)
# конец блока site

# блок обработки случайного текста и выдача ошибки
@bot.message_handler(content_types=["text"])
def get_text_message(message):
    bot.send_message(message.from_user.id, msg_error)


if __name__ == "__main__":

    # Enable saving next step handlers to file "./.handlers-saves/step.save".
    # Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
    # saving will hapen after delay 2 seconds.
    bot.enable_save_next_step_handlers(delay=2)

    # Load next_step_handlers from save file (default "./.handlers-saves/step.save")
    # WARNING It will work only if enable_save_next_step_handlers was called!
    bot.load_next_step_handlers()
    bot.polling(non_stop=True)
