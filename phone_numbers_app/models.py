import phonenumbers
import re

from .extensions import db
from .error_handlers import InvalidAPIUsage


class PhoneNumber(db.Model):
    """The main project database model"""
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(15), nullable=False, unique=False)

    def to_dict(self):
        """Serializes model object into json format"""
        return dict(
            id=self.id,
            phone=self.phone
        )

    def from_dict(self, data):
        """De-serializes model object from json format"""
        if 'phone' in data:
            cleaning = re.sub(r'[-()\\s]', '', data['phone'])
            parsing = phonenumbers.parse(f'{cleaning}', 'AT')
            if phonenumbers.is_valid_number(parsing) == 0:
                raise InvalidAPIUsage('This phone number is invalid')
            E614_f = phonenumbers.format_number(
                parsing,
                phonenumbers.PhoneNumberFormat.E164
            )
            setattr(self, 'phone', E614_f)
