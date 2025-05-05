# Arquivo de teste para verificar a integração com a API
# TesteIntegrado.py

import requests
from Projeto.Enums import *
from Projeto.Dictionaries import *

# URL da API
url = "http://127.0.0.1:8000/prever/lgbm"

# Dados de exemplo para enviar no POST
dados_nome_front = {
    "NAO_SABE_GRAU_ESTUDO_PAI": False,
    "NAO_SABE_GRAU_ESTUDO_MAE": False,
    "PRESENCA_ASPIRADOR": False,
    "PRESENCA_DVD": False,
    "PRESENCA_TV_ASSINATURA": False,
    "PRESENCA_TEL_FIXO": False,
    "PRESENCA_INTERNET": True,
    "COR_RACA": 0,
    "CO_MUNICIPIO_ESC": 5200258,
    "CO_UF_ESC": 52,
    "DEPENDENCIA_ADM_ESC": 2,
    "ENSINO": 1,
    "ESCOLA": 2,
    "ESTADO_CIVIL": 1,
    "FAIXA_ETARIA": 2,
    "LINGUA": 1,
    "LOCALIZACAO_ESC": 1,
    "NACIONALIDADE": 1,
    "OCUPACAO_PAI": "C",
    "OCUPACAO_MAE": "B",
    "SEXO": "F",
    "SIT_FUNC_ESC": 1,
    "GRAU_ESTUDO_PAI": 2,
    "GRAU_ESTUDO_MAE": 1,
    "QTD_RESIDENTES": 3,
    "RENDA_MENSAL_FAMILIA": 2,
    "FREQ_EMPREGADO": 0,
    "QTD_BANHEIRO": 1,
    "QTD_QUARTO": 2,
    "QTD_CARRO": 1,
    "QTD_MOTO": 1,
    "QTD_GELADEIRA": 1,
    "QTD_FREEZER": 0,
    "QTD_MAQ_LAVAR_ROUPA": 1,
    "QTD_MAQ_SECAR": 0,
    "QTD_MICROONDAS": 0,
    "QTD_MAQ_LAVAR_LOUCA": 0,
    "QTD_TELEVISOR": 1,
    "QTD_CELULAR": 1,
    "QTD_COMPUTADOR": 0,
}

# Fazendo a requisição POST
response = requests.post(url, json=dados_nome_front)

# Exibindo a resposta da API
print("Status Code:", response.status_code)

if response.status_code == 200:
    print("Resposta:", response.json())
    print('')
else:
    print("Erro:", response.text)
