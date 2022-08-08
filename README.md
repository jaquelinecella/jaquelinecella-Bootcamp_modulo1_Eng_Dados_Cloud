# In construction
## Introduction
 
 The goal of this project is to automate a cloud infrastructure and enable a continuous integration workflow that makes it possible to work in groups with security and agility.
 
## Description

1) First Part: In this part of the project I've created the files with yaml and Terrafom codes to configurate a worflow with Git Actions to up an AWS infrastructure. This infrastructure has a bucket S3 to storage, a Lambda Function that up a cluster EMR to execute a Job Spark to read a table(csv format)from bucket(raw-data) and write this table in Delta Format at the same bucket, but in staging-zone. Ath the same time, I've changed some registrations in staging-zone table(delta format).To conclude, I opened a Jupyter notebook in cluster EMR to verify if the changes were written correctly and I've deleted the infrastructure with Terraform, after the confirmation that everything was correct.
 
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

## Results
type here

## Architecture

add image here
 
 
## Author

add my credentials

