import os, json
from flask import jsonify

from config.logger import logger


def success_response(data=None, message=None, code=200, **extra):
    logger.info(message)
    return {
        "data": data,
        "meta": {
            "message": message,
            "code": code,
            **extra
        }
    }


def error_response(message, code=400):
    response = jsonify({
        "message": message,
        "code": code
    })
    response.status_code = code
    logger.error(message)
    return response


def get_message(path, data):
    file_path = os.getcwd() + "/src/general/message.json"
    with open(file_path, "r") as file:
        message = json.loads(file.read())
        return message[path][data]