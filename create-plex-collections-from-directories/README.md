Create Plex Collections from Folder Directories
============

This script creates a collections.yml file to create collections for Plex.

Scanning the folder structure the script finds every folder with "(Collection)" and automatically creates collections with every Movie inside the folder.

Allowing to make Collections from Directors, Movie Trilogies, Disney Movies, etc.


## Followed Folder Structure

The folder structure in this script is the one followed by [Plex](https://support.plex.tv/articles/naming-and-organizing-your-movie-media-files/).

```
├── Movies\
|   ├── 2001 - A Space Odyssey (1968)\
│   │   ├── 2001 - A Space Odyssey (1968).mp4
│   │   └── 2001 - A Space Odyssey (1968).eng.srt
│   ├── Alfred Hitchcock (Collection)\
│   │   ├── Rear Window (1954)\
|   |   |   ├── Rear Window (1954).mp4
│   │   │   └── Rear Window (1954).eng.srt
│   │   ├── The Birds (1963)\
|   |   |   ├── The Birds (1963).mp4
│   │   │   └── The Birds (1963).eng.srt
│   │   ├── ...
│   ├── Back to the Future (Collection)\
│   │   ├── Back to the Future (1985)\
|   |   |   ├── Back to the Future (1985).mp4
│   │   │   └── Back to the Future (1985).eng.srt
│   │   ├── ├── Back to the Future Part II (1989)\
|   |   |   ├── Back to the Future (1989).mp4
│   │   │   └── Back to the Future Part II (1989).eng.srt
│   │   ├── ├── Back to the Future Part III (1990)\
|   |   |   ├── Back to the Future Part III (1990).mp4
│   │   │   └── Back to the Future Part III (1990).eng.srt
|   ├── Ben-Hur (1959)\
│   │   ├── Ben-Hur (1959).mp4
│   │   └── Ben-Hur (1959).eng.srt
|   ├── ...
|   └── create_collections_for_plex.py
```

---

## How to Run

```sh
python create_collections_for_plex.py
```

---
