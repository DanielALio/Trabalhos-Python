import json
import urllib.request
import urllib.error

cep = input("CEP: ")
endereco = f"https://viacep.com.br/ws/{cep}/json/"

try:
    # O Python faz o mesmo pedido que o navegador fez na Parte 2
    resposta = urllib.request.urlopen(endereco)
    print("status:", resposta.status)
    print("tipo:", resposta.headers["Content-Type"])

    # O texto que voltou vira um dicionário do Python
    dados = json.loads(resposta.read())

    if "erro" in dados:
        print("CEP não encontrado")
    else:
        print(dados["logradouro"])
        print(dados["bairro"], "--", dados["localidade"])
except urllib.error.HTTPError as erro:
    print("o servidor recusou o pedido. status:", erro.code)
