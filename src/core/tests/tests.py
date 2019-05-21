import pytest


@pytest.mark.django_db
def test_products(client):
    response = client.post('/api/hs_codes_category/', {
        'category_name': 'animals',

    })
    assert response.status_code == 201

    # response = client.get('/api/hs_codes/')
    # assert response.status_code == 200
    # payload = response.json()
    #
    # assert payload[0].get('code') == '32456756'
    # assert payload[0].get('description') == 'fdghfdgfdg'
    # assert payload[0].get('short_description') == 'dfgdfgdfg'
    # assert payload[0].get('category_name') == 'animals'
    # assert payload[0].get('subcategory_name') == 'american animal'
