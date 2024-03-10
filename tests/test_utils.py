import json


def get_numbers_response(client):
    response = client.get('/api/numbers/')
    return response


def get_number_response(client, id):
    response = client.get(f'/api/numbers/{id}/')
    return response


def patch_number_response(client, id, json):
    response = client.patch(f'/api/numbers/{id}/', json=json)
    return response


def post_numbers_response(client, json):
    response = client.post('/api/numbers/', json=json)
    return response


def delete_numbers_response(client, id):
    response = client.delete(f'/api/numbers/{id}/')
    return response


def decode_response(response):
    decoding = json.loads(response.data.decode('utf-8'))
    return decoding
