from ctypes.wintypes import tagMSG
from keyword import issoftkeyword
from flask import Flask
from flask import request, redirect, render_template
import pandas as pd

app = Flask(__name__)


prod_carrinho = {}

catalogo = pd.read_csv('catalogo.csv', index_col='produto')
carrinho = pd.read_csv('carrinho.csv', index_col='produto')

produtos = catalogo.to_dict(orient='index')
'''produtos = {
    chave: list(valor.values()) 
    for chave,valor in produtos.items()
    }'''

dicionario = {}
for chave, valor in produtos.items():
    dicionario[chave] = list(valor.values())

produtos = dicionario.copy()
del dicionario
print(produtos)

@app.route("/")
def index():
    return "olá"

@app.route("/cad")
def cad():
    argumentos = request.args.to_dict()
    
    produto = argumentos['produto'] #arroz
    preco = float(argumentos['preco']) #10
    quantidade = int(argumentos['quantidade']) #10
    
    #dicionário
    produtos[produto] = [preco, quantidade]
    #dataframe
    catalogo.loc[produto] = [preco, quantidade]
    
    catalogo.to_csv('catalogo.csv')
    catalogo.to_html('catalogo.html')
    print(catalogo)
    return redirect('static/cadastrado.html')

@app.route('/lista')
def lista():
    return render_template('lista.html', lista=catalogo.to_html())

@app.route('/del')
def delet():
    argumentos = request.args.to_dict()

    prod_del = argumentos['prod_del']
    qtde_del = int(argumentos['qtde_del'])

    # if qtde_del <= quantidades[prod_del] and qtde_del > 0:
    #     nova_qtde = quantidades[prod_del] - qtde_del
    #     quantidades.update({prod_del: nova_qtde})

    # if quantidades[prod_del] == 0:
    #     produtos.pop(prod_del)
    #     precos.pop(prod_del)

    #deleção usando dataframe
    # quantidade maior ou igual ao catalogo
    if catalogo.loc[prod_del, 'quantidade'] <= qtde_del:
        catalogo.drop(prod_del, axis=0, inplace=True)
    else:
        catalogo.loc[prod_del, 'quantidade'] = catalogo.loc[prod_del, 'quantidade'] - qtde_del

    
    catalogo.to_csv('catalogo.csv')
    catalogo.to_html('catalogo.html')
    print(catalogo)
    return redirect('static/deletado.html')

@app.route("/adic_carrinho")
def adic_carrinho():
    argumentos = request.args.to_dict()
                                                
    produto = argumentos['produto']
    quantidade = int(argumentos['quantidade'])
    preco = float(produtos.get(produto)[0])
    print(preco)
    #dicionário
    prod_carrinho[produto] = [preco, quantidade] 

    #dataframe
    carrinho.loc[produto] = [preco, quantidade]
    print(produtos)
    #Ajuste nas quantidades do dict produtos.
    produtos[produto] = [preco,produtos[produto][1]-quantidade]
    #Ajuste nas quantidades do df catalogo.
    catalogo.loc[produto,'quantidade'] = catalogo.loc[produto,'quantidade']-quantidade
    return redirect('/carr')

@app.route('/carr')
def carr():
    return render_template('carrinho.html', carrinho=carrinho.to_html())

@app.route('/remov_carrinho')
def remov_carrinho():
    argumentos = request.args.to_dict()
    
    produto = argumentos['produto']
    quantidade = int(argumentos['quantidade'])
    preco = float(produtos.get(produto)[0])

    #dicionário    
    prod_carrinho[produto] = [preco, quantidade] 

    #dataframe
    carrinho.loc[produto] = [preco, quantidade]
    print(produtos)
    #Ajuste nas quantidades do dict produtos.
    produtos[produto] = [preco,produtos[produto][1]+quantidade]
    #Ajuste nas quantidades do df catalogo.
    catalogo.loc[produto,'quantidade'] = catalogo.loc[produto,'quantidade']+quantidade

    return redirect('/carr')

@app.route('/final_vend')
def final_vend():
    argumentos = request.args.to_dict()
    print(argumentos)

    if 'sim' in argumentos.values():
        total = 0
        for p in prod_carrinho:
            preco = float(prod_carrinho.get(p)[0]) * int(prod_carrinho.get(p)[1])
            total += preco
            print(total)

        catalogo.to_csv('catalogo.csv')
        return redirect('static/vendido.html')
    
    else:
        prod_carrinho.clear()
        print(prod_carrinho)
        return redirect('web\index.html')

if __name__ == "__main__":
    app.run(debug=True)