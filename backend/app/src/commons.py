from flask import make_response, jsonify


def build_response(obj: object):
    """Build a flask response"""
    response = make_response(jsonify(obj))
    response.headers['Content-Type'] = 'application/json'
    return response


def json_response(obj: object, status: int):
    """Build a flask response from a given JSON body"""
    response = make_response(obj, status)
    response.headers['Content-Type'] = 'application/json'
    return response


def custom_response(obj: object):
    response = make_response(obj)
    return response


def error_response(status: int, message: str):
    """Build a flask error response from a given message and status code"""
    return build_response({'status': status, 'message': message}), status
