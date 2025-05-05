from fastapi import FastAPI
from Projeto.Interfaces import IModeloEntrada
from Projeto.Services import PreverNota

# Cria a aplicação FastAPI
app = FastAPI()

# Inicializa o serviço de previsão de notas

# Rota de teste
@app.get("/")
def read_root():
    """
    Rota raiz da API.
    Retorna uma mensagem de boas-vindas.
    """
    return {"mensagem": "API para previsão de notas do ENEM"}

@app.post("/prever/{modelo}")
def prever_dados(dados: IModeloEntrada, modelo: str):
    """
    Rota para prever a nota do ENEM com base nos dados recebidos.
    Aceita dois parâmetros:
    - dados: dados de entrada no formato JSON.
    - modelo: o modelo a ser utilizado para a previsão (arvore_decisao ou lgbm).
    """
    try:
        # Inicializa o serviço de previsão com os dados recebidos
        servico_modelo = PreverNota(dados.model_dump())

        # Escolhe o modelo com base no parâmetro da URL
        if modelo == "arvore_decisao":
            nota = servico_modelo.arvore_decisao()
        elif modelo == "lgbm":
            nota = servico_modelo.lgbm()
        else:
            return {"erro": f"Modelo '{modelo}' não é suportado."}

        return {"mensagem": nota}
    
    except Exception as e:
        return {"erro": str(e)}

@app.post("/revisar/")
def dados_enviados(dados: IModeloEntrada):
    """
    Rota para receber dados enviados pelo front-end.
    Aceita um parâmetro:
    - dados: dados de entrada no formato JSON.
    """
    # Recuperar os dados enviados
    dados_enviados = dados.model_dump()
    return {"mensagem": "Dados recebidos com sucesso!", "dados": dados_enviados}
