import os

listProd = {}
listPreco = {}
listQtde = {}

total = 0

while True:
    print(
    """
╠══============================ BOAS-VINDAS =================================══╣
  ____    _____     _____              _   _   _____    _____    ____     _____ 
 / __ \  |  __ \   / ____|     /\     | \ | | |_   _|  / ____|  / __ \   / ____|
| |  | | | |__) | | |  __     /  \    |  \| |   | |   | |      | |  | | | (___  
| |  | | |  _  /  | | |_ |   / /\ \   | . ` |   | |   | |      | |  | |  \___ \ 
| |__| | | | \ \  | |__| |  / ____ \  | |\  |  _| |_  | |____  | |__| |  ____) |
 \____/  |_|  \_\  \_____| /_/    \_\ |_| \_| |_____|  \_____|  \____/  |_____/ 

╠══========================= MENU DE NAVEGAÇÃO ==============================══╣

                                1-Cadastro 
                                2-Vendas 
                                3-Relatório 
                                4-Sair 
                              """)
    opcao = input("""
                        INFORME A OPÇÃO DESEJADA: """)
    os.system('cls')
    match opcao:
        case '1':
            print("""
            Menu de Cadastro:​
            a) Cadastrar produtos;
            b) Listar produtos cadastrados;
            c) Deletar produtos;
            d) Voltar ao menu anterior.​
            """)
            opcao_cadastro = input('Escolha uma opção: ').lower()
            os.system('cls')
            if opcao_cadastro == 'a':
                
                produto = input('Digite o produto a ser cadastrado: ').lower()
                listProd[produto] = produto
                
                preco = (input('Digite o preço do produto, com "." separando os centavos: R$ '))
                if preco.replace('.','',1).isdigit():
                    preco = float(preco)
                    if preco <= 0:
                        input('Valor inválido. Aperte "Enter" para...')
                else:
                    print('Apenas números positivos são admitidos no cadastro de preços de produtos.')
                    input('Aperte "Enter" para...')
                    continue
                listPreco[produto] = preco
                
                qtde = input('Digite a quantidade do produto: ')
                if qtde.isdigit():
                    qtde = int(qtde)
                    if qtde <= 0:
                        input('Quantidade inválida. Aperte "Enter" para retornar ao Menu de Navegação.')
                else:
                    print('Apenas números positivos são admitidos no cadastro de quantidades de produtos.')
                    input('Aperte "Enter" para retornar ao Menu de Navegação.')
                listQtde[produto] = qtde
                """
                #novo_prod=input('Deseja cadastrar mais algum produto? Digite S para "Sim" ou N para "Não": ' ).lower()
                
                if novo_prod == 'n':
                    pass
                if novo_prod != 's':
                    novo_prod=input('Opção inválida. Digite S para "Sim" ou N para "Não": ')
                """                   
            elif opcao_cadastro == 'b':
                if len(listProd) == 0:
                    print('Não há produtos cadastrados!')
                
                else:
                    print('A lista de produtos cadastrados é: \n')
                    for produto in listProd:
                        print(f'{listProd[produto]}        R${listPreco[produto]}            {listQtde[produto]} und')
                input('Aperte "Enter" para retornar ao Menu de Navegação.')            

            elif opcao_cadastro == 'c':
                if len(listProd) == 0:
                    print('Não há produtos cadastrados!')
                    
                else:
                    print('A lista de produtos cadastrados é: \n')
                
                    for produto in listProd:
                        print(f'{listProd[produto]}        R${listPreco[produto]}            {listQtde[produto]} und')
                
                    delete = input('Digite o produto a ser deletado: ').lower()
                    listProd.pop(delete)
                    listPreco.pop(delete)
                    listQtde.pop(delete)
                input('Aperte "Enter" para continuar.')

                '''del_outro = input('Deseja deletar mais algum produto? Digite S para "Sim" ou N para "Não": ' ).lower()
                
                while del_outro == 'n':
                    pass
                if del_outro != 's':
                    del_outro=input('Opção inválida. Digite S para "Sim" ou N para "Não": ')'''

            elif opcao_cadastro == 'd':
                continue
            elif opcao_cadastro not in('a','b','c','d'):
                input('Opção inválida. Aperte "Enter" para retornar ao Menu de Navegação.')

        case '2':
            print("""
            Menu de Vendas:
            
            a) Adicionar produtos ao carrinho;
            b) Finalizar a compra;
            c) Voltar ao menu anterior.

            """)
            opcao_venda = input('Escolha uma opção: ').lower()

            os.system('cls')

            while opcao_venda == 'a':
                print("Produtos disponíveis: \n")
                for produto in listProd:
                    print(f'{listProd[produto]}        R${listPreco[produto]}            {listQtde[produto]} und\n')

                p = input("Digite o nome do produto que deseja comprar: \n")
                v = 0

                while p not in listProd[produto]:
                    p = input("Produto não encontrado. Digite um item válido: \n")

                if p in listProd[produto]:
                    q = int(input("Digite a quantidade a ser comprada: \n"))

                    while q > listQtde[produto]:
                        print("A quantidade informada deve ser igual ou menor do que a quantidade disponível.\n")
                        q = int(input("Digite uma quantidade válida: \n"))

                    if q <= listQtde[produto]:
                        v += q * float(listPreco[produto])
                        total += v

                        print("O seguinte item foi adicionado ao carrinho:\nProduto: ", p, "\nQuantidade: ", q, "\nPreço: R$", v)
                        
                        opçao = int(input("""Deseja adicionar mais algum item?
                                1 - Sim
                                2 - Não\n"""))
                        if opçao == 1:
                            continue
                        else:
                            break
                
            if opcao_venda == 'b':
                print("Compra finalizada!\nTotal da compra: R$", total)
                input('Aperte "Enter" para retornar ao Menu de Navegação.')

            elif opcao_venda == 'c':
                continue
            elif opcao_venda not in('a','b','c'):
                input('Opção inválida. Aperte "Enter" para retornar ao Menu de Navegação.')

                
        case '3':
            print("""
            Menu de Relatório: 
            
            a) Obter extrato de produtos vendidos;
            b) Voltar ao menu anterior.

            """)
            opcao_extrato = input('Escolha uma opção: ').lower()
            
            if opcao_extrato == 'a':
                pass
            elif opcao_extrato == 'b':
                continue
            elif opcao_extrato not in('a','b'):
                input('Opção inválida. Aperte "Enter" para retornar ao Menu de Navegação.')

                        
        case '4':
            print('Volte sempre!.')
            break
        
        case _:
            input('Opção Inválida. Aperte "Enter" para retornar ao Menu de Navegação.')