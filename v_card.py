import segno
from segno import helpers
from datetimeaddons import get_datetime


def qrcode_vcard(dict):
    #vcard = helpers.make_vcard_data(name='Doe;John', displayname='John Doe', email=['me@example.org', 'another@example.org'], url=['http://www.example.org', 'https://example.org/~joe'], phone=['+1234567', '+09348509348509', '+8327423'])
    vcard = helpers.make_vcard_data(name=dict['name'], displayname=dict['displayname'], email=dict['email'], url=dict['url'], phone=dict['phone'])
    qr=segno.make(vcard, error='h')
    file_name = 'vCard_' + get_datetime() + '.png'
    qr.save(file_name, scale=3)
    return file_name