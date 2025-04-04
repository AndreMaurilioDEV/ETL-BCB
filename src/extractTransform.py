import requests
import pandas as pd


def trimestreFunc(trimestre: str) -> pd.DataFrame:
    """
    Função para extrair os dados da API do Banco Central.

    Parâmetros:
    data - string - AAAAT (Exemplo: 20191)

    Saida:
    Dateframe  - Estrutura de dados do pandas
    """
    url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre='{trimestre}'&$format=json"
    req = requests.get(url)
    print("Status Code:", req.status_code)
    dados = req.json()
    df = pd.json_normalize(dados["value"])
    df["datatrimestre"] = pd.to_datetime(df["datatrimestre"])
    return df
