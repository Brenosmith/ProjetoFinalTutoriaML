# Arquivo Functions.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def names_front_to_model(dados: dict) -> dict:
    """
    Converte os nomes das chaves do dicionário de entrada para os nomes esperados pelo modelo.
    Nomes utilizados no front-end são convertidos para os nomes utilizados no modelo de previsão.
    - dados: dicionário com os dados de entrada.
    - Retorna um dicionário com os nomes das chaves convertidas.
    """    
    mapeamento = {
        "NAO_SABE_GRAU_ESTUDO_PAI": "BIN_Q001_DUMMY_H",
        "NAO_SABE_GRAU_ESTUDO_MAE": "BIN_Q002_DUMMY_H",
        "PRESENCA_ASPIRADOR": "BIN_Q018",
        "PRESENCA_DVD": "BIN_Q020",
        "PRESENCA_TV_ASSINATURA": "BIN_Q021",
        "PRESENCA_TEL_FIXO": "BIN_Q023",
        "PRESENCA_INTERNET": "BIN_Q025",
        "COR_RACA": "CAT_COR_RACA",
        "CO_MUNICIPIO_ESC": "CAT_CO_MUNICIPIO_ESC",
        "CO_UF_ESC": "CAT_CO_UF_ESC",
        "DEPENDENCIA_ADM_ESC": "CAT_DEPENDENCIA_ADM_ESC",
        "ENSINO": "CAT_ENSINO",
        "ESCOLA": "CAT_ESCOLA",
        "ESTADO_CIVIL": "CAT_ESTADO_CIVIL",
        "FAIXA_ETARIA": "CAT_FAIXA_ETARIA",
        "LINGUA": "CAT_LINGUA",
        "LOCALIZACAO_ESC": "CAT_LOCALIZACAO_ESC",
        "NACIONALIDADE": "CAT_NACIONALIDADE",
        "OCUPACAO_PAI": "CAT_Q003",
        "OCUPACAO_MAE": "CAT_Q004",
        "SEXO": "CAT_SEXO",
        "SIT_FUNC_ESC": "CAT_SIT_FUNC_ESC",
        "GRAU_ESTUDO_PAI": "NUM_Q001",
        "GRAU_ESTUDO_MAE": "NUM_Q002",
        "QTD_RESIDENTES": "NUM_Q005",
        "RENDA_MENSAL_FAMILIA": "NUM_Q006",
        "FREQ_EMPREGADO": "NUM_Q007",
        "QTD_BANHEIRO": "NUM_Q008",
        "QTD_QUARTO": "NUM_Q009",
        "QTD_CARRO": "NUM_Q010",
        "QTD_MOTO": "NUM_Q011",
        "QTD_GELADEIRA": "NUM_Q012",
        "QTD_FREEZER": "NUM_Q013",
        "QTD_MAQ_LAVAR_ROUPA": "NUM_Q014",
        "QTD_MAQ_SECAR": "NUM_Q015",
        "QTD_MICROONDAS": "NUM_Q016",
        "QTD_MAQ_LAVAR_LOUCA": "NUM_Q017",
        "QTD_TELEVISOR": "NUM_Q019",
        "QTD_CELULAR": "NUM_Q022",
        "QTD_COMPUTADOR": "NUM_Q024",
    }

    # Converte os nomes das chaves
    dados_convertidos = {mapeamento.get(k, k): v for k, v in dados.items()}
    return dados_convertidos

def adjust_colums_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ajusta os tipos de dados das colunas do DataFrame.
    Converte colunas booleanas, categóricas e numéricas para os tipos apropriados.
    - df: DataFrame a ser ajustado.
    - Retorna o DataFrame com os tipos de dados ajustados.
    """
    # Colunas booleanas
    bool_columns = [
        'BIN_Q001_DUMMY_H', 'BIN_Q002_DUMMY_H', 'BIN_Q018', 'BIN_Q020', 
        'BIN_Q021', 'BIN_Q023', 'BIN_Q025'
    ]
    
    # Colunas categóricas
    category_columns = [
        'CAT_COR_RACA', 'CAT_CO_MUNICIPIO_ESC', 'CAT_CO_UF_ESC', 
        'CAT_DEPENDENCIA_ADM_ESC', 'CAT_ENSINO', 'CAT_ESCOLA', 
        'CAT_ESTADO_CIVIL', 'CAT_FAIXA_ETARIA', 'CAT_LINGUA', 
        'CAT_LOCALIZACAO_ESC', 'CAT_NACIONALIDADE', 'CAT_Q003', 
        'CAT_Q004', 'CAT_SEXO', 'CAT_SIT_FUNC_ESC'
    ]
    
    # Colunas numéricas
    int_columns = [
        'NUM_Q001', 'NUM_Q002', 'NUM_Q005', 'NUM_Q006', 'NUM_Q007', 
        'NUM_Q008', 'NUM_Q009', 'NUM_Q010', 'NUM_Q011', 'NUM_Q012', 
        'NUM_Q013', 'NUM_Q014', 'NUM_Q015', 'NUM_Q016', 'NUM_Q017', 
        'NUM_Q019', 'NUM_Q022', 'NUM_Q024'
    ]
    
    # Função auxiliar para verificar e converter colunas
    def safe_convert(df, columns, dtype):
        existing_columns = [col for col in columns if col in df.columns]
        if existing_columns:
            try:
                df[existing_columns] = df[existing_columns].astype(dtype)
            except Exception as e:
                print(f"Erro ao converter colunas {existing_columns} para {dtype}: {e}")
        else:
            print(f"Nenhuma coluna encontrada para conversão para {dtype}: {columns}")
    
    # Converter os tipos de dados
    safe_convert(df, bool_columns, 'bool')
    safe_convert(df, category_columns, 'category')
    safe_convert(df, int_columns, 'int64')
    
    return df

def apply_label_encoder(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplicar o LabelEncoder para converter as colunas categóricas em numéricas. Utilizado para o modelo de árvore de decisão.
    - df: DataFrame a ser ajustado.
    - Retorna o DataFrame com as colunas categóricas convertidas.
    """
    label_encoder = LabelEncoder()
    categorical_columns = df.select_dtypes(include=['category']).columns

    for col in categorical_columns:
        df[col] = label_encoder.fit_transform(df[col])

    return df
