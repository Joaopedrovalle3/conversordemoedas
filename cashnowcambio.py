from flask import Flask, render_template, send_from_directory, request
import requests

app = Flask(__name__)

#criação da primeira página do site
@app.route('/')
def home():
    nome = valor_convertido
    return render_template('cashnow.html', valor_convertido=valor_convertido)

#imagem do html através do Flask
@app.route('/static/<path:G03removebgpreview>')
def servir_imagem(G03removebgpreview):
    return send_from_directory('static', G03removebgpreview.png)


#código do conversor de moedas
@app.route('/')
def obter_taxas():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data['rates']

@app.route('/')
def converter_moedas(valor, moeda_origem, moeda_destino, taxas):

    if moeda_origem in taxas and moeda_destino in taxas:
        taxa_origem = taxas[moeda_origem]
        taxa_destino = taxas[moeda_destino]
        valor_em_usd = valor / taxa_origem
        valor_convertido = valor_em_usd * taxa_destino
        return valor_convertido

    else:
        return None


taxa_de_cambio = obter_taxas()
valor = float(input('Digite o valor a ser convertido: '))
moeda_origem = input('Escolha a moeda de origem: ').upper()
moeda_destino = input('Escolha a moeda de destino: ').upper()

valor_convertido = converter_moedas(valor, moeda_origem, moeda_destino, taxa_de_cambio)

if valor_convertido is not None:
    print(f'\n{valor:.2f} {moeda_origem} é equivalente a {valor_convertido:.2f} {moeda_destino}')

else:
    print('Moeda inválida')

if __name__=="__main__":
    app.run(debug=True)
