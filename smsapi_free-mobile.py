# -*- coding: utf-8 -*-

import requests


def sendMessage(msg, user="user", password="password"):
    """Send SMS notification with free-mobile"""

    url = "https://smsapi.free-mobile.fr/sendmsg?user=" + \
          user + "&pass=" + password + "&msg=" + msg
    requests.get(url)
