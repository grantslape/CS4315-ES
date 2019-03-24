from flask import Flask, request, jsonify
from datetime import datetime

from commons.GenericException import GenericException
from commons.responses import error_response, build_response
from settings import ENVIRONMENT
from routes.index import index
from routes.reviews import reviews

app = Flask(__name__)

app.register_blueprint(index, url_prefix='/index/<name>')
app.register_blueprint(reviews, url_prefix='/reviews')


@app.before_request
def only_json():
    if not request.is_json:
        return error_response(400, 'Request is not valid json:')


@app.errorhandler(GenericException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/')
def heartbeat():
    return build_response({'time': str(datetime.now()), 'env': ENVIRONMENT})


if __name__ == "__main__":
    debug = True if ENVIRONMENT == 'development' else False
    app.run(host='0.0.0.0', port=5000, debug=debug)
