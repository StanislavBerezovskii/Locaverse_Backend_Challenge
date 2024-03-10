import json


def get_numbers_response(client):
    """Gets response for Retrieve-all CRUD operation"""
    response = client.get('/api/numbers/')
    return response


def get_number_response(client, id):
    """Gets response for Retrieve-one CRUD operation"""
    response = client.get(f'/api/numbers/{id}/')
    return response


def patch_number_response(client, id, json):
    """Gets response for Update CRUD operation"""
    response = client.patch(f'/api/numbers/{id}/', json=json)
    return response


def post_numbers_response(client, json):
    """Gets response for Create CRUD operation"""
    response = client.post('/api/numbers/', json=json)
    return response


def delete_numbers_response(client, id):
    """Gets response for Delete CRUD operation"""
    response = client.delete(f'/api/numbers/{id}/')
    return response


def decode_response(response):
    """Decodes API json response"""
    decoding = json.loads(response.data.decode('utf-8'))
    return decoding
