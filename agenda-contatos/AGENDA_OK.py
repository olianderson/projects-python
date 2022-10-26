#SIMULAÇÃO DE UMA AGENDA TELEFÔNICA
#claudio gay

AGENDA = dict()

AGENDA['anderson'] = {
    'telefone': '98985589999',
    'email': 'anderson@gmail.com',
    'endereco': 'Avenida 01',
}

AGENDA['yasmin'] = {
    'telefone': '98984308888',
    'email': 'yasmin@gmail.com',
    'endereco': 'Avenida 02',
}

def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print('Sem contatos na agenda.')


def buscar_contato(contato):
    try:
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('Email:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereco'])
        print('--------------------------------------------')

    except KeyError:
        print('O contato {} não está na agenda.'.format(contato))

    except Exception as error:
        print('OPS!! Um erro inesperado ocorreu')
        print(error)


def ler_contato():
    telefone = input('Digite o nome do telefone: ')
    email = input('Digite o nome do email: ')
    endereco = input('Digite o nome do endereco: ')

    return telefone, email, endereco


def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    salvar_alteracoes()
    print()
    print('O contato {} foi adicionado/editado'.format(contato))
    print()


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar_alteracoes()
        print()
        print('O contato {} foi excluído da agenda'.format(contato))
        print()

    except KeyError:
        print('Contato não existe na agenda')

    except Exception as error:
        print('OPS!! Um erro inesperado ocorreu ao excluir o contato')
        print(error)


def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write("{},{},{},{}\n".format(contato, telefone, email, endereco))
        print('Os contatos da agenda foram exportados com sucesso.')
    
    except Exception as error:
        print('OPS!! Um erro inesperado ocorreu ao exportar contatos')
        print(error)


def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()

            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_editar_contato(nome, telefone, email, endereco)

    except FileNotFoundError:
        print('Arquivo não encontrado')

    except Exception as error:
        print('OPS!! Um erro inesperado ocorreu ao inportar contatos')
        print(error)

def salvar_alteracoes():
    exportar_contatos('database.csv')


def load():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()

            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco,
                }
        print('Database carregado com sucesso')
        print('{} contatos carregados'.format(len(AGENDA)))

    except FileNotFoundError:
        print('Arquivo não encontrado.')

    except Exception as error:
        print('Algum erro inesperado ocorreu.')
        print(error)


#MENU DO PROGRAMA

def menu():
    print(
        '\n1 - Mostrar todos os contatos da agenda \n'
        '2 - Buscar contato \n' 
        '3 - Incluir contato \n'
        '4 - Editar contato \n'
        '5 - Excluir contato \n'
        '6 - Exportar contatos para .CSV \n'
        '7 - Importar contatos .CSV \n'
        '0 - Sair do programa \n'
    )


#INICIO DO PROGRAMA
load()
while True:
    menu()

    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        mostrar_contatos()

    elif opcao == '2':
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)

    elif opcao == '3':
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('Contato já existente na agenda')

        except KeyError:
            telefone, email, endereco = ler_contato()
            incluir_editar_contato(contato, telefone, email, endereco)

    elif opcao == '4':
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('Editando contato: {}'.format(contato))
            telefone, email, endereco = ler_contato()
            incluir_editar_contato(contato, telefone, email, endereco)

        except KeyError:
            print('O contato não existe.')

    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)

    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo a ser exportado: ')
        exportar_contatos(nome_do_arquivo)

    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo a ser importado: ')
        importar_contatos(nome_do_arquivo)

    elif opcao == '0':
        print('Encerrando programa...')
        break

    else:
        print('OPÇÃO INVÁLIDA.')
