# Photo gallery with emotions recognition

Gallery with face and emotions recognition written on python3 aiohttp.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to run the software:

```
Python3.6+, pip3
```

### Installing

A step by step instruction for installation:

Create `config.py` in project root dir:

```python
FLICKR_KEY = 'asdf09a0sd8f9ad8sf9a'
FLICKR_SECRET = '3452345kl3245k2345l'
FLICKR_ALBUM = '72157674388093532'
FLICKR_USER = '144522605@N06'

TEMPLATES_FOLDER = 'templates/'
STATIC_FOLDER = 'static/'

FACE_PLUS_PLUS_API_KEY = 'bkjh234jk32h4vkjh4k2j3hbk42jh'
FACE_PLUS_PLUS_API_SECRET = '023lk4jhb2lj3h4b8s-aiXp4234kjhb'
```

Install python packages

```bash
sudo pip3 install requirements.txt
```

Run
```bash
python3 webserver.py
```

Then open [localhost:8080](http://0.0.0.0:8080)

![Result will be like this](https://i.ibb.co/f8X51Qv/Screenshot-from-2019-02-06-20-41-48.png)

## Deployment

TODO

## Developers

Developed by [Momentum bots team](https://momentum-bots.top).

* **Anton Yurash** - *Web server development* - [YouRASH](https://github.com/yourash)
* **Alex Komarsiy** - *Database development* - [TODO]()
