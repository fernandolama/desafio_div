from logging.config import valid_ident
from flask import Flask
from flask import request, redirect
import pandas as pd

app = Flask(__name__)

produtos = {} #{produto: [valor, quantidade]}
precos = {}
quantidades = {}

df = pd.read_csv('catalogo.csv')
print(df)

@app.route("/cad")
def cad():
    argumentos = request.args.to_dict()
    
    produto = argumentos['produto'] #arroz
    preco = float(argumentos['preco']) #10
    quantidade = int(argumentos['quantidade']) #10
    
    #dicionário
    produtos[produto] = [preco, quantidade]
    #dataframe
    df.loc[produto] = [preco, quantidade]
    df.to_csv('catalogo.csv')
    df.to_html('catalogo.html')
    print(df)
    return redirect('static/cadastrado.html')

df = pd.read_csv('catalogo.csv')

@app.route("/cad2")
def cad2():
    df = pd.read_csv('catalogo.csv')
    argumentos = request.args.to_dict()
    
    produtos[argumentos['produto']] = argumentos['produto'] #arroz
    precos[argumentos['produto']] = float(argumentos['preco']) #10
    quantidades[argumentos['produto']] = int(argumentos['quantidade']) #10

    print(produtos, precos, quantidades)
    #return produtos
    df=pd.DataFrame({
        'produto' : produtos.values(),
        'preço' : precos.values(),
        'quantidade' : quantidades.values()
    })
    print(df)
    df.to_csv('catalogo.csv', index=False)
    df.to_html('catalogo.html')
    return redirect('static/cadastrado.html')

@app.route('/del')
def delet():
    df = pd.read_csv('catalogo.csv')
    argumentos = request.args.to_dict()

    prod_del = argumentos['prod_del']
    qtde_del = int(argumentos['qtde_del'])

    if qtde_del <= quantidades[prod_del] and qtde_del > 0:
        nova_qtde = quantidades[prod_del] - qtde_del
        quantidades.update({prod_del: nova_qtde})

    if quantidades[prod_del] == 0:
        produtos.pop(prod_del)
        precos.pop(prod_del)
    
    df=pd.DataFrame({
        'produto' : produtos.values(),
        'preço' : precos.values(),
        'quantidade' : quantidades.values()
    })

    df.to_csv('catalogo.csv')
    df.to_html('catalogo.html')
    print(df)
    return redirect('static/deletado.html')
    
@app.route('/vend')
def vend():
    df = pd.read_csv('catalogo.csv')
    
    argumentos = request.args.to_dict()


if __name__ == "__main__":
    app.run(debug=True)