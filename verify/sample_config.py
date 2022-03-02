import os

class Config(object):
    TOKEN = '' # 봇 토큰
    OWNERS = [123456789] # 관리자의 아이디
    DebugServer = [] # 채널 id
    BOT_NAME = "" # 봇 이름
    BOT_TAG = "#" # 태그
    BOT_ID = 123456789      # 봇 아이디
    AboutBot = "" # 봇 정보
    CommandInt = '!'
    color_code = 0x2f3136 # 색상코드

class Production(Config):
    LOGGER = False
class Development(Config):
    LOGGER = True