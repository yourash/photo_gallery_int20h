import requests
import config


class FaceRecognitionApi:

    URL = 'https://api-us.faceplusplus.com/facepp/v3/'

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def detect_face(self, image_url):
        response = None
        try:
            response = requests.post(self.URL + 'detect', data={
                'api_key': self.api_key,
                'api_secret': self.api_secret,
                'image_url': image_url,
                'return_attributes': 'emotion'
            })
        except Exception as e:
            print('{}'.format(e))
        return response


if __name__ == '__main__':
    face_api = FaceRecognitionApi(config.FACE_PLUS_PLUS_API_KEY,
                                  config.FACE_PLUS_PLUS_API_SECRET)
    print(face_api.detect_face('https://img.rl0.ru/f3f70ad4661bcac56b285cb86efdea1e/c615x400/'
                               'news.rambler.ru/img/2018/05/23142637.159422.8999.jpg').text)
