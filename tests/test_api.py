from .test_constants import (formatted_numbers,
                             test_json,
                             test_json_alt,
                             test_valid_jsons,
                             wrong_json,)
from .test_utils import (decode_response,
                         delete_numbers_response,
                         get_number_response,
                         get_numbers_response,
                         patch_number_response,
                         post_numbers_response)


def test_add_number(client):
    """Testing adding number"""
    response = post_numbers_response(client, test_json)
    assert response.status_code == 201
    res = decode_response(response).get("number")
    assert type(res) is dict
    assert res['phone'] == '+4367823232'


def test_add_same_number(client):
    """Testing adding non-unique number"""
    post_numbers_response(client, test_json)
    response = post_numbers_response(client, test_json)
    assert response.status_code == 400
    message = decode_response(response).get("message")
    assert message == 'This phone number has already been entered'


def test_add_invalid_number(client):
    """Testing adding invald number"""
    response = post_numbers_response(client, wrong_json)
    assert response.status_code == 400
    message = decode_response(response).get("message")
    assert message == 'This phone number is invalid'


def test_add_number_formatting(client):
    """Testing various number formatting"""
    form_list = list()
    for i in test_valid_jsons:
        response = post_numbers_response(client, i)
        assert response.status_code == 201
        res = decode_response(response).get('number')
        form_list.append(res['phone'])
        for i, j in zip(form_list, formatted_numbers):
            assert i == j


def test_get_numbers(client):
    """Testing get empty and filled db"""
    # Testing empty db
    response = get_numbers_response(client)
    assert response.status_code == 400
    message = decode_response(response).get("message")
    assert message == 'There are currently no phone numbers in the database'
    # Testing filled db
    post_numbers_response(client, test_json)
    response = get_numbers_response(client)
    res = decode_response(response).get("numbers")
    assert response.status_code == 200
    assert type(res[0]) is dict
    assert res[0]['phone'] == '+4367823232'
    assert type(res) is list


def test_get_number(client):
    """Testing getting number by id"""
    post_numbers_response(client, test_json)
    response = get_number_response(client, 1)
    assert response.status_code == 200
    res = decode_response(response).get("number")
    assert type(res) is dict
    assert res['phone'] == '+4367823232'


def test_patch_number(client):
    """Testing number patching"""
    post_numbers_response(client, test_json)
    response = patch_number_response(client, 1, test_json_alt)
    assert response.status_code == 201
    res = decode_response(response).get("number")
    assert type(res) is dict
    assert res['phone'] == '+4367933232'


def test_delete_number(client):
    """Testing number deletion"""
    post_numbers_response(client, test_json)
    response = delete_numbers_response(client, 1)
    assert response.status_code == 204
    assert response.data == b''
