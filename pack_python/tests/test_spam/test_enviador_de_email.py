import pytest as pytest

from pack_python.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['academiarocksfit@gmail.com', 'cleysoncassio@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'tatianevirgilio8@gmail.com',
        'teste Assunto',
        'teste Corpo'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'cleysoncassio']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'tatianevirgilio8@gmail.com',
            'teste Assunto',
            'teste Corpo'
        )
