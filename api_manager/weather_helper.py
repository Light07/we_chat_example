# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import requests

import settings

class GetWeather(object):
    headers = {'apikey': settings.baidu_apikey}

    def get_city_code(self, city):
        url = 'http://apis.baidu.com/apistore/weatherservice/citylist?cityname=%s'%city

        r = requests.get(url, headers=self.headers)
        j =  r.json()['retData']
        for i in j:
            if i['name_cn'] == city:
                return i['area_id']

    def get_weather(self, city):
        city_code = self.get_city_code(city)
        url = 'http://apis.baidu.com/apistore/weatherservice/recentweathers?cityname={}&cityid={}'.format(city, city_code)
        r = requests.get(url, headers=self.headers)
        raw_data = r.json()

        if raw_data.has_key("retData"):

            if type(raw_data['retData']) == dict:
                j = raw_data['retData']['today']
                content = "今日{city}的天气情况如下：\n" \
                          "日期：{date},"  \
                          "{week}, "  \
                          "当前温度：{curTemp}, "  \
                          "{type}, {fengxiang}, {fengli}"  \
                          "最高气温：{hightemp}, " \
                          "最低气温：{lowtemp}, " \
                          "PM值：{aqi}" .format(city=city, date=j['date'], week=j['week'], curTemp=j['curTemp'],type=j['type'],\
                                             fengxiang=j['fengxiang'], fengli=j['fengli'], hightemp=j['hightemp'],\
                                              lowtemp=j['lowtemp'], aqi=j['aqi'])
                return content
            else:
                return "您输入的城市有误，请重新输入."
        else:
            return "您输入的城市有误，请重新输入."

if __name__ == "__main__":
    w = GetWeather()
    print w.get_weather('上海')