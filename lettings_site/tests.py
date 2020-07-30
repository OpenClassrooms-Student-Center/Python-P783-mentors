import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_index(client):
    uri = reverse('index')
    resp = client.get(uri)
    assert 'title' in str(resp.content)
