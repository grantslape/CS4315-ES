"""Flask API for interacting with an Elasticsearch cluster"""
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
from werkzeug.exceptions import NotFound, BadRequest

from commons import setup_conn, error_response, build_response, GenericException
from commons.misc import set_up
from models import BusinessElastic, CheckinElastic, TipElastic, UserElastic, ReviewElastic
from routes import index, document, search
from settings import ENVIRONMENT

app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(index, url_prefix='/index/<string:name>')
app.register_blueprint(document, url_prefix='/doc/<string:name>/<int:doc_id>')
app.register_blueprint(search, url_prefix='/search')

setup_conn()
set_up('reviews', ReviewElastic)
set_up('users', UserElastic)
set_up('tips', TipElastic)
set_up('checkins', CheckinElastic)
set_up('businesses', BusinessElastic)


@app.before_request
def only_json():
    if request.method in ('POST', 'PUT') and not request.is_json:
        return error_response(400, 'Request is not valid json')


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


if __name__ == '__main__':
    debug = True if ENVIRONMENT == 'development' else False
    app.run(host='0.0.0.0', port=5000, debug=debug)
