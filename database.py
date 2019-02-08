import pymongo

from config import DATABASE_HOST, DATABASE_PORT, DATABASE_NAME, DATABASE_PASSWORD, DATABASE_LOGIN

connection = pymongo.MongoClient(DATABASE_HOST, DATABASE_PORT)
db = connection[DATABASE_NAME]
db.authenticate(DATABASE_LOGIN, DATABASE_PASSWORD)


class PhotosDB:

    @classmethod
    def update_photos(cls, photos):
        for photo in photos[0]:
            photo['check_face'] = 'False'
            photo['face'] = ''
            photo['emotions'] = ''
            if not db.photos.find_one({"id": photo['id']}):
                db.photos.insert_one(photo)

    @classmethod
    def get_photos(cls):
        return db.photos.find()

    @classmethod
    def get_unchecked_face_photos(cls):
        return db.photos.find({"check_face": 'False'})

    @classmethod
    def update_photo(cls, photo):
        db.photos.find_one_and_update({"_id": photo['_id']},
                                      {"$set": {"check_face": photo['check_face'],
                                                "face": photo['face'],
                                                "emotions": photo['emotions']}})
