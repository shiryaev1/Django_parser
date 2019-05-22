import pytest
import json


@pytest.mark.django_db
def test_products(client):
    response = client.post('/api/hs_codes_category/', {
        'category_name': 'cars',

    })

    assert response.status_code == 201
    category_id = response.json()['id']
    response = client.post('/api/hs_codes_subcategory/', {
            'hs_code_category_id': category_id,
            'subcategory_name': 'bmv'
    })
    assert response.status_code == 201
    subcategory_id = response.json()['id']
    response = client.post('/api/hs_codes/', {
        'code': '23423',
        'description': 'cool car',
        'short_description': 'cool',
        'hs_code_category': category_id,
        'hs_code_subcategory': subcategory_id
    })

    assert response.status_code == 201

    response = client.get('/api/hs_codes/')

    assert response.status_code == 200

    payload = response.json()
    hs_code_category_id = response.json()[0].get('hs_code_category')
    hs_code_subcategory = response.json()[0]['hs_code_subcategory']

    assert payload[0].get('code') == '23423'
    assert payload[0].get('description') == 'cool car'
    assert payload[0].get('short_description') == 'cool'
    assert payload[0].get('hs_code_category') == hs_code_category_id
    assert payload[0].get('hs_code_subcategory') == hs_code_subcategory

    hs_subcategory_id = response.json()[0]['hs_code_subcategory']
    hs_code_id = response.json()[0]['id']
    response = client.put(f'/api/hs_codes/{hs_code_id}/', json.dumps({
        'code': '23423',
        'description': 'cool car',
        'short_description': 'cool',
        'hs_code_subcategory': hs_subcategory_id

    }), content_type='application/json')

    assert response.status_code == 200

    response = client.delete(f'/api/hs_codes/{hs_code_id}/')

    assert response.status_code == 204





