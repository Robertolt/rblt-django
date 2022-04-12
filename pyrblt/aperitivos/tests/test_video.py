import pytest
from django.urls import reverse

from pyrblt.aperitivos.models import Video
from pyrblt.django_assertions import assert_contains


@pytest.fixture
def video(db):
    v = Video(slug='motivacao', titulo='Vídeo Aperitivo: Motivação', vimeo_id='694576600')
    v.save()
    return v


@pytest.fixture
def resp(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug,)))


@pytest.fixture
def resp_video_nao_encontrado(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug+'video_nao_existente',)))


def test_status_code_video_nao_encontrado(resp_video_nao_encontrado):
    assert resp.status_code == 404


def test_status_code(resp):
    assert resp_video_nao_encontrado.status_code == 200


def test_titulo_video(resp, video):
    assert_contains(resp, video.titulo)


def test_conteudo_video(resp):
    assert_contains(resp, '<div style="padding:75% 0 0 0;position:relative;"><iframe '
                          f'src="https://player.vimeo.com/video/{video.vimeo_id}?h=4451873560&amp;badge=0&amp"'
                          ';autopause=0&amp '
                          ';player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; '
                          'picture-in-picture" allowfullscreen '
                          'style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Seasonal Sale - '
                          'Spring"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>')
