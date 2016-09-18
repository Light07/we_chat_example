# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import settings

import requests

class RobotHelper(object):
    headers = {'apikey': settings.baidu_apikey}

    def get_robot(self, info):
        url = 'http://apis.baidu.com/turing/turing/turing?key=50e00487dfb7481ca2df2686017d2fd8&info=%s&userid=eb2edb736'%(info)
        r = requests.get(url, headers=self.headers)
        try:
            j = r.json()
            if int(r.status_code) == 200:
                return j['text']
            else:
                return info
        except Exception as e:
            print e
            return info

if __name__ == "__main__":
    w = RobotHelper()
    print w.get_robot('上海 天气')