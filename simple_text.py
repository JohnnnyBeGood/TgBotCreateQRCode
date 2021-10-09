from datetimeaddons import get_datetime
import segno


def qrcode_text(txt):
    qr = segno.make(txt)
    file_name = 'txt_' + get_datetime() + '.png'
    qr.save(file_name, scale=3)
    return file_name