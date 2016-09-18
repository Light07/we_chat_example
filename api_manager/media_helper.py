# -*- coding: UTF-8 -*-
import sys

from api_manager.access_token_helper import AccessTokenHelper

reload(sys)
sys.setdefaultencoding("utf-8")

import settings

import requests

class MediaHelper(object):

    def __init__(self):
        self.access_token = AccessTokenHelper()
        self.access_token.start()

    def add_meida(self, filePath, media_type):
        openFile = open(filePath, "rb")
        param = {'media': openFile}
        url = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (self.access_token.get_access_token(), media_type)
        print url
        r = requests.post(url, param)
        print r.json()

if __name__ == '__main__':
    myMedia = MediaHelper()

    print myMedia.add_meida("D:/view.jpg","image")
    #
    # filePath = "D:/code/mpGuide/media/test.jpg"   #请安实际填写
    # mediaType = "image"
    # myMedia.uplaod(accessToken, filePath, mediaType)