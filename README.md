# Plex Meta Manager Anime IDs
Last generated at: January 04, 2023 01:23 AM UTC

This is a list for mapping MyAnimeList IDs and AniList IDs to AniDb IDs and then to TVDb IDs or IMDb IDs for us with [Plex-Meta-Manager](https://github.com/meisnate12/Plex-Meta-Manager).

This list is generated daily at 12:00 AM UTC 

## Format

This is an example entry you would find in the [pmm_anime_ids.json](https://raw.githubusercontent.com/meisnate12/Plex-Meta-Manager-Anime-IDs/master/pmm_anime_ids.json) file.

```json
{
  "11": {
    "tvdb_id": 70900,
    "imdb_id": "tt7941838",
    "mal_id": 821,
    "anilist_id": 821
  }
}
```

- The main key of each entry is the AniDb ID of the entry. 
- `tvdb_id`: This is always the Series ID that contains the show/season/movie/special. **This should never be a TVDb Movie ID or TVDb Season ID.**
- `imdb_id`: This should be the IMDb ID of the Series for shows and seasons, but should link directly to the IMDb ID of the Movie or Special if it is one. You can provide multiple comma-separated IMDb IDs if the Anime is a series of Movies/Specials.
- `mal_id`: This should link directly to the exact same anime on [MyAnimeList.net](https://myanimelist.net). You can provide multiple comma-separated MyAnimeList IDs if the Anime has multiple entries.
- `anilist_id`: This should link directly to the exact same anime on [AniList.co](https://anilist.co). You can provide multiple comma-separated MyAnimeList IDs if the Anime has multiple entries.

## Lists
The two lists used to make pmm_anime_ids.json are below. If something is incorrect it likely needs to be fixed in one of those locations.
- [Anime-Lists/anime-lists](https://github.com/Anime-Lists/anime-lists/) for converting AniDb IDs to TVDb Series IDs or IMDb IDs. If there is an issue with these IDs it would be best to fix the source list usually.
- [manami-project/anime-offline-database](https://github.com/manami-project/anime-offline-database/) for converting MyAnimeList IDs and AniList IDs to AniDb IDs. If there is an issue with these IDs the source list generally will not make manuel edits so it would be best to submit your edits using the `pmm_edits.json` file.


## PMM Edits
If there are incorrect IDs and the source list will not change the ID then you can submit a PR to this repo and edit the `pmm_edits.json` file. The format of each entry is defined above. You should only edit the IDs you actually want changed.

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