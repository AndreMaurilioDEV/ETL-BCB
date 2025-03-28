from src.extractTransform import trimestreFunc
from src.load import salvarCsv
import pandas as pd

dadosBcb = trimestreFunc('20231')
salvarCsv(dadosBcb, 'src/datasets/meiosPagamentosTri.csv', ';', '.')



