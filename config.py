import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = 29415533
API_HASH = "7c606daedce1208e89a9936fa72e429e"
BOT_TOKEN = "6898857342:AAGTeX0HsT7k_gOFo7MoxMm_CUb3-7l5VHY"
MONGO_DB_URI = "mongodb+srv://Leo88815:Leo88815@leo1.tefmyr4.mongodb.net/?retryWrites=true&w=majority&appName=Leo1"
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))
LOG_GROUP_ID = -4234821729
OWNER_ID = 6795757702

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Learningbots79/Learning_Bots",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/leoworl")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/+759_Us418SE5ZWRl")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQHA2G0AjKrmuD_0XeorUFj-FRX6EO69Puk6nzNXufp8jtQ4xt5b9173BH9bnk2Fju30RpH8KOCA7nvJE8G10U36lgkBRGatTICoIPnyUDsIDHPCaytttTAAbZFMfc0AsJSlF2EoTxcJgCRan1IS9jjVOcuQh4iw9ArYMYLY-cTK6K_AZ_fzt3_B3umjUoGxLZrMuT2nlvVnI7urx1QMUYvVoSQHh4BoUf5aHunX-8OJUeYaAUt3bks_-B9TY2YLqlubpjG0JU5OeCOcthiNsG_-KDVlJh6ip6Tpz4qXZG-ZtzNnXCoMmES0fE6UHlkXGuIE-GUNlc6X3dnNrkr2cquRrnQoGwAAAAGVDwiGAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/618736bca90c18ee4118f.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/618736bca90c18ee4118f.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/618736bca90c18ee4118f.jpg"
STATS_IMG_URL = "https://graph.org/file/618736bca90c18ee4118f.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/618736bca90c18ee4118f.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/618736bca90c18ee4118f.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
