from database import PhotosDB
import aiohttp_jinja2
import jinja2
import config


class Handler:

    def __init__(self, app):
        aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(config.TEMPLATES_FOLDER))

    @aiohttp_jinja2.template('index.html')
    async def handle_index(self, request):
        photos = PhotosDB().get_photos(emotion='happiness')
        return {'photos': photos, 'emotions': config.EMOTIONS}

    @aiohttp_jinja2.template('emotion.html')
    async def handle_emotion(self, request):
        photos = PhotosDB().get_photos(emotion=request.match_info.get('emotion'))
        return {'photos': photos, 'emotions': config.EMOTIONS}

    @aiohttp_jinja2.template('emotion.html')
    async def global_filter(self, request):
        if request.match_info.get('global_filter') == 'all':
            photos = PhotosDB().get_photos()
        elif request.match_info.get('global_filter') == 'faces':
            photos = PhotosDB().get_photos(only_faces=True)
        return {'photos': photos, 'emotions': config.EMOTIONS}
