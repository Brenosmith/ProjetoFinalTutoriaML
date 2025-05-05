Brenosmith: Gostaria de criar um arquivo reafme para o github que desse um overview do meu projeto.

Dividido em quatro partes:
1. Como executar o projeto
2. O que é cada arquivo e subpastas de forma simplificada
3. O que o projeto faz, qual o objetivo
4. Quais são os resultados do projeto

Estruture esse arquivo baseado no arquivo atual, no projeto e na estrutura do mesmo.

Workspace: Collecting workspace informationFiltering to most relevant information```markdown
# Previsão de Notas do ENEM 2023

Este projeto utiliza técnicas de Machine Learning para prever as notas do ENEM 2023 com base em dados socioeconômicos e escolares. Ele inclui um backend em FastAPI, um frontend em Streamlit e modelos de aprendizado de máquina treinados e otimizados.

---

## 1. Como executar o projeto

### Backend (API)
Para iniciar a API em modo de desenvolvimento (debug):
```bash
uvicorn app_api:app --reload --log-level debug
```

Para iniciar a API em modo de produção:
```bash
uvicorn app_api:app
```

### Frontend
Para iniciar o frontend em modo de desenvolvimento (debug):
```bash
streamlit run app_front.py --logger.level=debug
```

Para iniciar o frontend em modo de produção:
```bash
streamlit run app_front.py
```

### MLFlow
Para iniciar o servidor MLFlow:
```bash
mlflow server --host 127.0.0.1 --port 9080
```

Acesse o MLFlow pela URI: [http://127.0.0.1:9080](http://127.0.0.1:9080)

---

## 2. Estrutura do projeto

### Arquivos principais
- **`app_api.py`**: Backend da aplicação, implementado com FastAPI. Contém rotas para previsão de notas.
- **`app_front.py`**: Frontend da aplicação, implementado com Streamlit. Permite interação com os modelos de Machine Learning.
- **`TesteIntegrado.py`**: Script para testar a integração entre o backend e os modelos de previsão.
- **`requirements.txt`**: Lista de dependências do projeto.

### Notebooks
- **`1_Tratamento_Dados_Enem_23.ipynb`**: Processamento inicial dos dados do ENEM.
- **`2_Analise_Dados_Enem_23.ipynb`**: Análise exploratória dos dados.
- **`3_Modelagem_Enem_23_Arvore.ipynb`**: Treinamento e otimização do modelo de árvore de decisão.
- **`3_Modelagem_Enem_23_LGBM.ipynb`**: Treinamento e otimização do modelo LightGBM.
- **`4_Analise_Resultados_Enem_23.ipynb`**: Análise dos resultados obtidos pelos modelos.

### Subpastas
- **`Bases/`**: Contém os dados utilizados no projeto, como arquivos `.pkl` e o dicionário de microdados.
- **`Projeto/`**: Contém os módulos principais, como `Services.py` (implementação dos modelos) e utilitários.
- **`mlartifacts/` e `mlruns/`**: Diretórios gerados pelo MLFlow para rastreamento de experimentos.
- **`Resultados/`**: Resultados gerados pelos modelos e análises.

---

## 3. Objetivo do projeto

O objetivo deste projeto é prever as notas do ENEM 2023 com base em dados socioeconômicos e escolares dos participantes. Ele utiliza dois modelos principais:
- **Árvore de Decisão**: Um modelo interpretável e eficiente para dados tabulares.
- **LightGBM**: Um modelo baseado em gradiente boosting, otimizado para alta performance.

O projeto também inclui uma interface interativa para facilitar o uso dos modelos e a análise dos resultados.

---

## 4. Resultados do projeto

Os resultados incluem:
- **Modelos treinados**: Dois modelos otimizados (Árvore de Decisão e LightGBM) salvos em arquivos `.pkl`.
- **Análise de desempenho**: Comparação entre os resultados reais e previstos, com métricas como RMSE e R².
- **Interface interativa**: Um frontend que permite ao usuário inserir dados e obter previsões em tempo real.
- **Rastreamento de experimentos**: Utilização do MLFlow para monitorar e comparar diferentes execuções de modelos.

Os resultados mostram que o modelo LightGBM apresenta melhor desempenho em termos de precisão, enquanto a Árvore de Decisão é mais interpretável.

--- 

Este projeto é uma solução para análise e previsão de notas do ENEM, combinando ciência de dados, aprendizado de máquina e desenvolvimento de software.