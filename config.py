import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "24054192"))
API_HASH = getenv("API_HASH", "ed9a8a61a1b4a1ad0915cbe87ba490ed")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7394763318:AAGSLAKh5YSWGBGAVnBY5GeAvu4HxVu5ypU")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://madpanel:madboy11@atlascluster.gprqayn.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster")


DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 960))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002182187594"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "5901320319"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://t.me/GeceExpress",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/GeceExpress")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/GeceExpress")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")

# Time after which you're assistant account will leave chats automatically.

AUTO_LEAVE_ASSISTANT_TIME = int(

    getenv("ASSISTANT_LEAVE_TIME", "3400")

)  # Remember to give value in Seconds

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2041df9cbcd142cba804578a2cf85939")

SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "80ffd296320e49299830e80b11e3bf73")

# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 314572800))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 3221225472))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BAAGtVnawoafEoHr7rzDa7VTTY_U3r0X9Gv4qw5UGorddfWZ8xbu1vgRT0cqhraAx3J-rAAYoxXXEvZp-bAg_OZaFx-O1kg6BlKLovpW7I2P1OxVjWEhLKDmTPx2MKhpKTgrV3m0ksa4uiJt7GAyc656OJR_eHGwXYQKCEauDrqjIB9t67KFcxgmI2CsUTGAR77f7NMIUbG49gwSUZk-jBSc9Co7oZujwuNkHkq2vxMAdZTZZEGszGqvNcYOAwXBjtry6X1opkOy9LlaP3Ofxjc0G8JmU0V4rtklGEIKvIUBZpI3uNQAV10xzoBL8ExopbSD3Kjjs7W_4SlPUqEB0U2hAAAAAV-_AH8A")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/321decfc24b08c837626c.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/321decfc24b08c837626c.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/321decfc24b08c837626c.jpg"
STATS_IMG_URL = "https://telegra.ph/file/321decfc24b08c837626c.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/321decfc24b08c837626c.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/321decfc24b08c837626c.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/321decfc24b08c837626c.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/321decfc24b08c837626c.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/321decfc24b08c837626c.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/321decfc24b08c837626c.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/321decfc24b08c837626c.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/321decfc24b08c837626c.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))



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
