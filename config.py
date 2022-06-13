## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BAB8PuErIfstLm4uQEzFsW1nOk6fGWg4KmTYPqT3ETPklWd7wHZvFmd4p-I_sjA3NfwKVJ4TN6Voon_lG5oCvZrzTMMqPvUg-vkjvRS_RrW2f2Nr1SYWqxo8Fnx3g7ZT_ywJj9kS_mSxY6_WUpTkpmxuIPaWD7j1fXHo5z2w5EUmXX_22Qwym9axCHgyG710oF7WUmYkMpHRPlthA6p42bSp_EnwNb7NvNsWhghWyP0xYDT5egK7ckw1z0dAtOxz6vlq6jzZsUS7Lvef2L5nHPjFL74FN8M5BkDKZ2KIM3nWijdBqRx_kGBHaOtXAIGX48CxTxVfAo7wVsDub5Y_nL4lAAAAAUS05_kA")
BOT_TOKEN = getenv("BOT_TOKEN", "5489171712:AAHLUtNKo6UewcKaf-_BYbVWjtkArrpREJ0")
BOT_NAME = getenv("BOT_NAME", "Y_3_2_BOT")
API_ID = int(getenv("API_ID", "6507985"))
API_HASH = getenv("API_HASH", "3417f2a7bb73203236d16dda82d11614")
OWNER_NAME = getenv("OWNER_NAME", "⦁𝗔ٰٖ𝗟ٰٖ𝗦ٰٖ𝗛ٰٖ𝗔ٰٖ𝗬ٰٖ𝗘ٰٖ𝗕ٰٖ ➪🇳🇱")
OWNER_USERNAME = getenv("OWNER_USERNAME", "lIllIIllll")
ALIVE_NAME = getenv("ALIVE_NAME", "⦁𝗔ٰٖ𝗟ٰٖ𝗦ٰٖ𝗛ٰٖ𝗔ٰٖ𝗬ٰٖ𝗘ٰٖ𝗕ٰٖ ➪🇳🇱")
BOT_USERNAME = getenv("BOT_USERNAME", "Playvideo1BoT")
OWNER_ID = getenv("OWNER_ID", "5373530553")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "M_4_44")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "lIllIIllll")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "AHNOC")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/46fa55b49b85c084159ce.png")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/466de30ee0f9383c8e09e.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
