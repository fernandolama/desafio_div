from flask import Flask
from flask import request, redirect
import pandas as pd

app = Flask(__name__)

produtos = {} #{produto: [valor, quantidade]}

df = pd.read_csv('catalogo.csv', index_col='produto')
print(df)

@app.route("/cad")
def cad():
    argumentos = request.args.to_dict()
    
    produto = argumentos['produto'] #arroz
    preco = argumentos['preco'] #10
    quantidade = argumentos['quantidade'] #10
    
    #dicionário
    produtos[produto] = [preco, quantidade]
    #dataframe
    df.loc[produto] = [preco, quantidade]
    df.to_csv('catalogo.csv')
    df.to_html('catalogo.html')
    print(df)
    return redirect('static/cadastrado.html')

@app.route('/del')
def delet():
    argumentos = request.args.to_dict()

    prod_del = argumentos['prod_del']
    qtde_del = argumentos['qtde_del']

    if len(produtos) == 0:
        print('Não há produtos cadastrados!')
                    
    else:
        print('A lista de produtos cadastrados é: \n')
                
        for p in produtos:
            print(f'{produtos[p]}        R${preco[p]}            {quantidade[p]} und')
                               
        while qtde_del > quantidade[prod_del]:
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

if __name__ == "__main__":
    app.run(debug=True)