import segno
from datetimeaddons import get_datetime
from segno import helpers


def qrcode_geo(txt):
    latitude, longitude = float(txt.split(' ')[0]), float(txt.split(' ')[1])
    config = helpers.make_geo_data(latitude, longitude)
    file_name = 'geo_' + get_datetime() + '.png'
    qr = segno.make(config, error='H')
    qr.save(file_name, scale=3)
    return file_name