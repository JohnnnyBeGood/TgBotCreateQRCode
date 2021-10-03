import v_card, simple_text, site_ref, wifi_pass, geographic


def smpl_text(txt):
    return simple_text.qrcode_text(txt)


def wifi(dict):
    return wifi_pass.qrcode_wifi(dict)


def vCard(dict):
    return v_card.qrcode_vcard(dict)


def geo(txt):
    return geographic.qrcode_geo(txt)


def site(txt):
    return site_ref.qrcode_site(txt)