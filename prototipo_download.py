# prototipo_download.py
"""
Baixa o CSV do Google Drive e o devolve como pandas.DataFrame
para comprovar que o pipeline base funciona.
"""

from pathlib import Path
import gdown
import pandas as pd

# 1) ID do arquivo no Drive  (tudo depois de 'id=' ou entre as barras, depende do link)
FILE_ID = "1Oquyuq9hHifoOgKcMDT13Srzjs2CZBvo"

# 2) Google Drive URL de download direto
URL = f"https://drive.google.com/uc?export=download&id={FILE_ID}"

# 3) Pasta de saída (mesma pasta do script, subpasta "data")
DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)
CSV_PATH = DATA_DIR / "central_emendas_raw.csv"

def baixar_csv() -> Path:
    """
    Faz o download se o arquivo ainda não existir.
    Retorna o caminho completo do arquivo CSV.
    """
    if CSV_PATH.exists():
        print("✔ Arquivo já baixado, usando cache local.")
        return CSV_PATH

    print("▶ Baixando arquivo...")
    gdown.download(URL, str(CSV_PATH), quiet=False)
    print("✔ Download concluído:", CSV_PATH)
    return CSV_PATH

def carregar_dataframe() -> pd.DataFrame:
    """
    Garante que o CSV esteja baixado e devolve um DataFrame.
    """
    csv_file = baixar_csv()
    df = pd.read_csv(csv_file)
    print("✔ DataFrame carregado com", df.shape[0], "linhas e", df.shape[1], "colunas")
    return df

# Execução direta: python prototipo_download.py
if __name__ == "__main__":
    df = carregar_dataframe()
    # mostra as 5 primeiras linhas só para conferência
    print(df.head())
