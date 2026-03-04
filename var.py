# Modules
from dotenv import load_dotenv
import json
import logging
import os
import sys
import time
import traceback
from PIL import ImageFont

##### VARIABLES #####

load_dotenv()

start_time = time.time()

##### BITCOIN SWITCH #####

ws_switch = os.getenv("BITCOIN_SWITCH_WS")
lnurl = os.getenv("LNURL")

##### MERCHANT #####

price = os.getenv("PRICE")
currency = os.getenv("CURRENCY")

suggested_wallets = json.loads(os.environ['SUGGESTED_WALLETS'])

##### SYSTEM #####

debuglevel = os.getenv("DEBUG_LEVEL", "INFO")

file_handler = logging.FileHandler('zapshutter.log')
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]

logging.basicConfig(handlers=handlers, format='%(asctime)s %(levelname)s - %(message)s', level=debuglevel)
logging.info(f"Setting debug level at {debuglevel}")

production = os.getenv("PRODUCTION", "True").lower() in ('true', '1', 't')

##### TRIGGER #####

#tray0 = json.loads(os.environ['TRAY0'])

relay_duration = float(os.getenv("RELAY_DURATION", 500)) / 1000

##### DISPLAY #####

show_display = os.getenv("SHOWDISPLAY", "True").lower() in ('true', '1', 't')

display_expiry = int(os.getenv("DISPLAY_DELAY", 1))
suceess_screen_expiry = int(os.getenv("SUCCESS_SCREEN_EXPIRY", 5))

picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

font_a = os.getenv("FONTA", "Font.ttc")
font_b = os.getenv("FONTB", "Rushfordclean.otf")
fontsize_a = int(os.getenv("FONTSIZEA", 24))
fontsize_b = int(os.getenv("FONTSIZEB", 32))

#font36 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 36)
fontA = ImageFont.truetype(os.path.join(picdir, font_a), fontsize_a)
fontB = ImageFont.truetype(os.path.join(picdir, font_b), fontsize_b)