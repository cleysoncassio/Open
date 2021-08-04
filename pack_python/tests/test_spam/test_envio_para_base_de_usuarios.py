from unittest.mock import Mock

import pytest as pytest


from pack_python.spam.main import EnviadorDeSpam
from pack_python.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='RKS', email='academiarocksfit@gmail.com'),
            Usuario(nome='Tatiane', email='academiarocksfit@gmail.com')
        ],
        [
            Usuario(nome='RKS', email='academiarocksfit@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'cleysoncassio@gmail.com',
        'teste',
        'Confira nossas novidades'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='academiarocksfit', email='academiarocksfit@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'academiarocksfit@gmail.com',
        'Teste',
        'Confira nossas novidades'
    )
    enviador.enviar.assert_called_once_with(
        'academiarocksfit@gmail.com',
        'academiarocksfit@gmail.com',
        'Teste',
        'Confira nossas novidades'
    )
