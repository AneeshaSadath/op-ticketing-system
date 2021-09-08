import re

from mongoengine import ValidationError


def phone_number_validation(val):
    if not re.match("^[0-9]{3}[-|\\s][0-9]{3}[-|\\s][0-9]{4}$", val):
        raise ValidationError("value should be valid phone number")


def zipcode_validation(val):
    if not re.match("^\\d{5}(?:[-\\s]\\d{4})?$", str(val)):
        raise ValidationError("value should be valid zipcode")
