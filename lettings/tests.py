import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_index(client):
    uri = reverse('lettings:index')
    resp = client.get(uri)
    assert 'title' in str(resp.content)


@pytest.mark.django_db
def test_letting(client):
    uri = reverse('lettings:letting', kwargs={'letting_id': 3})
    resp = client.get(uri[1:])
    assert 'title' in str(resp.content)
