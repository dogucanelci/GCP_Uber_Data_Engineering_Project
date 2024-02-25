![0_report_first_overview](https://github.com/dogucanelci/GCP_Uber_Data_Engineering_Project/assets/59261856/0f1f95d7-a087-4601-8a8d-bbe117f5a70f)

<h1 style="display: inline-block;"> Uber End to End Data Engineering Project on Google Cloud Platform </h1>
buraya data info ve linkler gelecek

## 📝 Table of Contents
1. [Project Overview](#introduction)
2. [Project Architecture](#project-architecture)  
  2.1. [Data Modeling](#data-modeling)
  2.2. [Data Ingestion](#data-ingestion)  
  2.3. [Compute Engine Building](#data-vm)  
  2.4. [ETL Process](#data-etl)
  2.5. [BigQuery Data Warehouse](#data-bqdwh)
  2.6. [Data Reporting](#data-reporting)
3. [Credits](#credits)
4. [Contact](#contact)

<a name="introduction"></a>
## 🔬 Project Overview 

This project can be defined as End-to-end Data Engineering Project applied in Google Cloud Platform. NYC Uber driver dataset is used for these project.Uber dataset is investigated and new data model is created in first process. A new cloud bucket is created as a source of the raw data. In next step, new Virtual Machine is created as computing engine to install and Mage.ai tool permenantly. Python scripts are built for data extraction, transformation and loading in Mage.ai with consistent order for get raw data from source bucket, manipulate and load into BigQuery Datawarehouse for analysing. In BigQuery, new big table is created by join dim tables with fact tables to get desired columns. In final step Report is created in LookerStudio.

<a name="project-architecture"></a>
## 📝 Project Architecture

You can find the detailed information on the diagram below:

![1_project_structure](https://github.com/dogucanelci/GCP_Uber_Data_Engineering_Project/assets/59261856/8d43e743-6a78-45c9-acbf-9425f2d88f64)

<a name="data-ingestion"></a>
### 📤 Data Ingestion
- A new cloud bucket is created as a source of the raw data.The raw dataset is uploaded into this bucket as .csv file.
  
![2_data_ingestion_bucket](https://github.com/dogucanelci/GCP_Uber_Data_Engineering_Project/assets/59261856/789d5c40-0bb7-4c49-b29d-03e0777bff71)

<a name="data-vm"></a>
### ⚙️ Compute Engine Building
- New Virtual Machine instance is created for using as a Compute Engine to install and run Orchestration tool(Mage.ai).
- VM is created and access the instance via SSH.
- All requirements(python3 and mage.ai) are installed.
- Requirements:
  
```sh
# Install Python and pip 
sudo apt-get update
sudo apt-get install python3-distutils
sudo apt-get install python3-apt
sudo apt-get install wget
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
sudo pip3 install mage-ai
Install Pandas
sudo pip3 install pandas
sudo pip3 install google-cloud
sudo pip3 install google-cloud-bigquery
```
![3_virtual_machine_building](https://github.com/dogucanelci/GCP_Uber_Data_Engineering_Project/assets/59261856/3d120f3f-c637-4646-ab14-a32d199e1f25)

<a name="data-etl"></a>
### 📥 Data Orchestration and ETL Process
- Python scripts are built for data extraction, transformation and loading in Mage.ai with consistent order for get raw data from source bucket, manipulate and load into BigQuery Datawarehouse for analysing.

![4_mage_ai_etl](https://github.com/dogucanelci/GCP_Uber_Data_Engineering_Project/assets/59261856/f0f39b0a-5fc7-45c8-a17f-4111e0e205dd)

<a name="data-bqdwh"></a>
### 📊 BigQuery Datawarehouse
- When load process is done, there are dim tables and 1 fact table in BigQuery Data Warehouse as expected.
- In BigQuery, new big table(tbl_analytics) is created by join dim tables with fact tables to get desired columns.
  
![5_bigquery_all_tables](https://github.com/dogucanelci/GCP_Uber_Data_Engineering_Project/assets/59261856/8454208d-020e-4b98-b67a-6c0ab370f6fc)

![6_bigquery_tbl_analytics](https://github.com/dogucanelci/GCP_Uber_Data_Engineering_Project/assets/59261856/a305f1f8-fa8e-4fff-b6bd-0a21f023fadf)

<a name="data-reporting"></a>
### 📊 Data Reporting
- BigQuery is connected with Looker Studio BI , and used the Views of the DB to create interactive and insightful data visualizations.

![7_report1](https://github.com/dogucanelci/GCP_Uber_Data_Engineering_Project/assets/59261856/019ea373-1ed6-45ae-9da0-8c36637514b9)
![8_report2](https://github.com/dogucanelci/GCP_Uber_Data_Engineering_Project/assets/59261856/89baf668-c774-43ad-a14d-6eb71ada0de3)


### 🛠️ Technologies Used

- **Data Source**: Google Cloud Bucket Storage
- **Orchestration**: Mage.ai
- **Compute Engine**: Google Cloud VM Instance
- **ETL Process**: Mage.ai, Python 
- **Date Warehousing**: Bigquery, t-SQL
- **Storage**: Google Cloud Bucket Storage
- **Data Visualization**: Looker Studio

<a name="credits"></a>
## 📋 Credits

- This Project is inspired by the video of the [YouTube Channel "Darshil Parmar"](https://www.youtube.com/watch?v=WpQECq5Hx9g)  

<a name="contact"></a>
## 📨 Contact Me

[LinkedIn](https://www.linkedin.com/in/elcidogucan/)
[Website](https://www.dogucanelci.com)
[Gmail](dogucanelci@gmail.com)
