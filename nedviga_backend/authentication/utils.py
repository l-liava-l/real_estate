# coding: utf-8

import re

re_phone = re.compile("^[0-9]+$")

from urllib.request import urlopen


def send_sms(phone, message):
    url = 'https://smsimple.ru/http_send.php?user=yorcc-lark&pass=aLt4U5C6&or_id=59989&phone={0}&message={1}'.\
        format(phone, message)
    urlopen(url)
