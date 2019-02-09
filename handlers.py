from database import PhotosDB
import aiohttp_jinja2
import jinja2
import config


class Handler:

    def __init__(self, app):
        aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(config.TEMPLATES_FOLDER))

    @aiohttp_jinja2.template('index.html')
    async def handle_index(self, request):
        print('index')
        photos = await PhotosDB().get_photos()
        return {'photos': photos}

    @aiohttp_jinja2.template('emotion.html')
    async def handle_emotion(self, request):
        print(request.match_info.get('emotion'))
        photos = await PhotosDB().get_photos()
        return {'photos': photos}
