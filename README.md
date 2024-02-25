![image](https://github.com/dogucanelci/Azure_e2e_data_engineering_project_1/assets/59261856/bf084dc4-c403-4b3e-a1c4-f67bdc339f6b)

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

![1_project_str](https://github.com/dogucanelci/Azure_e2e_data_engineering_project_1/assets/59261856/f0fdf9eb-5b61-4f18-806f-2d8f5d2cef13)


<a name="data-ingestion"></a>
### 📤 Data Ingestion
- A new cloud bucket is created as a source of the raw data.The raw dataset is uploaded into this bucket as .csv file. 

![2_IR](https://github.com/dogucanelci/Azure_e2e_data_engineering_project_1/assets/59261856/a2e6d6ee-5b67-4e16-8c99-4c54a1488d5a)

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

<a name="data-etl"></a>
### 📥 Data Orchestration and ETL Process
- Python scripts are built for data extraction, transformation and loading in Mage.ai with consistent order for get raw data from source bucket, manipulate and load into BigQuery Datawarehouse for analysing.

![8_synapse_pipeline](https://github.com/dogucanelci/Azure_e2e_data_engineering_project_1/assets/59261856/068eeb10-86e0-4122-b172-6480409f8fa4)

<a name="data-bqdwh"></a>
### 📊 BigQuery Datawarehouse
- When load process is done, there are dim tables and 1 fact table in BigQuery Data Warehouse as expected.
- In BigQuery, new big table(tbl_analytics) is created by join dim tables with fact tables to get desired columns.


<a name="data-reporting"></a>
### 📊 Data Reporting
- BigQuery is connected with Looker Studio BI , and used the Views of the DB to create interactive and insightful data visualizations.

![10_powerbi_report](https://github.com/dogucanelci/Azure_e2e_data_engineering_project_1/assets/59261856/67e3b07b-44f3-448b-b774-202b28850015)


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
