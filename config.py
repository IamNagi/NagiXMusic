import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "29665018"))
API_HASH = getenv("API_HASH", "1d318a0f759217ce9afc8a46460ca660")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7418765377:AAH3RA09xixovc-Gfb5-cxq6OVW9QCmFKOM")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 99999999))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", ""))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", ""))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AnonymousX1025/AnonXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FLEX_bots_News")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/FLEX_SUPPORT_CHAT")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQHEpvoAkAz2CbNucVgC5g_qiB3fOS5FglARGBZ_J4bsC8KQJ4jDuSIV3_OiASYJ1Xxm6OQQcPlXxeAbxRcP_UcQcivep_iCQ8E7zePW6XvpeD2XrA4sJZTD_i_T6-LUQyNZfsNtqazL0HyGEfLdANpEVG7crFw2pkNlBozo2c_4B6wO9rClG6sB8xITS8SDxSGWbmIfg93xfFkYhOvq52pWyGzihzd0cZeX1Oo_6SmfjOH0jdCpsrVPpVrykJjnR3XMAPyzTYbrSBxE_OwNGZZFxBsCVMmeVMEgihADHZbTlGJYeFQWBD8UUjYCe445Uvw8nkp7CiEcguhvTZ-AzLKi28xoYwAAAAF2rw5hAA")
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
    "START_IMG_URL", "https://unitedcamps.in/Images/file_1059.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://unitedcamps.in/Images/file_1059.jpg"
)
PLAYLIST_IMG_URL = "https://unitedcamps.in/Images/file_1059.jpg"
STATS_IMG_URL = "https://unitedcamps.in/Images/file_1059.jpg"
TELEGRAM_AUDIO_URL = "https://unitedcamps.in/Images/file_1059.jpg"
TELEGRAM_VIDEO_URL = "https://unitedcamps.in/Images/file_1059.jpg"
STREAM_IMG_URL = "https://unitedcamps.in/Images/file_1059.jpg"
SOUNCLOUD_IMG_URL = "https://unitedcamps.in/Images/file_1059.jpg"
YOUTUBE_IMG_URL = "https://unitedcamps.in/Images/file_1059.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://unitedcamps.in/Images/file_1059.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://unitedcamps.in/Images/file_1059.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://unitedcamps.in/Images/file_1059.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
