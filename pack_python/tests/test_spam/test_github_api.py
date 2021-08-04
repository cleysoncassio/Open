from unittest.mock import Mock

import pytest as pytest

from pack_python import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url ='https://avatars.githubusercontent.com/u/947107?v=4'
    resp_mock.json.return_value = {
        'login': 'cleysoncassio', 'id': 947107,
        'avatar_url': url,
    }
    get_mock = mocker.patch('pack_python.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('cleyso')
    assert avatar_url == url


def test_buscar_avatar_integração():
    url = github_api.buscar_avatar('cleysoncassio')
    assert 'https://avatars.githubusercontent.com/u/83619276?v=4' == url
