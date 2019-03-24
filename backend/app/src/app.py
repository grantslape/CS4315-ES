from flask import Flask, jsonify
from datetime import datetime

from settings import ENVIRONMENT
from routes.index import index
from routes.reviews import reviews

app = Flask(__name__)

app.register_blueprint(index, url_prefix='/index')
app.register_blueprint(reviews, url_prefix='/reviews')


@app.route('/')
def heartbeat():
    return jsonify(time=str(datetime.now()), env=ENVIRONMENT)


if __name__ == "__main__":
    debug = True if ENVIRONMENT == 'development' else False
    app.run(host='0.0.0.0', port=5000, debug=debug)
