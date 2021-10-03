import segno
from segno import helpers
from datetimeaddons import get_datetime


def qrcode_wifi(dict):
    ssid = dict['ssid']
    password = dict['password']
    security = dict['security']
    config_qr = helpers.make_wifi_data(ssid=ssid,
                                       password=password,
                                       security=security)
    file_name = 'wifi_' + get_datetime() + '.png'
    qr = segno.make(config_qr, error='h')
    qr.save(file_name, scale=3)
    return file_name