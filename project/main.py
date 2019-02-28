from sanic import Sanic

app = Sanic(__name__)


def init():
    app.run(host='0.0.0.0', port=8000, debug=True)
