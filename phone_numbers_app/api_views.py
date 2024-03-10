import phonenumbers
import re

from flask import jsonify, request, Blueprint
from http import HTTPStatus

from .extensions import db
from .error_handlers import InvalidAPIUsage
from .models import PhoneNumber

main = Blueprint("main", __name__)

@main.route('/api/numbers/<int:id>/', methods=['GET'])
def get_number(id):
    """API endpoint for Retrieve-one CRUD operation"""
    number = PhoneNumber.query.get(id)
    if number is None:
        raise InvalidAPIUsage(
            'The requested object was not found in the database'
            )
    return jsonify({'number': number.to_dict()}), HTTPStatus.OK


@main.route('/api/numbers/<int:id>/', methods=['PATCH'])
def update_number(id):
    """API endpoint for Update CRUD operation"""
    data = request.get_json()
    if 'phone' not in data or data['phone'] == '':
        raise InvalidAPIUsage('Please enter the phone number')
    cleaning = re.sub(r'[-()\\s]', '', data['phone'])
    parsing = phonenumbers.parse(f'{cleaning}', 'AT')
    if phonenumbers.is_valid_number(parsing) == 0:
        raise InvalidAPIUsage('This phone number is invalid')
    E614_f = phonenumbers.format_number(
                parsing,
                phonenumbers.PhoneNumberFormat.E164
            )
    if PhoneNumber.query.filter_by(phone=E614_f).first() is not None:
        raise InvalidAPIUsage('This phone number has already been entered')
    number = PhoneNumber.query.get_or_404(id)
    number.phone = E614_f
    db.session.commit()
    return jsonify({'number': number.to_dict()}), HTTPStatus.CREATED


@main.route('/api/numbers/<int:id>/', methods=['DELETE'])
def delete_number(id):
    """API endpoint for Delete CRUD operation"""
    number = PhoneNumber.query.get_or_404(id)
    db.session.delete(number)
    db.session.commit()
    return '', HTTPStatus.NO_CONTENT


@main.route('/api/numbers/', methods=['GET'])
def get_numbers():
    """API endpoint for Retrieve-all CRUD operation"""
    numbers = PhoneNumber.query.all()
    numbers_list = [number.to_dict() for number in numbers]
    if not bool(numbers_list):
        raise InvalidAPIUsage('There are currently no phone '
                              'numbers in the database')
    return jsonify({'numbers': numbers_list}), HTTPStatus.OK


@main.route('/api/numbers/', methods=['POST'])
def add_number():
    """API endpoint for Create CRUD operation"""
    data = request.get_json()
    if 'phone' not in data or data['phone'] == '':
        raise InvalidAPIUsage('Please enter the phone number')
    number = PhoneNumber()
    number.from_dict(data)
    if PhoneNumber.query.filter_by(phone=number.phone).first() is not None:
        raise InvalidAPIUsage('This phone number has already been entered')
    db.session.add(number)
    db.session.commit()
    return jsonify({'number': number.to_dict()}), HTTPStatus.CREATED
