import pytest


@pytest.mark.django_db
def test_products(client):
    response = client.post('/api/hs_codes_category/', {
        'category_name': 'animals',
        'hs_code_category_id': "feb03e3e-5b7f-4abf-b100-d52a143150eb"

    })
    assert response.status_code == 201
    category_id = response.json()['id']
    response = client.post('/api/hs_codes_subcategory/', {
            'hs_code_category_id': category_id,
            'subcategory_name': 'dfgdfgdfgdfg'
    })
    assert response.status_code == 201
    subcatid = response.json()['id']
    response = client.post('/api/hs_codes/', {
        'code': '23423',
        'description': 'dfgfdgdfg',
        'short_description': 'dfgdfggfdgf',
        'hs_code_category_id': category_id,
        'hs_code_subcategory': subcatid
    })

    assert response.status_code == 201



