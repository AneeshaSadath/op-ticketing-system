import pytest
from mongoengine import ValidationError
from flaskr.validation import phone_number_validation, zipcode_validation


@pytest.mark.parametrize('number', ["832-610-9681", "832 610 9681"])
def test_phone_number_validation(number):
    try:
        phone_number_validation(number)
        assert True
    except ValidationError:
        assert False


@pytest.mark.parametrize('number', ["832-610-968", "832-6109681", "8326109681"])
def test_phone_number_validation_with_invalid_number(number):
    with pytest.raises(ValidationError):
        phone_number_validation(number)


@pytest.mark.parametrize('zipcode', ["77752", "77752 2345", "77752-2345"])
def test_zipcode_validation(zipcode):
    try:
        zipcode_validation(zipcode)
        assert True
    except ValidationError:
        assert False


@pytest.mark.parametrize('zipcode', ["7775", "77752/2345", "7775-2345", "7775 2345"])
def test_zipcode_validation_with_invalid_zipcode(zipcode):
    with pytest.raises(ValidationError):
        phone_number_validation(zipcode)


