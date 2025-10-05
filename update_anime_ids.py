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

anime_dicts = {}

logger.info("Scanning Anime-Lists")
anidb_url = "https://raw.githubusercontent.com/Anime-Lists/anime-lists/master/anime-list-master.xml"
for anime in html.fromstring(requests.get(anidb_url).content).xpath("//anime"):
    anidb_id = str(anime.xpath("@anidbid")[0])
    if not anidb_id:
        continue
    anidb_id = int(anidb_id[1:]) if anidb_id[0] == "a" else int(anidb_id)
    if anidb_id not in anime_dicts:
        anime_dicts[anidb_id] = {}
    tvdb_id = str(anime.xpath("@tvdbid")[0])
    try:
        if tvdb_id:
            anime_dicts[anidb_id]["tvdb_id"] = int(tvdb_id)
    except ValueError:
        pass
    tvdb_season = str(anime.xpath("@defaulttvdbseason")[0])
    if tvdb_season == "a":
        tvdb_season = "-1"
    try:
        if tvdb_season:
            anime_dicts[anidb_id]["tvdb_season"] = int(tvdb_season)
    except ValueError:
        pass
    try:
        anime_dicts[anidb_id]["tvdb_epoffset"] = int(str(anime.xpath("@episodeoffset")[0]))
    except ValueError:
        anime_dicts[anidb_id]["tvdb_epoffset"] = 0

    imdb_id = str(anime.xpath("@imdbid")[0])
    if imdb_id.startswith("tt"):
        anime_dicts[anidb_id]["imdb_id"] = imdb_id


manami_url = "https://api.github.com/repos/manami-project/anime-offline-database/releases"
logger.info("Scanning Manami-Project")
manami_release_url = None
for asset in requests.get(requests.get(manami_url).json()[0]["assets_url"]).json():
    if asset["name"] == "anime-offline-database.json":
        manami_release_url = asset["browser_download_url"]
        break
for anime in requests.get(manami_release_url).json()["data"]:
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
"""
logger.info("Scanning AnimeAggregations")
aggregations_url = "https://raw.githubusercontent.com/notseteve/AnimeAggregations/main/aggregate/AnimeToExternal.json"
for anidb_id, anime in requests.get(aggregations_url).json()["animes"].items():
    anidb_id = int(anidb_id)
    if anidb_id not in anime_dicts:
        anime_dicts[anidb_id] = {}
    if "IMDB" in anime["resources"] and "imdb_id" not in anime_dicts[anidb_id]:
        anime_dicts[anidb_id]["imdb_id"] = ",".join(anime["resources"]["IMDB"])
    if "MAL" in anime["resources"] and "mal_id" not in anime_dicts[anidb_id]:
        anime_dicts[anidb_id]["mal_id"] = int(anime["resources"]["MAL"][0]) if len(anime["resources"]["MAL"]) == 1 else ",".join(anime["resources"]["MAL"])
    if "TMDB" in anime["resources"]:
        tmdb_tv_id = next((r for r in anime["resources"]["TMDB"] if r.startswith("tv")), None)
        if tmdb_tv_id:
            anime_dicts[anidb_id]["tmdb_show_id"] = int(tmdb_tv_id[3:])
        else:
            tmdb_movie_ids = [r[6:] for r in anime["resources"]["TMDB"] if r.startswith("movie")]
            anime_dicts[anidb_id]["tmdb_movie_id"] = int(tmdb_movie_ids[0]) if len(tmdb_movie_ids) == 1 else ",".join(tmdb_movie_ids)
"""

logger.info("Scanning Anime ID Edits")
with open("anime_id_edits.json", "r") as f:
    for anidb_id, ids in json.load(f).items():
        anidb_id = int(anidb_id)
        if anidb_id in anime_dicts:
            for attr in ["tvdb_id", "mal_id", "anilist_id", "imdb_id", "tmdb_show_id", "tmdb_movie_id"]:
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
