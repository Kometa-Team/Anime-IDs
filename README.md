# Plex Meta Manager Anime IDs
Last generated at: December 29, 2022 01:24 AM UTC

This is a list for mapping MyAnimeList IDs and AniList IDs to AniDb IDs and then to TVDb IDs or IMDb IDs for us with [Plex-Meta-Manager](https://github.com/meisnate12/Plex-Meta-Manager).

This list is generated daily at 12:00 AM UTC 

## Lists
The two lists used to make pmm_anime_ids.json are below. If something is incorrect it likely needs to be fixed in one of those locations.
- [Anime-Lists/anime-lists](https://github.com/Anime-Lists/anime-lists/) for converting AniDb IDs to TVDb IDs or IMDb IDs
- [manami-project/anime-offline-database](https://github.com/manami-project/anime-offline-database/) for converting MyAnimeList IDs and AniList IDs to AniDb IDs

If they cannot be fixed at that location you can submit a PR to this repo and edit the pmm_edits.json file. Each entry is defined as follows:

```json
{
  "1": {
    "tvdb_id": 2,
    "mal_id": 3,
    "anilist_id": 4,
    "imdb_id": "tt5"
  }
}
```