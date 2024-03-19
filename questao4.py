# BOAS VINDAS
print('\nBem-vindo ao Controle de livros do Maicon da Silva Botelho RU: 1904125')
print('""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')

# VARIÁVEIS GLOBAIS
lista_livro = []
id_global = 0


# FUNÇÃO CADASTRAR LIVRO
def cadastrar_livro(id):
    print('------------------------ MENU CADASTRAR LIVRO ------------------------')
    nome = input('Por favor entre com o nome do livro: ').upper()
    autor = input('Por favor entre com o nome do autor: ').upper()
    editora = input('Por favor entre com o nome da editora: ').upper()

    # CRIA UM DICIONÁRIO
    livro = {
        'ID': id,
        'Nome': nome,
        'Autor': autor,
        'Editora': editora
    }

    # ADICIONA O DICIONÁRIO A LISTA DE LIVROS
    lista_livro.append(livro)
    print('Livro cadastrado com sucesso!')


# FUNÇÃO CONSULTAR LIVRO
def consultar_livro():
    while True:
        try:
            print('------------------------ MENU CONSULTAR LIVRO ------------------------')
            print('Escolha a opção desejada:')
            print('1 - Consultar Todos os Livros')
            print('2 - Consultar Livro por ID')
            print('3 - Consultar Livro(s) por Autor')
            print('4 - Retornar ao menu principal')
            opcaoMenuConsulta = input('>> ')
            if opcaoMenuConsulta not in ['1', '2', '3', '4']:
                raise ValueError('Opção inválida! Escolha entre 1, 2, 3 ou 4')

        except ValueError as e:
            print('\n***', e, '***\nPor favor tente novamente!\n')
            continue

        if opcaoMenuConsulta == '1':
            # CONSULTA TODOS OS LIVROS
            print('Consulta de todos os livros:')

            if lista_livro:
                for livro in lista_livro:
                    print('id:', livro['ID'])
                    print('nome:', livro['Nome'])
                    print('autor:', livro['Autor'])
                    print('editora:', livro['Editora'])
                    print('============================')
            else:
                print('Nenhum livro encontrado.')

        elif opcaoMenuConsulta == '2':
            # CONSULTA POR ID
            id_consulta = int(input('Digite o ID do livro a ser consultado: '))
            encontrado = False
            for livro in lista_livro:
                if livro['ID'] == id_consulta:
                    print('Livro encontrado:')
                    print('id:', livro['ID'])
                    print('nome:', livro['Nome'])
                    print('autor:', livro['Autor'])
                    print('editora:', livro['Editora'])
                    print('============================')
                    encontrado = True
                    break

            if not encontrado:
                print('Livro não encontrado.')


        elif opcaoMenuConsulta == '3':
            # CONSULTA POR AUTOR
            autor_consulta = input('Digite o nome do autor a ser consultado: ').upper()
            livros_encontrados = [livro for livro in lista_livro if livro['Autor'] == autor_consulta]
            if livros_encontrados:
                print('Livros encontrados:')
                for livro in livros_encontrados:
                    print('id:', livro['ID'])
                    print('nome:', livro['Nome'])
                    print('autor:', livro['Autor'])
                    print('editora:', livro['Editora'])
                    print('============================')
            else:
                print('Nenhum livro encontrado para o autor especificado.')


        elif opcaoMenuConsulta == '4':
            # RETORNA AO MENU
            print('Retornando ao menu principal...')
            break

        print('""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')


# FUNÇÃO REMOVER LIVRO
def remover_livro():
    print('------------------------ MENU REMOVER LIVRO --------------------------')
    while True:
        # VERIFICA SE O VALOR DIGITADO É NÚMERICO
        try:
            id_remover = int(input('Digite o ID do livro a ser removido: '))
            break
        except ValueError:
            print('Por favor, digite um valor numérico válido para o ID.')

    # REMOVE O LIVRO PELO ID
    for livro in lista_livro:
        if livro['ID'] == id_remover:
            lista_livro.remove(livro)
            print('Livro removido com sucesso!')
            break
    else:
        print('Livro não encontrado.')


# PROGRAMA PRINCIPAL
while True:
    try:
        print('--------------------------- MENU PRINCIPAL ---------------------------')
        print('Escolha a opção desejada:')
        print('1 - Cadastrar Livro')
        print('2 - Consultar Livro(s)')
        print('3 - Remover Livro')
        print('4 - Sair')
        opcaoMenu = input('>> ')
        print('""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')

        if opcaoMenu not in ['1', '2', '3', '4']:
            raise ValueError('Opção inválida! Escolha entre 1,2,3 ou 4')

    except ValueError as e:
        print('\n***', e, '***\nPor favor tente novamente!\n')

    if opcaoMenu == '1':
        # CADASTRAR LIVRO
        id_global += 1
        cadastrar_livro(id_global)

    elif opcaoMenu == '2':
        # CONSULTAR LIVROS
        consultar_livro()

    elif opcaoMenu == '3':
        # REMOVER LIVRO
        remover_livro()

    elif opcaoMenu == '4':
        # ENCERRA O PROGRAMA
        print('Encerrando o programa...')
        break

    print('""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')
