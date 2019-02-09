# Photo gallery with emotions recognition

Gallery with face and emotions recognition written on python3 aiohttp.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to run the software:

```
Python3.6+, pip3, MongoDB
```

### Installing

A step by step instruction for installation:

Create your MongoDb database on [MLab](https://mlab.com)

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

DATABASE_HOST = 'ds12345.mlab.com'
DATABASE_PORT = 27228
DATABASE_NAME = 'int_20h'

DATABASE_LOGIN = 'admin'
DATABASE_PASSWORD = 'password'

EMOTIONS = {'anger': 'Гнев',
            'disgust': 'Отвращение',
            'fear': 'Страх',
            'happiness': 'Счастье',
            'neutral': 'Нейтральный',
            'sadness': 'Печаль',
            'surprise': 'Удивленный'}
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

![Main page](https://i.ibb.co/Qbzdnhq/Screenshot-from-2019-02-09-14-19-52.png)
![Emotions](https://i.ibb.co/ZRQK8m0/Screenshot-from-2019-02-09-14-20-16.png)

## Deployment

Don't forget to create `config.py`

Run
```bash
heroku create
git push heroku master
```

## Developers

Developed by [Momentum bots](https://momentum-bots.top) team.

* **Anton Yurash** - *Web server development* - [YouRASH](https://github.com/yourash)
* **Alex Komarsiy** - *Database development* - [Komarskiy](https://github.com/Komarskiy)
