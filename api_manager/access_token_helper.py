# -*- coding: UTF-8 -*-

import time
import threading
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import requests

import settings

class AccessTokenHelper(threading.Thread):

    url= "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" %(settings.app_id, settings.app_secret)

    def __init__(self):
        threading.Thread.__init__(self)
        self._time_left = 0
        self._access_token = ''

    def _get_access_token_for_real(self):
        r = requests.get(self.url)
        self._time_left = r.json()['expires_in']
        self._access_token = r.json()['access_token']

    def get_access_token(self):
        if self._time_left < settings.REFRESH_INTERVAL:
            self._get_access_token_for_real()
        return self._access_token

    def run(self):
        while(True):
            print self._time_left
            if self._time_left > settings.REFRESH_INTERVAL:
                time.sleep(settings.SLEEP_TIME)
                self._time_left -= settings.SLEEP_TIME

            else:
                self._get_access_token_for_real()

if __name__ == "__main__":
    access_token = AccessTokenHelper()
    print access_token.start()
    print access_token.get_access_token()