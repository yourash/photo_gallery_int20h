from threading import Thread
from flickr_integration import FlickrApi
from database import PhotosDB
from time import sleep
import config


class PhotoDataWorker(Thread):

    def __init__(self):
        super().__init__()
        self.flickr_api = FlickrApi()
        self.photo_database = PhotosDB()

    def check_photos_repeating(self):
        all_photos = [self.flickr_api.get_all_by_album(config.FLICKR_ALBUM, config.FLICKR_USER),
                      self.flickr_api.get_all_by_tag('#int20h')]
        self.photo_database.update_photos(all_photos)

    def run(self):
        while True:
            self.check_photos_repeating()
            sleep(4)
