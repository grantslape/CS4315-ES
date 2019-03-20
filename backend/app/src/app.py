from flask import Flask, jsonify
from datetime import datetime

from routes.index import index

app = Flask(__name__)

app.register_blueprint(index, url_prefix='/index')


@app.route('/heartbeat')
def heartbeat():
    return jsonify(time=str(datetime.now()), env='local')


if __name__ == "__main__":
    # TODO: check environment
    app.run(host='0.0.0.0', port=5000)
