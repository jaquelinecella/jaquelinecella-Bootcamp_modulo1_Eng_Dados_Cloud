import boto3
import pandas as pd

# Criar um cliente para interagir com o AWS S3
s3_client = boto3.client('s3')

s3_client.download_file("datalake-jaque-igti-edc",
                        "data/Controle Saldo.xlsx",
                        "data/Controle Saldo.xlsx")

df = pd.read_xlsx("Controle Saldo.xlsx")
print(df)

s3_client.upload_file("data/QUANTIDADE_PASSAPORTES.csv",
                    "datalake-jaque-igti-edc",
                    "data/QUANTIDADE_PASSAPORTES.csv")