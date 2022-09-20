#SETUP
import os

#FUNÇÕES
#Função de cadastro de produto
def cadastro_produto():
    #Cadastrar produto
    produto = input('Digite o produto a ser cadastrado: ').lower()
    listProd[produto] = produto
                
    #Cadastrar preço
    preco = input('Digite o preço do produto, com "." separando os centavos: R$ ')
    if preco.replace('.','',1).isdigit():
        preco = float(preco)
    else:
        print('Valor inválido. Apenas números positivos são admitidos no cadastro de preços de produtos.')
        print(f'O produto', produto, 'não pôde ser cadastrado.')
        input('Aperte "Enter" para continuar.')
        listProd.clear()
        os.system('cls')
        return
    listPreco[produto] = preco         
    
    #Cadastrar quantidade
    qtde = input('Digite a quantidade do produto: ')
    if qtde.isdigit():
        qtde = int(qtde)
        while qtde <= 0:
            qtde = int(input('Quantidade inválida. Digite um valor maior do que 1 para a quantidade do produto: '))
        
    else:
        print('Valor inválido. Apenas números positivos são admitidos no cadastro de quantidades de produtos.')
        print(f'O produto', produto, 'não pôde ser cadastrado.')
        input('Aperte "Enter" para continuar.')
        listProd.clear()
        listPreco.clear()
        os.system('cls')
        return
    listQtde[produto] = qtde
    os.system('cls')

#Função de deletar produtos
def deletar_produto():
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