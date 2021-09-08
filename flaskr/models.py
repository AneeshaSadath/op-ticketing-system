import mongoengine
import mongoengine_goodjson as me
import datetime

from flaskr.validation import phone_number_validation, zipcode_validation

MARITAL_STATUS = ("Married", "Single")


class PatientData(me.Document):
    first_name = mongoengine.StringField(required=True)
    middle_name = mongoengine.StringField(default="")
    last_name = mongoengine.StringField(required=True)
    email = mongoengine.EmailField(default=None)
    home_phone = mongoengine.StringField(validation=phone_number_validation)
    mobile_phone = mongoengine.StringField(validation=phone_number_validation)
    address_1 = mongoengine.StringField(required=True)
    address_2 = mongoengine.StringField()
    city = mongoengine.StringField()
    state = mongoengine.StringField()
    zipcode = mongoengine.StringField(validation=zipcode_validation)
    marital_status = mongoengine.StringField(
        default="Single", choices=MARITAL_STATUS
    )
    gender = mongoengine.StringField(required=True)
    dob = mongoengine.DateTimeField(required=True)
    age = mongoengine.IntField(required=True)
    created_at = mongoengine.DateTimeField(default=datetime.datetime.utcnow)
