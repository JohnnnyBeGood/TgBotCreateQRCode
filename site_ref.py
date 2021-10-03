import segno
from segno import helpers
from datetimeaddons import get_datetime


def qrcode_site(txt):
    qr = segno.make(txt)
    file_name = 'site-ref_' + get_datetime() + '.png'
    qr.save(file_name, scale=3)
    return file_name