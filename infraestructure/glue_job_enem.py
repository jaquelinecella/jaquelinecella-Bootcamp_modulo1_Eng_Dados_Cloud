import sys
from pyspark.context import SparkContext
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job

##@params: ['JOB_NAME']
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

#A partir daqui mesmo código do EMR
#Ler dados do ENEM 2020

enem = (
    spark
    .read
    .format("csv")
    .option("InferSchema", True)
    .option("delimiter", ";")
    .load("s3://datalake-jaque-igti-edc/raw-data/enem/")
)

#Escrever no datalake em parquet

(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("year")
    .save("s3://datalake-jaque-igti-edc/staging/enem-glue/")
)
