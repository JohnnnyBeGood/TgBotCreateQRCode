from datetimeaddons import get_datetime
import segno


def qrcode_text(txt):
    # today = date.today()
    # d = today.strftime("%b-%d-%Y")
    # time_now = datetime.now()
    # t = time_now.strftime("%H_%M_%S")
    qr = segno.make(txt)
    file_name = 'txt_' + get_datetime() + '.png'
    qr.save(file_name, scale=3)
    return file_name