# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

baidu_apikey = "your baidu key"

#wechat key
encodingAESKey = 'your encoding key'
token = 'we_chat'
app_id = "your wechat app id"
app_secret = "your wechat secret"

welcome_message = """欢迎关注iTesting.由于作者正在研究微信开发，公众号菜单暂时隐藏，但每周推送不受影响。\n
你可以通过查看历史文章进行学习，我会尽快恢复菜单选项。\n
试试我的研究成果 “智能机器人”吧， 玩法如下：\n
查天气：公众号里直接回复 “城市名称+天气” 来查看当天的天气，例如输入 上海天气  ，你将会得到上海今日天气。\n
逗机器人： 公众号里直接回复文本消息，中英文都可以，机器人会尝试理解并回答你，智能爆表哦。\n
待改进: 公众号里直接回复语音，图片，机器人会原样返回给你。"""

TIME_OUT = 7200
SLEEP_TIME = 2
REFRESH_INTERVAL = 10