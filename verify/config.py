import os

class Config(object):
    TOKEN = 'OTMyNTg1NDE3NjYyOTM1MDUw.YeVH2g.GIwZ52j_jnrodHLvFt6i-AH3dwU' # 봇 토큰
    OWNERS = [896570484588703744] # 관리자의 아이디
    DebugServer = [901745892418256906] # 채널 id
    BOT_NAME = "배틀이" # 봇 이름
    BOT_TAG = "#0001" # 태그
    BOT_ID = 932585417662935050      # 봇 아이디
    AboutBot = "" # 봇 정보
    CommandInt = '!'

    color_code = 0x2f3136 # 색상코드

class Production(Config):
    LOGGER = False

class Development(Config):
    LOGGER = True