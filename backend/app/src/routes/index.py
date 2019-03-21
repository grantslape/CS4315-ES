from flask import Blueprint, request, jsonify

index = Blueprint('index', __name__)


@index.route('', methods=["POST"])
def create_index():
    return jsonify(msg='created an index')
