from pack_python.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='cleyson', email='cleysoncassio@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='cleyson', email='cleysoncassio@gmail.com'),
                Usuario(nome='Tatiane', email='cleysoncassio@gmail.com')
                ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
