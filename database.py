import json


class PhotosDB:

    PHOTO_FILE = 'photo_data.json'

    @classmethod
    def get_photos(cls):
        with open(cls.PHOTO_FILE) as file:
            return json.load(file)['photos']

    @classmethod
    def update_photos(cls, photos):
        with open(cls.PHOTO_FILE, 'w') as file:
            return json.dump({'photos': photos}, file)
