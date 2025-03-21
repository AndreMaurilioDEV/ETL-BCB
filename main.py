import requests
import pandas as pd

def trimestreFunc(trimestre):
        url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre='{trimestre}'&$format=json"
        req = requests.get(url) 
        req.raise_for_status()
        dados = req.json()
        df = pd.json_normalize(dados['value'])
        print(df)  
        return df

trimestreFunc('20231')
