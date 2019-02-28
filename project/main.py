from sanic import Sanic

from environs import Env
from project.settings import Settings

app = Sanic(__name__)


def init():
    env = Env()
    env.read_env()

    app.config.from_object(Settings)
    app.run(
        host=app.config.HOST,
        port=app.config.PORT,
        debug=app.config.DEBUG,
        auto_reload=app.config.DEBUG,
    )
