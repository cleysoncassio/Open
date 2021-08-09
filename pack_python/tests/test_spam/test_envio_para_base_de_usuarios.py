from unittest.mock import Mock
import pytest as pytest
from pack_python.spam.main import EnviadorDeSpam
from pack_python.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='cleyson', email='cleysoncassio@gmail.com'),
            Usuario(nome='Tatiane', email='tatianvevirgilio8@gmail.com')
        ],
        [
            Usuario(nome='cleyson', email='cleysoncassio@gmail.com')
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
        'teste assunto',
        'teste corpo'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='cleyson', email='cleysoncassio@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'tatianevirgilio8@gmail.com',
        'teste assunto',
        'teste corpo'
    )
    enviador.enviar.assert_called_once_with(
        'tatianevirgilio8@gmail.com',
        'cleysoncassio@gmail.com',
        'teste assunto',
        'teste corpo'
    )
