# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import time
from flask import Flask, request, make_response,redirect, url_for, render_template
import hashlib
import xml.etree.ElementTree as ET

import settings
from api_manager.weather_helper import GetWeather
from api_manager.robot_helper import RobotHelper
from xml_messages.xml_helper import XMLHelper

app = Flask(__name__)
app.debug = True

@app.route('/welcome')
def hello_world():
    return "Welcome to Kevin's website!"

@app.route('/',  methods=['GET', 'POST'])
def wechat():
        if request.method == 'GET':
            if len(request.args) > 0:
                temparr = []
                token = settings.token
                signature = request.args["signature"]
                timestamp = request.args["timestamp"]
                nonce = request.args["nonce"]
                echostr = request.args["echostr"]
                temparr.append(token)
                temparr.append(timestamp)
                temparr.append(nonce)
                temparr.sort()
                newstr = "".join(temparr)
                sha1str = hashlib.sha1(newstr)
                temp = sha1str.hexdigest()
                if signature == temp:
                    return make_response(echostr)
                else:
                    return make_response("Access denied")
            else:
                return make_response("Wrong args received")

        else:
            raw_data = request.stream.read()
            xml_raw = ET.fromstring(raw_data)
            msg = {}
            for child in xml_raw:
                msg[child.tag] = child.text

            msgtype = msg['MsgType']
            tou = msg['ToUserName']
            fromu = msg['FromUserName']
            time_str = str(int(time.time()))

            if msgtype == "event":
                event_msg = xml_raw.find('Event').text
                print event_msg
                if event_msg == "subscribe":
                    sub_content = settings.welcome_message
                else:
                    sub_content = "error"
                xml_reader = XMLHelper().read_xml("txt_message.xml")
                response = make_response(xml_reader.format(to_user=fromu, from_user=tou, c_time=time_str, content_value=sub_content))
            elif msgtype == "image":
                media_id = msg['MediaId']
                xml_reader = XMLHelper().read_xml("img_message.xml")
                response = make_response(xml_reader.format(to_user=fromu, from_user=tou, c_time=time_str, media_id=media_id))
            elif msgtype == "voice":
                media_id = msg['MediaId']
                xml_reader = XMLHelper().read_xml("voice_message.xml")
                response = make_response(xml_reader.format(to_user=fromu, from_user=tou, c_time=time_str, media_id=media_id))
            elif msgtype == 'text':
                # co = xml_raw.find('Content').text.strip().split(' ')
                # if co[len(co)-1] == '天气':
                #     weather = GetWeather()
                #     auto_response_content = weather.get_weather(co[:-1][0])
                # else:
                r = RobotHelper()
                auto_response_content = r.get_robot(xml_raw.find('Content').text)
                xml_reader = XMLHelper().read_xml("txt_message.xml")
                response = make_response(xml_reader.format(to_user=fromu, from_user=tou, c_time=time_str, content_value=auto_response_content))

            elif msgtype in ["video","shortvideo"]:
                title = "My video"
                description = "Check out my video"
                media_id = msg['MediaId']
                xml_reader = XMLHelper().read_xml("video_message.xml")
                response = make_response(xml_reader.format(to_user=fromu, from_user=tou, c_time=time_str, media_id=media_id, title=title, description=description))
            else:
                unknown_content = u"""我不知道你在干什么,无法回复你"""
                xml_reader = XMLHelper().read_xml("txt_message.xml")
                response = make_response(xml_reader.format(to_user=fromu, from_user=tou, c_time=time_str, content_value=unknown_content))

            response.content_type = 'application/xml'
            return response

if __name__ == '__main__':
    app.run(debug=True)
