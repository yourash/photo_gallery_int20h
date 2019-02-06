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

    @staticmethod
    def unique(lst):
        last = object()
        for item in lst:
            if item == last:
                continue
            yield item
            last = item

    def check_photos_repeating(self):
        results_union_of_photos = self.photo_database.get_photos()
        try:
            all_photos = [self.flickr_api.get_all_by_album(config.FLICKR_ALBUM, config.FLICKR_USER),
                          self.flickr_api.get_all_by_tag('#int20h')]
            results_union_of_photos = list(self.unique(all_photos))
        except Exception as e:
            print('check_photos_repeating: {}'.format(e))

        self.photo_database.update_photos(results_union_of_photos)

    def run(self):
        while True:
            self.check_photos_repeating()
            sleep(4)
