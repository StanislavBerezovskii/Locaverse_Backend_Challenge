from flask import jsonify, Blueprint

errors = Blueprint("errors", __name__)


class InvalidAPIUsage(Exception):
    """A custom Exception template for the project"""
    status_code = 400

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return dict(message=self.message)


@errors.app_errorhandler(InvalidAPIUsage)
def invalid_api_usage(error):
    """A custom json Error for the project"""
    return jsonify(error.to_dict()), error.status_code
