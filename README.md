# Script to Create Plex Collections

This github project allows to create collections for the Plex Library.

You can create collections from Oscar Winners in the ```read-from-oscars-csv``` folder.

![Best_Picture](https://i.imgur.com/Uy7G7YU.png)

---

From ```create-plex-collections-from-directories``` folder, you can create collections from your folder structure directly.

![Collections_from_directories](https://i.imgur.com/klX2KUk.png)

---

### Usage

Afterwards, after having your ```movie_oscars.yml``` and ```collections.yml``` files. Place them inside ```collections.d``` folder in ```plex-autocollections-master```

To install requirements, inside ```plex-autocollections-master``` run:

```sh
pip install -r requirements.txt
```

And execute ```main.py```:

```sh
python3 main.py
```

---

### Credits

Using ```plex-autocollections-master``` which is a fork of [plex-autocollections](https://github.com/alex-phillips/plex-autocollections) made by [Alex Philips](https://github.com/alex-phillips).

---

## License

This project is licensed under the terms of the **MIT** [license](https://github.com/ampzord/plex-autollection-script/blob/master/LICENSE).

