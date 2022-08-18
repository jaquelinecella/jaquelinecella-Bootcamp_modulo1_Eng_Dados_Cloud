
## Introduction
 
  The objective of this project is to automate a cloud infrastructure and enable a continuous integration(CI) an continuous delivery(CD) that allows it to be possible to work in groups with security and agility.
  
  **This readme was created after I've finished the tests and I've deleted the infrastructure, so the workflow will have a lot of test errors. Please disregard these errors**.
 
## Description

1) First Part: In this part of the project I've created the files with yaml and Terrafom codes to configurate a worflow with Git Actions to up an AWS infrastructure. This infrastructure has a bucket S3 to storage, a Lambda Function that up a cluster EMR to execute a Job Spark to read a table(csv format)from bucket(raw-data) and write this table in Delta Format at the same bucket, but in staging-zone. Ath the same time, I've changed some registrations in staging-zone table(delta format). To conclude, I've opened a Jupyter notebook in cluster EMR to verify if the changes were written correctly and I've deleted the infrastructure with Terraform, after the confirmation that everything was correct.
2) Second Part: In this part of the project I've used a fake data simulator to conect with AWS Kinesis and storage this streaming data in S3. I've used the same structure that I had used in the First Part, but I've opted to create another bucket to storage the streaming data. To Kinesis I've created a file called "kinesis.tf" to create resources, cloudwatch options and firehose configurations. The firehose is a delivery streaming, but it's more similar with a mini-batch delivery that a real time. I've inserted the buffer condition to 5mb or 60 seconds.This data was simulated with fake_web_events library that was written in Python, after that this data was sent to bucket in json format, then the Glue Crawler understand the format and I could use SQL with Athena to do some queries.

## Used Tools 

* Terraform;
* Git Actions;
* Pyspark;
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

## How to Use

To use this structure you need to follow the steps below:
* First Part:
  1) Download Visual Studio Code(VSC) and after, AWS Cli, Terraform, Python, Git and anything else if the program asks;
  2) You can use another code editor instead of VSC;
  2) You need to clone this repository and open a new repository in your Github;
  3) Rename the resources that are with my personal name. For exemplo: the bucket;
  4) Manually create the bucket that is in the "provider.tf" file. This is the only bucket that needs to be created manually;
  5) Manually create a Key Pair in EC2 and change it in file "lambda_function";
  6) Manually copy the number of "Subnet ID" in EMR;
  7) Go to Lambda Function, click in "test", choose a name, can be the default, save and click in test. This step is just to test de "lambda_function.py". At this moment the cluster EMR is starting;
  7) Go to Settings/Secrets on Github to configure your AWS secret keys;
  8) Create a "dev" branch to work safely;
  9) Go to Github and do the "pull request" to start the "Test on PR" workflow, and after do the "merge" the "Deploy" will start;
  10) Refresh S3, Lambda, IAM,  to see if the resources were created. To wait until the EMR finishes creating the cluster;
  11) In EMR, open a JupyterLab or Jupyter, choose PySpark. To use Pyspark to verify if the modifications of the files "delta_spark_upsert" was updated correctly and to see the diference between the versions;
  12) Now "stop" the notebook, "terminate" the cluster and delete the files in bucket that were generate by Notebook operations, for exemplo, because this resources were not created by Terraform;
  13) Remember that you need to create a file with the name "lambda_function_payload.zip" to do a "destroy" command; 
  14) Access the "infrastructure" folder with the command "cd infrastructure";
  15) Type "terraform destroy" and wait some minutes to destroy all the infrastructure.  



* Second Part:
  1) I am considering that you have my repository updated. If you don't have you need updated to create the resources in AWS and in Github.
  2) Click in "Delivery Streams" in Kinesis, refresh S3, Athena and Glue Crawler to see the resources that were created;
  3) Type "pyhton simulations_to_kinesys.py" in terminal to create fakes data. You can dowloand the fake-web-events library with pip package;
  4) Refresh the S3, click in "run Crawler" and after refresh. Refresh Athena and now you can use the SQL to do some queries;
  5) Manually delete the data in the firehose(firehose/folder) bucket because it was not created by Terraform;
  6) Remember that you need to create a file with the name "lambda_function_payload.zip" to do a destroy command; 
  7) Access the "infrastructure" folder with the command "cd infrastructure";
  8) Type "terraform destroy" and wait some minutes to destroy all the infrastructure.  

## Results

Automation of a cloud infrastructure, increased speed and security of processes, and writing of files in Delta Lake format that allow for faster queries and changes within Big Data tables.


## Architecture

This Architecture was used in the First Part of the Project:

 <div align=<"center"> 
 <image src= "https://user-images.githubusercontent.com/93526685/184159437-2034ed66-b9dd-4d2a-a52a-ebf35fd355c7.png" width="600px" />
 </div> 
 
This Architecture was used in the Second Part of the Project: 
 
  <div align=<"center"> 
 <image src= "https://user-images.githubusercontent.com/93526685/184159642-3ab4bcfe-17c4-4c36-bddb-f810628a9044.png" width="600px" />
 </div> 
 
 
## Autor

Jaqueline Cella

* Linkedin- @jaqueline-cella
* Github- @jaquelinecella

