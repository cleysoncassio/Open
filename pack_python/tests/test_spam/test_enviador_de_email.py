import pytest as pytest

from pack_python.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['cleysoncassio@gmail.com', 'tatianevirgilio8@gmail.com'])
def test_remetente(destinatario):
    enviador = Enviador()
    destinatarios = ['cleysoncassio@gmail.com', 'tatianevirgilio8@gmail.com']
    destinatario
    resultado = enviador.enviar(
        destinatario,
        'academiarocksfit@gmail.com',
        'teste de envio de email',
        'Primeira turma Guido Von Rossum aberta.'
    )

    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    [',', 'academiarocksfit']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'academiarocksfit@gmail.com',
            'teste de envio de email',
            'Primeira turma Guido Von Rossum aberta.'
        )
