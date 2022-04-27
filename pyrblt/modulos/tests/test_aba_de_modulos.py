import pytest
from django.urls import reverse

from pyrblt.django_assertions import assert_contains
from model_bakery import baker

from pyrblt.modulos.models import Modulo


@pytest.fixture
def modulos(db):
    return baker.make(Modulo, 2)


@pytest.fixture
def resp(client, modulos):
    resp = client.get(reverse('base:home'))
    return resp


def test_titulos_dos_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)