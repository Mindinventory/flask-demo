from flask import Blueprint, jsonify

user = Blueprint('user', __name__)


@user.route('/info', methods=['GET'])
def get_user_info():
    return jsonify({'message': 'User information endpoint'})
