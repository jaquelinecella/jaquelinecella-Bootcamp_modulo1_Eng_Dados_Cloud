# In construction
## Introduction
 
 The goal of this project is to automate a cloud infrastructure and enable a continuous integration workflow that makes it possible to work in groups with security and agility.
 
## Description

1) First Part: In this part of the project I created the files with yaml and Terrafom codes to configurate a worflow with Git Actions to up an AWS infrastructure. This infrastructure has a bucket S3 to storage, a Lambda Function that up a cluster EMR to execute a Job Spark to read a table(csv format)from bucket(raw-data) and write this table in Delta Format at the same bucket, but in staging-zone. Ath the same time, I've changed some registrations in staging-zone table(delta format). To conclude, I opened a Jupyter notebook in cluster EMR to verify if the changes were written correctly and I deleted the infrastructure with Terraform, after the confirmation that everything was correct.
2) Second Part: In this part of the project I used a fake data simulator to conect with AWS Kinesis and storage this streaming data in S3. I've used the same structure that I had used in the First Part, but I opted to created another bucket to storage the streaming data. To Kinesis I created a file called "kinesis.tf" to create resources, cloudwatch options and firehose configurations. The firehose is a delivery streaming, but it's more similar with a mini-batch delivery that a real time. I inserted the buffer condition to 5mb or 60 seconds.These data was simulated with fake_web_events library that were writing in Python, after that these data were sent to bucket in json format, then the Glue Crawler understand the format and I could use SQL in Athena to do some queries.

## Tools Used 

* Terraform;
* Git Actions;
* Spark;
* Python;
* SQL;
* AWS S3;
* AWS Lambda;
* AWS EMR;
* AWS EC2;
* AWS Crawler;
* AWS Athena;
* AWS Kinesis;
* AWS CloudWatch.

## Instalation

In terminal you need type:
* First Part:
  1) You nedd to clone my repository



* Second Part:
  1) I am considering that you have my repository updated. If you don't have you need updated to create the resources in AWS;
  2) Type "pyhton simulations_to_kinesys.py" in terminal to create fakes data;
  3) Refresh the S3, click in "run Crawler" and after, refresh to updated, refresh Athena and now you can use the SQL to do some queries;
  4) Manually delete the data in the firehose(firehose/folder) bucket because it was not created by Terraform;
  5) Remember that you need to create a file with the name "lambda_function_payload.zip" to do a destroy command; 
  6) Access the "infrastructure" folder with the command "cd infrastructure";
  7) Type "terraform destroy" and wait some minutes to destroy all the infrastructure.  

## Results

type here

Obs: This Readme was created after I've finished the tests and excluded the infrastructure, because of this the workflow is not working now.

## Architecture

add image here
 
 
## Autor

Jaqueline Cella

* Linkedin- @jaqueline-cella
* Github- @jaquelinecella

