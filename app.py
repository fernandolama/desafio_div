from flask import Flask
from flask import request, redirect, render_template
import pandas as pd

app = Flask(__name__)

produtos = {} #{produto: [valor, quantidade]}
precos = {}
quantidades = {}

catalogo = pd.read_csv('catalogo.csv', index_col='produto')
print(catalogo)

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

if __name__ == "__main__":
    app.run(debug=True)