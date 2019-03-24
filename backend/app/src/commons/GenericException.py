from flask import jsonify


class GenericException(Exception):
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        payload = dict(self.payload or ())
        rv = {'message': self.message, 'payload': payload}
        return rv
