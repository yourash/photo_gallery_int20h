from threading import Thread

from face_plus_api import FaceRecognitionApi
from flickr_integration import FlickrApi
from database import PhotosDB
from time import sleep
import config


class PhotoDataWorker(Thread):

    def __init__(self):
        super().__init__()
        self.flickr_api = FlickrApi()
        self.photo_database = PhotosDB()
        self.face_api = FaceRecognitionApi(config.FACE_PLUS_PLUS_API_KEY,
                                           config.FACE_PLUS_PLUS_API_SECRET)

    def check_new_photos(self):
        all_photos = [self.flickr_api.get_all_by_album(config.FLICKR_ALBUM, config.FLICKR_USER),
                      self.flickr_api.get_all_by_tag('#int20h')]
        self.photo_database.update_photos(all_photos)

    def check_emotion_photo(self):
        photos = self.photo_database.get_unchecked_face_photos()
        for photo in photos:
            result = self.face_api.detect_face(photo['url_m']).json()
            if 'faces' in result:
                if result['faces']:
                    photo['check_face'] = True
                    photo['face'] = True
                    emotions = result['faces'][0]['attributes']['emotion']
                    weight_emotions = []
                    for emotion in emotions:
                        if emotions[emotion] > 20:
                            weight_emotions.append(emotion)
                    photo['emotions'] = weight_emotions
                    self.photo_database.update_photo(photo)
                else:
                    photo['check_face'] = True
                    photo['face'] = False
                    self.photo_database.update_photo(photo)
            sleep(4)

    def run(self):
        while True:
            self.check_new_photos()
            self.check_emotion_photo()
            sleep(4)
