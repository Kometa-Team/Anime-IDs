# Kometa Anime IDs

Last generated at: June 03, 2024 01:19 AM UTC

This is an autogenerated list for mapping AniDB IDs to MyAnimeList IDs, AniList IDs, TVDb IDs, and IMDb IDs for use with [Kometa](https://github.com/Kometa-Team/Kometa).

This list is generated daily at 12:00 AM UTC 

## Format

This is an example mapping entry you would find in the [anime_ids.json](https://raw.githubusercontent.com/Kometa-Team/Anime-IDs/master/anime_ids.json) file.

```json
{
  "11": {
    "tvdb_id": 70900,
    "imdb_id": "tt7941838",
    "mal_id": 821,
    "anilist_id": 821,
    "tmdb_movie_id": 327796,
    "tmdb_show_id": 12121
  }
}
```

- The main key of each entry is the AniDB ID of the entry. 
- `tvdb_id`: This is always the Series ID that contains the show/season/movie/special. **This should never be a TVDb Movie ID or TVDb Season ID.**
- `imdb_id`: This should be the IMDb ID of the Series for shows and seasons, but should link directly to the IMDb ID of the Movie or Special if it is one. You can provide multiple comma-separated IMDb IDs if the Anime is a series of Movies/Specials.
- `mal_id`: This should link directly to the exact same anime on [MyAnimeList.net](https://myanimelist.net). You can provide multiple comma-separated MyAnimeList IDs if the Anime has multiple entries.
- `anilist_id`: This should link directly to the exact same anime on [AniList.co](https://anilist.co). You can provide multiple comma-separated MyAnimeList IDs if the Anime has multiple entries.
- `tmdb_movie_id`: This looks at the AniDB site under the resources for the anime. 
- `tmdb_show_id`: This looks at the AniDB site under the resources for the anime. 

## Source Lists

The two source lists used to autogenerate `anime_ids.json` are below. 
1. [Anime-Lists/anime-lists](https://github.com/Anime-Lists/anime-lists/) maps AniDB IDs to TVDb Series IDs and IMDb IDs. ([Raw List](https://raw.githubusercontent.com/Anime-Lists/anime-lists/master/anime-list-master.xml))
2. [manami-project/anime-offline-database](https://github.com/manami-project/anime-offline-database/) maps AniDB IDs to MyAnimeList IDs and AniList IDs. ([Raw List](https://raw.githubusercontent.com/manami-project/anime-offline-database/master/anime-offline-database.json))
3. [notseteve/AnimeAggregations](https://github.com/notseteve/AnimeAggregations) parses data from the AniDB site and maps the links there to TMDb IDs, IMDb IDs, and MyAnimeList IDs.

## Make Changes

To change ID's mapped in the autogenerated `anime_ids.json` you can either update the [Anime-Lists/anime-lists](https://github.com/Anime-Lists/anime-lists/) List for TVDb IDs and IMDb IDs or add the Source to MyAnimeList for MyAnimeList IDs and AniList IDs.

If that doesn't work you can also submit a Pull Request to the Repo editing the `anime_id_edits.json` file. The format of each entry is defined above. You should only edit the IDs you actually want changed.

```json
{
  "9826": {
    "mal_id": "18397,25781,36106"
  },
  "10583": {
    "mal_id": "23775,23777"
  }
}
```

## Common Kometa Convert Erorrs

If any **Solution** doesn't work you can always manually make changes using the `anime_id_edits.json` file.

- `No TVDb ID or IMDb ID found for AniDB ID: #####`
  - **Issue:** [Anime-Lists](https://raw.githubusercontent.com/Anime-Lists/anime-lists/master/anime-list-master.xml) does not have a TVDb ID or IMDb ID with the given AniDB ID. 
  - **Solution:** Raise an Issue or submit a Pull Request to [Anime-Lists/anime-lists](https://github.com/Anime-Lists/anime-lists/) with the ID added.

- `AniDB ID not found for MyAnimeList ID: #####`
  - **Issue:** Kometa received a MyAnimeList ID from a Builder and that MyAnimeList ID doesn't have an AniDB Source on [manami-project](https://raw.githubusercontent.com/manami-project/anime-offline-database/master/anime-offline-database.json). 
  - **Solution:** [manami-project/anime-offline-database](https://github.com/manami-project/anime-offline-database/) is an automated list and doesn't accept Pull Requests. You can try and update MyAnimeList directly but I don't know when or even if that info will populate back to this list.

- `AniDB ID not found for AniList ID: #####`
  - **Issue:** Kometa received a AniList ID from a Builder and that AniList ID doesn't have an AniDB Source on [manami-project](https://raw.githubusercontent.com/manami-project/anime-offline-database/master/anime-offline-database.json). 
  - **Solution:** [manami-project/anime-offline-database](https://github.com/manami-project/anime-offline-database/) is an automated list and doesn't accept Pull Requests. You can try and update MyAnimeList directly but I don't know when or even if that info will populate back to this list.

- `AniDB ID: {anidb_id} not found`
  - **Issue:** Kometa is looking at an AniDB ID that is not found on [Anime-Lists](https://raw.githubusercontent.com/Anime-Lists/anime-lists/master/anime-list-master.xml).
  - **Solution:** However Kometa is getting the ID is probably wrong either a builder sending bad data or guid tag in plex has a non-numeric character.

- `AniDB ID not found for IMDb ID: #####`
  - **Issue:** Kometa received an IMDb ID from a Builder and that IMDb ID is not attached to any AniDB ID on [Anime-Lists](https://raw.githubusercontent.com/Anime-Lists/anime-lists/master/anime-list-master.xml). 
  - **Solution:** Raise an Issue or submit a Pull Request to [Anime-Lists/anime-lists](https://github.com/Anime-Lists/anime-lists/) with the ID added.

- `AniDB ID not found for TVDb ID: #####`
  - **Issue:** Kometa received a TVDb ID from a Builder and that TVDb ID is not attached to any AniDB ID on [Anime-Lists](https://raw.githubusercontent.com/Anime-Lists/anime-lists/master/anime-list-master.xml). 
  - **Solution:** Raise an Issue or submit a Pull Request to [Anime-Lists/anime-lists](https://github.com/Anime-Lists/anime-lists/) with the ID added.