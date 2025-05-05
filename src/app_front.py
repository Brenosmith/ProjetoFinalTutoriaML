# Arquivo: app_front.py

import streamlit as st
import requests
from Projeto.Enums import *
from Projeto.Dictionaries import *

# URL da API
BASE_API_URL = "http://127.0.0.1:8000/prever/"

# Título do aplicativo
st.title("Previsão com Modelo de Machine Learning")

# Seleção de modelo no corpo principal
st.header("Seleção de Modelo")
modelo_selecionado = st.selectbox(
    "Escolha o modelo de Machine Learning",
    ["Decision Tree", "LightGBM"]
)

# Ajustando a URL da API com base no modelo selecionado
if modelo_selecionado == "Decision Tree":
    API_URL = f"{BASE_API_URL}arvore_decisao"
elif modelo_selecionado == "LightGBM":
    API_URL = f"{BASE_API_URL}lgbm"

# Formulário para entrada de dados
st.header("Insira os dados do modelo")

# Campos binários
NAO_SABE_GRAU_ESTUDO_PAI = st.checkbox("Não sabe o grau de estudo do pai", value=False)
NAO_SABE_GRAU_ESTUDO_MAE = st.checkbox("Não sabe o grau de estudo da mãe", value=False)
PRESENCA_ASPIRADOR = st.checkbox("Presença de aspirador", value=False)
PRESENCA_DVD = st.checkbox("Presença de DVD", value=False)
PRESENCA_TV_ASSINATURA = st.checkbox("Presença de TV por assinatura", value=False)
PRESENCA_TEL_FIXO = st.checkbox("Presença de telefone fixo", value=False)
PRESENCA_INTERNET = st.checkbox("Presença de internet", value=False)

# Campos categóricos
COR_RACA = st.selectbox("Cor/Raça", [e.value for e in CorRacaEnum])
CO_MUNICIPIO_ESC = st.selectbox("Código do município da escola", [e.value for e in MunicipioEscolaEnum])
CO_UF_ESC = st.selectbox("UF da escola", [e.value for e in UfEnum])
DEPENDENCIA_ADM_ESC = st.selectbox("Dependência administrativa da escola", [e.value for e in DependenciaAdmEscolaEnum])
ENSINO = st.selectbox("Ensino", [e.value for e in EnsinoEnum])
ESCOLA = st.selectbox("Escola", [e.value for e in EscolaEnum])
ESTADO_CIVIL = st.selectbox("Estado civil", [e.value for e in EstadoCivilEnum])
FAIXA_ETARIA = st.selectbox("Faixa etária", [e.value for e in FaixaEtariaEnum])
LINGUA = st.selectbox("Língua estrangeira", [e.value for e in LinguaEstrangeiraEnum])
LOCALIZACAO_ESC = st.selectbox("Localização da escola", [e.value for e in LocalizacaoEscolaEnum])
NACIONALIDADE = st.selectbox("Nacionalidade", [e.value for e in NacionalidadeEnum])
OCUPACAO_PAI = st.selectbox("Ocupação do pai", [e.value for e in OcupacaoEnum])
OCUPACAO_MAE = st.selectbox("Ocupação da mãe", [e.value for e in OcupacaoEnum])
SEXO = st.selectbox("Sexo", [e.value for e in SexoEnum])
SIT_FUNC_ESC = st.selectbox("Situação funcional da escola", [e.value for e in SituacaoFuncionalEscolaEnum])
GRAU_ESTUDO_PAI = st.selectbox("Grau de estudo do pai", [e.value for e in GrauEstudoEnum])
GRAU_ESTUDO_MAE = st.selectbox("Grau de estudo da mãe", [e.value for e in GrauEstudoEnum])

# Campos numéricos
QTD_RESIDENTES = st.number_input("Quantidade de residentes", value=3, step=1)
RENDA_MENSAL_FAMILIA = st.number_input("Renda mensal da família", value=4, step=1)
FREQ_EMPREGADO = st.number_input("Frequência de empregado", value=0, step=1)
QTD_BANHEIRO = st.number_input("Quantidade de banheiros", value=2, step=1)
QTD_QUARTO = st.number_input("Quantidade de quartos", value=2, step=1)
QTD_CARRO = st.number_input("Quantidade de carros", value=2, step=1)
QTD_MOTO = st.number_input("Quantidade de motos", value=0, step=1)
QTD_GELADEIRA = st.number_input("Quantidade de geladeiras", value=1, step=1)
QTD_FREEZER = st.number_input("Quantidade de freezers", value=1, step=1)
QTD_MAQ_LAVAR_ROUPA = st.number_input("Quantidade de máquinas de lavar roupa", value=1, step=1)
QTD_MAQ_SECAR = st.number_input("Quantidade de máquinas de secar", value=0, step=1)
QTD_MICROONDAS = st.number_input("Quantidade de micro-ondas", value=1, step=1)
QTD_MAQ_LAVAR_LOUCA = st.number_input("Quantidade de máquinas de lavar louça", value=0, step=1)
QTD_TELEVISOR = st.number_input("Quantidade de televisores", value=3, step=1)
QTD_CELULAR = st.number_input("Quantidade de celulares", value=4, step=1)
QTD_COMPUTADOR = st.number_input("Quantidade de computadores", value=3, step=1)

# Botão para enviar os dados
if st.button("Calcular Previsão"):
    # Montando o payload para a API
    payload = {
        # arrumar ordem de acordo com modelo
        "NAO_SABE_GRAU_ESTUDO_PAI": NAO_SABE_GRAU_ESTUDO_PAI,
        "NAO_SABE_GRAU_ESTUDO_MAE": NAO_SABE_GRAU_ESTUDO_MAE,
        "PRESENCA_ASPIRADOR": PRESENCA_ASPIRADOR,
        "PRESENCA_DVD": PRESENCA_DVD,
        "PRESENCA_TV_ASSINATURA": PRESENCA_TV_ASSINATURA,
        "PRESENCA_TEL_FIXO": PRESENCA_TEL_FIXO,
        "PRESENCA_INTERNET": PRESENCA_INTERNET,
        "COR_RACA": list(CorRacaEnum).index(CorRacaEnum(COR_RACA)),
        "CO_MUNICIPIO_ESC": dict_municipio_escola.get(MunicipioEscolaEnum(CO_MUNICIPIO_ESC).name),
        "CO_UF_ESC": dict_uf.get(UfEnum(CO_UF_ESC).name),
        "DEPENDENCIA_ADM_ESC": dict_dependencia_adm_escola.get(DependenciaAdmEscolaEnum(DEPENDENCIA_ADM_ESC).name),
        "ENSINO": dict_ensino.get(EnsinoEnum(ENSINO).name),
        "ESCOLA": dict_escola.get(EscolaEnum(ESCOLA).name),
        "ESTADO_CIVIL": list(EstadoCivilEnum).index(EstadoCivilEnum(ESTADO_CIVIL)),
        "FAIXA_ETARIA": dict_faixa_etaria.get(FaixaEtariaEnum(FAIXA_ETARIA).name),
        "LINGUA": list(LinguaEstrangeiraEnum).index(LinguaEstrangeiraEnum(LINGUA)),
        "LOCALIZACAO_ESC": dict_localizacao_escola.get(LocalizacaoEscolaEnum(LOCALIZACAO_ESC).name),
        "NACIONALIDADE": dict_nacionalidade.get(NacionalidadeEnum(NACIONALIDADE).name),
        "OCUPACAO_PAI": dict_ocupacao.get(OcupacaoEnum(OCUPACAO_PAI).name),
        "OCUPACAO_MAE": dict_ocupacao.get(OcupacaoEnum(OCUPACAO_MAE).name),
        "SEXO": SexoEnum(SEXO).value,
        "SIT_FUNC_ESC": dict_situacao_funcional_escola.get(SituacaoFuncionalEscolaEnum(SIT_FUNC_ESC).name),
        "GRAU_ESTUDO_PAI": dict_grau_estudo.get(GrauEstudoEnum(GRAU_ESTUDO_PAI).name),
        "GRAU_ESTUDO_MAE": dict_grau_estudo.get(GrauEstudoEnum(GRAU_ESTUDO_MAE).name),
        "QTD_RESIDENTES": QTD_RESIDENTES,
        "RENDA_MENSAL_FAMILIA": RENDA_MENSAL_FAMILIA,
        "FREQ_EMPREGADO": FREQ_EMPREGADO,
        "QTD_BANHEIRO": QTD_BANHEIRO,
        "QTD_QUARTO": QTD_QUARTO,
        "QTD_CARRO": QTD_CARRO,
        "QTD_MOTO": QTD_MOTO,
        "QTD_GELADEIRA": QTD_GELADEIRA,
        "QTD_FREEZER": QTD_FREEZER,
        "QTD_MAQ_LAVAR_ROUPA": QTD_MAQ_LAVAR_ROUPA,
        "QTD_MAQ_SECAR": QTD_MAQ_SECAR,
        "QTD_MICROONDAS": QTD_MICROONDAS,
        "QTD_MAQ_LAVAR_LOUCA": QTD_MAQ_LAVAR_LOUCA,
        "QTD_TELEVISOR": QTD_TELEVISOR,
        "QTD_CELULAR": QTD_CELULAR,
        "QTD_COMPUTADOR": QTD_COMPUTADOR,
    }

    # Fazendo a requisição para a API
    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()  # Levanta exceções para erros HTTP
        resultado = response.json()
        st.success(f"Resultado da previsão: {resultado['mensagem']}")

    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao chamar a API: {e}")
