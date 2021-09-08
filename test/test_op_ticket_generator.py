import pytest
from tasks import op_ticket_generator

DATA = {
    "first_name": "test_name",
    "middle_name": "test_mid",
    "last_name": "test_last",
    "email": "test@gmail.com",
    "home_phone": "832-610-9681",
    "mobile_phone": "832-610-9681",
    "address_1": "test_palce",
    "address_2": "test_place",
    "city": "test_city",
    "state": "test_state",
    "zipcode": "77568",
    "marital_status": "Single",
    "gender": "Female",
    "dob": "29/03/1998",
    "age": 24,
}

LIST_DATA = ("ID", ["TEST1", "TEST2"])
STRING_DATA = ("ID", "DATA")
TUPLE_DATA = ("ID", ("TEST1", "TEST2"))

STRING_ID = ("ID", DATA)
NUMERICAL_ID = (12344, DATA)


@pytest.mark.parametrize('id,data', [STRING_ID, NUMERICAL_ID])
def test_op_ticket_generator(id, data):
    try:
        # when
        op_ticket_generator(id, data)
        # then
        assert True
    except TypeError:
        assert False


def test_op_ticket_generator_without_id():
    with pytest.raises(TypeError):
        data = DATA
        op_ticket_generator(data)


@pytest.mark.parametrize('id,data', [LIST_DATA, STRING_DATA, TUPLE_DATA])
def test_op_ticket_generator_with_invalid_data(id, data):
    with pytest.raises(TypeError):
        op_ticket_generator(id, data)