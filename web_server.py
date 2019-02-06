from aiohttp.web import Application, get, run_app
from handlers import Handler
from photo_data_worker import PhotoDataWorker
import config

PhotoDataWorker().start()
app = Application()
app.router.add_static('/static', config.STATIC_FOLDER)

handler = Handler(app)
app.add_routes([get('/', handler.handle_index)])


if __name__ == '__main__':
    run_app(app)
