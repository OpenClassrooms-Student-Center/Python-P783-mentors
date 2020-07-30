import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_index(client):
    uri = reverse('profiles:index')
    resp = client.get(uri)
    assert 'title' in str(resp.content)


@pytest.mark.django_db
def test_profile(client):
    uri = reverse('profiles:profile', kwargs={'username': '4meRomance'})
    resp = client.get(uri[1:])
    assert 'title' in str(resp.content)
