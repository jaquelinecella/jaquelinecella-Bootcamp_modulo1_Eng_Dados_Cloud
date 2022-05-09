#comentário para modificar o arquivo.py
from pyspark.sql.functions import mean, max, min, col, count
from pypark.sql import SparkSession

spark=(
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
)


# Ler dados do ENEM
enem = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", ";")
    .load("s3://datalake-jaque-igti-edc/raw-data/enem/"))

(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("year")
    .save("s3://datalake-jaque-igti-edc/staging/enem/")
)
