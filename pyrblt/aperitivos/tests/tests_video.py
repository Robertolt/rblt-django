import pytest
from django.urls import reverse

from pyrblt.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp):
    assert_contains(resp, '<h1>Vídeo Aperitivo: Motivação</h1>')


def test_conteudo_video(resp):
    assert_contains(resp, '<div style="padding:75% 0 0 0;position:relative;"><iframe '
                          'src="https://player.vimeo.com/video/694576600?h=4451873560&amp;badge=0&amp;autopause=0&amp'
                          ';player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; '
                          'picture-in-picture" allowfullscreen '
                          'style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Seasonal Sale - '
                          'Spring"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>')