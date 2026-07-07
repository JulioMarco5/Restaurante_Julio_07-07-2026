import os
from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_nome_do_progama():
    print("""  
░██████╗███████╗███╗░░██╗░█████╗░░█████╗░
██╔════╝██╔════╝████╗░██║██╔══██╗██╔══██╗
╚█████╗░█████╗░░██╔██╗██║███████║██║░░╚═╝
░╚═══██╗██╔══╝░░██║╚████║██╔══██║██║░░██╗
██████╔╝███████╗██║░╚███║██║░░██║╚█████╔╝
╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝░╚════╝░
""")


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Adicionar avaliação')
    print('5. Adicionar item ao cardápio')
    print('6. Exibir cardápio')
    print('7. Sair')


def cadastrar_restaurante():
    limpar_tela()

    print('Cadastro de Restaurante\n')
    nome = input('Nome: ')
    categoria = input('Categoria: ')

    Restaurante(nome, categoria)

    print(f'\n{nome} cadastrado com sucesso!')
    input('\nPressione Enter para voltar ao menu...')


def listar_restaurantes():
    limpar_tela()

    print('Lista de Restaurante\n')

    Restaurante.listar_restaurantes()
    
    input('\nPressione Enter para voltar ao menu...')


def alternar_estado_restaurante():
    nome = input("Digite o nome do restaurante: ")

    for restaurante in Restaurante.restaurantes:
        if restaurante._nome.lower() == nome.lower():
            restaurante._ativo = not restaurante._ativo

            if restaurante._ativo:
                print(f"{restaurante._nome} ativado com sucesso!")
            else:
                print(f"{restaurante._nome} desativado com sucesso!")
            return

    print("Restaurante não encontrado.")


def adicionar_avaliacao():
    nome = input("Nome do restaurante: ")

    for restaurante in Restaurante.restaurantes:
        if restaurante._nome.lower() == nome.lower():

            cliente = input("Nome do cliente: ")
            nota = int(input("Nota (0 a 5): "))

            restaurante.receber_avaliacao(cliente, nota)

            print("Avaliação cadastrada!")
            return

    print("Restaurante não encontrado.")


def adicionar_item_no_cardapio():
    nome = input("Nome do restaurante: ")

    for restaurante in Restaurante.restaurantes:
        if restaurante._nome.lower() == nome.lower():

            tipo = input("1 - Prato\n2 - Bebida\nEscolha: ")

            nome_item = input("Nome: ")
            preco = float(input("Preço: "))

            if tipo == "1":
                descricao = input("Descrição: ")
                prato = Prato(nome_item, preco, descricao)
                restaurante.adicionar_no_cardapio(prato)

            elif tipo == "2":
                tamanho = input("Tamanho: ")
                bebida = Bebida(nome_item, preco, tamanho)
                restaurante.adicionar_no_cardapio(bebida)

            print("Item adicionado com sucesso!")
            return

    print("Restaurante não encontrado.")


def exibir_cardapio():
    nome = input("Nome do restaurante: ")

    for restaurante in Restaurante.restaurantes:
        if restaurante._nome.lower() == nome.lower():
            restaurante.exibir_cardapio()
            return

    print("Restaurante não encontrado.")


def finalizar_app():
    limpar_tela()
    print('Programa encerrado!')


def escolher_opcao():

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar_restaurante()

    elif opcao == "2":
        listar_restaurantes()

    elif opcao == "3":
        alternar_estado_restaurante()

    elif opcao == "4":
        adicionar_avaliacao()

    elif opcao == "5":
        adicionar_item_no_cardapio()

    elif opcao == "6":
        exibir_cardapio()
        input('\nPressione Enter para voltar ao menu...')

    elif opcao == "7":
        finalizar_app()
        exit()

    else:
        print("Opção inválida.")


def main():
    while True:
        limpar_tela()
        exibir_nome_do_progama()
        exibir_opcoes()
        escolher_opcao()
        
if __name__ == "__main__":
    main()