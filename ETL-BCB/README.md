# ETL-BCB

## Funções Principais

O projeto **ETL-BCB** contém duas funções principais que são usadas para extrair, transformar e carregar os dados:

### 1. `trimestreFunc`

A função `trimestreFunc` é responsável por extrair e transformar dados com base em um parâmetro de entrada, geralmente representando um trimestre específico. Ela realiza as operações de extração e transformação, preparando os dados para o próximo passo no processo ETL.

- **Localização:** `src/extractTransform.py`
- **Parâmetro de entrada:** Um código representando o trimestre (exemplo: `'20231'`).
- **Objetivo:** Extrair e transformar os dados para análise posterior.

### 2. `salvarCsv`

A função `salvarCsv` é usada para salvar os dados processados em um arquivo CSV. Após a transformação dos dados, ela permite que você salve os resultados em um formato fácil de manipular e compartilhar.

- **Localização:** `src/load.py`
- **Parâmetros de entrada:**
  - **dados:** Dados a serem salvos (geralmente resultantes da função `trimestreFunc`).
  - **caminho_arquivo:** Caminho onde o arquivo CSV será salvo (exemplo: `'src/datasets/meiosPagamentosTri.csv'`).
  - **delimitador:** O delimitador que será utilizado no CSV (exemplo: `','`).
- **Objetivo:** Salvar os dados transformados em um arquivo CSV para posterior uso ou análise.

### Exemplo de uso

No arquivo `main.py`, essas funções são usadas da seguinte maneira:

```python
from src.extractTransform import trimestreFunc
from src.load import salvarCsv

# Extrai e transforma os dados para o trimestre '20231'
dados_transformados = trimestreFunc('20231')

# Salva os dados transformados em um arquivo CSV
salvarCsv(dados_transformados, 'src/datasets/meiosPagamentosTri.csv', ',')
