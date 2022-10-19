from flask import Flask
from flask import request, redirect, render_template
import pandas as pd

app = Flask(__name__)

produtos = {} #{produto: [valor, quantidade]}

catalogo = pd.read_csv('catalogo.csv', index_col='produto')
print(catalogo)

carrinho = pd.DataFrame(data={
    'produto': [],
    'preco': [],
    'quantidade': []
}).set_index('produto')

@app.route("/")
def index():
    return "olá"            

@app.route("/rel_qtde_prod")
def rel_qtde_prod():
    
    return redirect

if __name__ == "__main__":
    app.run(debug=True)