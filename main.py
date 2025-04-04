from src.extractTransform import trimestreFunc
from src.load import salvarCsv
import pandas as pd
from src.load import salvarSqlite
from src.load import salvarMySQL

dadosBcb = trimestreFunc("20231")

# salvarCsv(dadosBcb, 'ETL-BCB/src/datasets/meiosPagamentosTri.csv', ';', '.')

# salvarSqlite(dadosBcb, "src/datasets/etlbcb.db", "meios_pagamentos_tri")

salvarMySQL(dadosBcb, "root", "teste", "localhost", "etlbcb", "meios_pagamentos_tri")
