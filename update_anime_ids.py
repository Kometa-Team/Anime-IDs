import json, os, sys
from datetime import datetime, UTC

if sys.version_info[0] != 3 or sys.version_info[1] < 11:
    print("Version Error: Version: %s.%s.%s incompatible please use Python 3.11+" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))
    sys.exit(0)

try:
    import requests
    from git import Repo
    from lxml import html
    from kometautils import KometaArgs, KometaLogger
except (ModuleNotFoundError, ImportError):
    print("Requirements Error: Requirements are not installed")
    sys.exit(0)

options = [
    {"arg": "tr", "key": "trace",        "env": "TRACE",        "type": "bool", "default": False, "help": "Run with extra trace logs."},
    {"arg": "lr", "key": "log-requests", "env": "LOG_REQUESTS", "type": "bool", "default": False, "help": "Run with every request logged."}
]
script_name = "Anime IDs"
base_dir = os.path.dirname(os.path.abspath(__file__))
args = KometaArgs("Kometa-Team/Anime-IDs", base_dir, options, use_nightly=False)
logger = KometaLogger(script_name, "anime_ids", os.path.join(base_dir, "logs"), is_trace=args["trace"], log_requests=args["log-requests"])
logger.screen_width = 160
logger.header(args, sub=True)
logger.separator()
logger.start()

AniDBIDs = html.fromstring(requests.get("https://raw.githubusercontent.com/Anime-Lists/anime-lists/master/anime-list-master.xml").content)
Manami = requests.get("https://raw.githubusercontent.com/manami-project/anime-offline-database/master/anime-offline-database.json").json()

anime_dicts = {}

logger.info("Scanning Anime-Lists")
for anime in AniDBIDs.xpath("//anime"):
    anidb_id = str(anime.xpath("@anidbid")[0])
    if not anidb_id:
        continue
    anidb_id = int(anidb_id[1:]) if anidb_id[0] == "a" else int(anidb_id)
    anime_dict = {}
    tvdb_id = str(anime.xpath("@tvdbid")[0])
    try:
        if tvdb_id:
            anime_dict["tvdb_id"] = int(tvdb_id)
    except ValueError:
        pass
    tvdb_season = str(anime.xpath("@defaulttvdbseason")[0])
    if tvdb_season == "a":
        tvdb_season = "-1"
    try:
        if tvdb_season:
            anime_dict["tvdb_season"] = int(tvdb_season)
    except ValueError:
        pass
    try:
        anime_dict["tvdb_epoffset"] = int(str(anime.xpath("@episodeoffset")[0]))
    except ValueError:
        anime_dict["tvdb_epoffset"] = 0

    imdb_id = str(anime.xpath("@imdbid")[0])
    if imdb_id.startswith("tt"):
        anime_dict["imdb_id"] = imdb_id
    anime_dicts[anidb_id] = anime_dict

logger.info("Scanning Manami-Project")
for anime in Manami["data"]:
    if "sources" not in anime:
        continue

    anidb_id = None
    mal_id = None
    anilist_id = None
    for source in anime["sources"]:
        if "anidb.net" in source:
            anidb_id = int(source.partition("anime/")[2])
        elif "myanimelist" in source:
            mal_id = int((source.partition("anime/")[2]))
        elif "anilist.co" in source:
            anilist_id = int((source.partition("anime/")[2]))
    if anidb_id and anidb_id in anime_dicts:
        if mal_id:
            anime_dicts[anidb_id]["mal_id"] = mal_id
        if anilist_id:
            anime_dicts[anidb_id]["anilist_id"] = anilist_id

logger.info("Scanning Anime ID Edits")
with open("anime_id_edits.json", "r") as f:
    for anidb_id, ids in json.load(f).items():
        anidb_id = int(anidb_id)
        if anidb_id in anime_dicts:
            for attr in ["tvdb_id", "mal_id", "anilist_id", "imdb_id"]:
                if attr in ids:
                    anime_dicts[anidb_id][attr] = ids[attr]

with open("anime_ids.json", "w") as write:
    json.dump(anime_dicts, write, indent=2)

logger.separator()

if [item.a_path for item in Repo(path=".").index.diff(None) if item.a_path.endswith(".json")]:

    logger.info("Saving Anime ID Changes")

    with open("README.md", "r") as f:
        data = f.readlines()

    data[2] = f"Last generated at: {datetime.now(UTC).strftime('%B %d, %Y %I:%M %p')} UTC\n"

    with open("README.md", "w") as f:
        f.writelines(data)
else:
    logger.info("No Anime ID Changes Detected")

logger.separator(f"{script_name} Finished\nTotal Runtime: {logger.runtime()}")
