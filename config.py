import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "23945390"))
API_HASH = getenv("API_HASH", "ebdbadc8f503b28abc4c52f7da6b9f18")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7282714112:AAFEQzVDEVdgXWw2pZhjYWzcnV5meDcgXJ4")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://erkbwrs084:909090@cluster0.qdrfgmb.mongodb.net/?retryWrites=true&w=majority")


DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 960))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002238574089"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7305205222"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Meyit47zade/MYTGRUPBOT",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/MytDuyuru")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DelularSohbet")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")

# Time after which you're assistant account will leave chats automatically.

AUTO_LEAVE_ASSISTANT_TIME = int(

    getenv("ASSISTANT_LEAVE_TIME", "3400")

)  # Remember to give value in Seconds

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 314572800))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 3221225472))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BAFtYK4AZnVwUkn3R-PHIydfuMQ-d5WBeasCN5p4pF4EdcJParIknV2ktIBSQOc0Q-0almcrGHCJL20GTfbhK-1MM_NWy5_aGlN6cbjXw06HhKr9YgAcmjc02PUGgCZlXH8Pb1WjzNVr4eMWpSR-9LfVi1BGLtBTkM9OQvdxD9WFUi3kbtVLo9k60Ly4kQmUWbfWo12zT6euqJ_Qo0rObRhhzQHXdagu74kQZXmW0wLUuYYe2_maor53oeof-T5YQ6ldCMqmD8E8C6WfBHdQ5I9L0sTUrKa1SbKAUuN4oWa7RyLTvguU-_-HHXo2jTnO0Eik7kDjH2foKPZMurnhbjhbtgmouwAAAAGi-S0sAA")
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
    if not re.match("(?:http|https)://", SUPPORT_CHAT):https://Sohbetikidebir
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
