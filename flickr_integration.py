from flickrapi import FlickrAPI
from config import FLICKR_KEY, FLICKR_SECRET


class FlickrApi:

    def __init__(self):
        self.flickr = FlickrAPI(FLICKR_KEY, FLICKR_SECRET, format='parsed-json')
        self.extras = 'url_s,url_m,url_o'

    def get_all_by_album(self, album, user):
        photos = {}
        try:
            photos = self.flickr.photosets.getPhotos(photoset_id=album,
                                                     user=user,
                                                     tag_mode='all',
                                                     extras=self.extras)['photoset']['photo']
        except Exception as e:
            print('{}'.format(e))
        return photos

    def get_all_by_tag(self, tag):
        photos = {}
        try:
            photos = self.flickr.photos.search(text=tag,
                                               tag_mode='all',
                                               extras=self.extras,)['photos']['photo']
        except Exception as e:
            print('{}'.format(e))
        return photos


