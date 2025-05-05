# Arquivo: Projeto/Services.py

import os
import joblib
import pandas as pd
from Projeto.Functions import *

class PreverNota:

    @staticmethod
    def __carregar_modelo__ (__nome_modelo__: str) -> object:
        """
        Carrega o modelo treinado a partir de um arquivo pickle.
        :param __nome_modelo__: Nome do modelo a ser carregado.
        :return: O modelo carregado.
        """
        current_path = os.path.abspath(__file__)
        models_path = os.path.dirname(current_path) + "/Modelos/"

        # Carregar modelo treinado pickle
        with open(f'{models_path}{__nome_modelo__}.pkl', 'rb') as file:
            modelo = joblib.load(file)

        return modelo

    def __init__(self, dados: dict) -> None:
        """
        Inicializa a classe PreverNota com os dados de entrada.
        :param dados: Dados de entrada no formato JSON.
        """
        # Inicializa a classe com os dados de entrada, convert json para dataframe
        self.dados = adjust_colums_types(pd.DataFrame([names_front_to_model(dados)]))
              
        # carregar os modelos treinados
        self.modelos = {
            "arvore_decisao": self.__carregar_modelo__("modelo_arvore_decisao_base"),
            "lgbm": self.__carregar_modelo__("modelo_lgbm_bayes")
        }

    def arvore_decisao(self) -> float:
        """
        Prever a nota usando o modelo de árvore de decisão.
        :return: A nota prevista pelo modelo.
        """
        # Prever a nota usando o modelo de árvore de decisão
        modelo = self.modelos["arvore_decisao"]
        nota = modelo.predict(apply_label_encoder(self.dados))
        return nota[0]

    def lgbm(self) -> float:
        """
        Prever a nota usando o modelo LGBM.
        :return: A nota prevista pelo modelo.
        """
        # Prever a nota usando o modelo LGBM
        modelo = self.modelos["lgbm"]
        nota = modelo.predict(self.dados)
        return nota[0]
