import pandas as pd
import sqlite3
from sqlalchemy import create_engine


def salvarCsv(df: pd.DataFrame, nome_arquivo: str, separador: str, dec: str):
    """
    Salva os dados em um arquivo CSV.

    Esta função recebe os dados processados e os salva em um arquivo CSV
    no caminho especificado.

    Parâmetros:
    dados (list ou DataFrame): Os dados a serem salvos no arquivo CSV.
                               Normalmente, é o resultado de uma transformação ou extração.

    caminho_arquivo (str): O caminho onde o arquivo CSV será salvo, incluindo o nome do arquivo e a extensão.

    delimitador (str): O delimitador a ser utilizado no arquivo CSV.
                       O valor padrão para arquivos CSV é a vírgula (`,`), mas outros delimitadores como ponto e vírgula (`;`) também podem ser usados.

    Retorna:
    None: A função não retorna nenhum valor. Ela apenas salva o arquivo no sistema de arquivos local.

    """
    df.to_csv(nome_arquivo, sep=separador, decimal=dec)
    return


def salvarSqlite(df: pd.DataFrame, nome_banco: str, nome_tabela: str):

    conn = sqlite3.connect(nome_banco)

    df.to_sql(nome_tabela, conn, if_exists="replace", index=False)

    conn.close()


def salvarMySQL(
    df: pd.DataFrame, usuario: str, senha: str, host: str, banco: str, nome_tabela: str
):

    engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}/{banco}")

    df.to_sql(nome_tabela, con=engine, if_exists="replace", index=False)
