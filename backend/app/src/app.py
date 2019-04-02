"""Flask API for interacting with an Elasticsearch cluster"""
from flask import Flask, request, jsonify
from datetime import datetime
from werkzeug.exceptions import NotFound, BadRequest

from commons import setup_conn, error_response, build_response, GenericException
from commons.misc import set_up
from models import Review, User, Tip, Checkin, Business
from routes import index, reviews, businesses
from settings import ENVIRONMENT

app = Flask(__name__)

app.register_blueprint(index, url_prefix='/index/<name>')
app.register_blueprint(reviews, url_prefix='/reviews')
# TODO de-duplicate code so we can use 1 route for all CRUD operations
app.register_blueprint(businesses, url_prefix='/doc')

setup_conn()
set_up('reviews', Review)
set_up('users', User)
set_up('tips', Tip)
set_up('checkins', Checkin)
set_up('businesses', Business)


@app.before_request
def only_json():
    if not request.is_json:
        return error_response(400, 'Request is not valid json:')


# Error Handlers
@app.errorhandler(GenericException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.errorhandler(404)
def page_not_found(e: NotFound):
    return build_response({'message': e.description}), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return build_response({'message': e.description}), 405


@app.errorhandler(400)
def malformed_payload(e: BadRequest):
    return build_response({'message': e.description}), 400


@app.route('/')
def heartbeat():
    return build_response({'time': str(datetime.now()), 'env': ENVIRONMENT})


if __name__ == "__main__":
    debug = True if ENVIRONMENT == 'development' else False
    app.run(host='0.0.0.0', port=5000, debug=debug)
