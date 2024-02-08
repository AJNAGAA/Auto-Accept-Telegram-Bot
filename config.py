import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") # ⚠️ Required
   
    # database config
    DB_URL  = os.environ.get("DB_URL","")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","AutoAcceptBot")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://telegra.ph/file/0ceb5f176f3cf877a08b5.jpg")
    ADMIN       = int(os.environ.get('ADMIN', '')) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "")) # ⚠️ Required
    WELCOME_MSG = os.environ.get("WELCOME_MSG", "Hey {user},\nYour Request Approved ✅,\n\nWelcome to **{title}**")
    LEAVE_MSG = os.environ.get("LEAVE_MSG", "By {user},\nSee You Again 👋\n\nFrom **{title}**")
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


class TxT(object):

    HELP_MSG = """
<b> ADMIN Available commands:- </b>

➜ /set_welcome - To set custom welcome message (support photo & video & animation or gif)
➜ /set_leave - To set custom leave message (support photo & video & animation or gif)
➜ /option - To toggle your welcome & leave message (whether it'll show to user or not)
➜ /status - To see status about bot
➜ /restart - To restart the bot
➜ /broadcast - To brodcast the users (only those user who has started your bot)


⚠️ <b> Support HTML & Markdown formating in welcome or leave message for more info <a href=https://core.telegram.org/api/entities#:~:text=%2C%20MadelineProto.-,Allowed%20entities,-For%20example%20the> Link </a>. </b>


<b>⦿ Developer:</b> <a href=https://t.me/Snowball_Official>ѕησωвαℓℓ ❄️</a>
"""
