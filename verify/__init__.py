import os
import sys
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)

ENV = bool(os.environ.get('ENV', False))

if ENV:
    TOKEN            = os.environ.get('TOKEN', None)
    try:
        OWNERS       = set(int(x) for x in os.environ.get("OWNERS", "").split())
    except ValueError:
        raise Exception("OWNERS 칸이 비어있습니다 !")
    try:
        DebugServer  = set(int(x) for x in os.environ.get("DebugServer", "").split())
    except ValueError:
        raise Exception("DebugChannel 칸이 비어있습니다 !")
    BOT_NAME         = os.environ.get('BOT_NAME', None)
    BOT_TAG          = os.environ.get('BOT_TAG', "#1234")
    try:
        BOT_ID       = int(os.environ.get('BOT_ID', None))
    except ValueError:
        raise Exception("BOT_ID에 올바른 정수가 없습니다.")
    color_code       = int(os.environ.get('color_code', "0xc68e6e"), 0)
    AboutBot         = os.environ.get('AboutBot', None)
    CommandInt       = os.environ.get('CommandInt', None)

else:
    from verify.config import Development as Config

    TOKEN            = Config.TOKEN
    OWNERS           = Config.OWNERS
    DebugServer      = Config.DebugServer
    BOT_NAME         = Config.BOT_NAME
    BOT_TAG          = Config.BOT_TAG
    BOT_ID           = Config.BOT_ID
    color_code       = Config.color_code
    AboutBot         = Config.AboutBot
    CommandInt       = Config.CommandInt

EXTENSIONS = []
for file in os.listdir("verify/cogs"):
    if file.endswith(".py"):
        EXTENSIONS.append(file.replace(".py", ""))

BOT_NAME_TAG_VER = "%s%s" %(BOT_NAME, BOT_TAG)