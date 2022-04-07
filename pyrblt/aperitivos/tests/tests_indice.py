import pytest
from django.urls import reverse

from pyrblt.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'slug', [
        'Vídeo Aperitivo: Motivação',
        'Instalando Windows',
    ]
)
def test_titulo_video(resp, slug):
    assert_contains(resp, slug)


@pytest.mark.parametrize(
    'slug', [
        'motivacao',
        'instalacao-windows',
    ]
)
def test_link_video(resp, slug):
    link_video = reverse('aperitivos:video', args=(slug,))
    assert_contains(resp, f'href"{link_video}"')