import os
from xml.sax.handler import property_declaration_handler

listProd = {}
listPreco = {}
listQtde = {}

total = 0

while True:
# Tela de boas-vindas/Menu de navegação
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
            #Menu de cadastro
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
                #Cadastrar produto
                produto = input('Digite o produto a ser cadastrado: ').lower()
                listProd[produto] = produto
                
                #Cadastrar preço
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
                
                #Cadastrar quantidade
                qtde = input('Digite a quantidade do produto: ')
                if qtde.isdigit():
                    qtde = int(qtde)
                    if qtde <= 0:
                        input('Quantidade inválida. Aperte "Enter" para retornar ao Menu de Navegação.')
                        os.system('cls')
                else:
                    print('Apenas números positivos são admitidos no cadastro de quantidades de produtos.')
                    input('Aperte "Enter" para retornar ao Menu de Navegação.')
                listQtde[produto] = qtde
                os.system('cls')
                """
                novo_prod=input('Deseja cadastrar mais algum produto? Digite S para "Sim" ou N para "Não": ' ).lower()
                
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
                        print()
                
                input('\nAperte "Enter" para retornar ao Menu de Navegação.')
                os.system('cls')            

            elif opcao_cadastro == 'c':
                if len(listProd) == 0:
                    print('Não há produtos cadastrados!')
                    
                else:
                    print('A lista de produtos cadastrados é: \n')
                
                    for produto in listProd:
                        print(f'{listProd[produto]}        R${listPreco[produto]}            {listQtde[produto]} und')
                
                    prod_del = input('Digite o produto a ser deletado: ').lower()
                    qtde_del = int(input('Digite a quantidade de itens a serem deletados: '))
                    
                    while qtde_del > listQtde[prod_del]:
                        qtde_del = int(input('A quantidade digite é maior do que a quantidade em estoque. Digite uma quantidade menor: '))

                    if qtde_del <= listQtde[prod_del] and qtde_del > 0:
                        novaqtde = listQtde[prod_del] - qtde_del
                        listQtde.update({prod_del: novaqtde})
                    
                    if listQtde[prod_del] == 0:
                        listProd.pop(prod_del)
                        listPreco.pop(prod_del)
                    
                print(qtde_del,'unidades do produto',prod_del,'foram deletadas com sucesso!')
                input('Aperte "Enter" para continuar.')
                os.system('cls')

                '''del_outro = input('Deseja deletar mais algum produto? Digite S para "Sim" ou N para "Não": ' ).lower()
                
                while del_outro == 'n':
                    pass
                if del_outro != 's':
                    del_outro=input('Opção inválida. Digite S para "Sim" ou N para "Não": ')'''

            elif opcao_cadastro == 'd':
                os.system('cls')
                continue
            
            elif opcao_cadastro not in('a','b','c','d'):
                input('Opção inválida. Aperte "Enter" para retornar ao Menu de Navegação.')
                os.system('cls')

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

                p = input("Digite o nome do produto que deseja comprar: \n").lower()
                v = 0

                while p not in listProd[produto]:
                    p = input("Produto não encontrado. Digite um item válido: \n").lower()

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
                            os.system('cls')
                            continue
                        else:
                            os.system('cls')
                            break
                
            if opcao_venda == 'b':
                print("Compra finalizada!\nTotal da compra: R$", total)
                input('Aperte "Enter" para retornar ao Menu de Navegação.')
                os.system('cls')

            elif opcao_venda == 'c':
                os.system('cls')
                continue
            elif opcao_venda not in('a','b','c'):
                input('Opção inválida. Aperte "Enter" para retornar ao Menu de Navegação.')
                os.system('cls')

                
        case '3':
            print("""
            Menu de Relatório: 
            
            a) Obter extrato de produtos vendidos;
            b) Voltar ao menu anterior.

            """)
            opcao_extrato = input('Escolha uma opção: ').lower()
            
            if opcao_extrato == 'a':
                os.system('cls')
                pass
            elif opcao_extrato == 'b':
                os.system('cls')
                continue
            elif opcao_extrato not in('a','b'):
                input('Opção inválida. Aperte "Enter" para retornar ao Menu de Navegação.')
                os.system('cls')

                        
        case '4':
            print('Volte sempre!.')
            break
        
        case _:
            input('Opção Inválida. Aperte "Enter" para retornar ao Menu de Navegação.')
            os.system('cls')