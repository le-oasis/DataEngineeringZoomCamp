# DataEngineeringZoomCamp

# Module 1 Homework: Docker & SQL

**Preparing the Environment**

Before proceeding with the SQL exercises, we'll download the necessary data files using the following commands:

**1. Download the gzipped CSV file:**



# Data Pipeline in Docker: Homework
### Project Overview
This project aims to create a data pipeline that ingests, processes, and analyzes NY Taxi data using Docker containers. The pipeline involves the following key components:

- Data Ingestion: Downloads NY Taxi data (green_tripdata_2019-09.csv.gz and taxi_zone_lookup.csv) from external sources and utilizes a Python script (ingest_data.py) to ingest the data into a PostgreSQL database.
- Database: Employs a PostgreSQL database (pg-database) to store the ingested data.
- Data Exploration and Analysis: Leverages Jupyter Notebooks for data exploration and analysis tasks, potentially utilizing Spark for large-scale data processing.

# Project Structure
The project directory structure comprises various folders and files, each serving a specific purpose:

- Root Directory: Houses key files like the Dockerfile (building instructions), README.md (project information), docker-compose.yml (orchestrates multiple containers), requirements.txt (Python dependencies), output.csv (final output data), and spark folder (Spark configuration and resources).
- Apps Directory: Contains Python scripts related to data ingestion (ingest_data.py) and pipeline logic (pipeline.py), along with SQL scripts for data transformations (sql_scripts).
- Lakehouse Directory: Stores raw data files (CSV format) in the data subfolder and a Jupyter Notebook environment for analysis in the jupyter subfolder.
- Notebooks Directory: Hosts individual Jupyter Notebooks used for data exploration and analysis tasks.
- Doc Directory: Contains images for documentation or visualization purposes.


# Installation and Setup
### Install Data:

```
curl -o taxi_zone_lookup.csv https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv
```

```
curl -L --silent https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz | gzip -d > green_tripdata_2019-09.csv
```


Use code with caution. Learn more

### Create Dockerfile:


```
FROM python:3.9

# Copy requirements.txt first for efficient caching
COPY requirements.txt .


# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory
WORKDIR /app

# Copy the pipeline.py file
COPY apps/ingest_data.py ingest_data.py

# Override the entrypoint
ENTRYPOINT [ "python","ingest_data.py" ]

```

### Build Docker Image:

```
docker build -t taxi_ingest:v01 .
```

### Install pgcli for Connecting to PostgreSQL:

```
pip install pgcli
```

# Running the Data Pipeline
Create Docker Network:

```
docker network create oasiscorp
```


## Run PostgreSQL Container:

```
docker run -it \
  -e POSTGRES_USER="oasis" \
  -e POSTGRES_PASSWORD="oasis" \
  -e POSTGRES_DB="ny_taxi" \
  -v ~/ny_taxi_postgres_data:/var/lib/postgres/data \
  -p 5435:5432 \
  --network=oasiscorp \
  --name pg-database \
  postgres:13
```

## Run pgAdmin Container (Optional for Graphical Interface):

```
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8383:80 \
  --network=oasiscorp \
  --name pgadmin \
  dpage/pgadmin4:latest
```




## Run Data Ingestion Pipeline:

```
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz"

docker run -it \
  --network=oasiscorp \
  taxi_ingest:v01 \
  --user=root \
  --password=root \
  --host=pg-database \
  --port=5432 \
  --db=ny_taxi \
  --table_name=green_taxi_data \
  --url="$URL"
```


## Data Exploration and Analysis:
### Install Jupyter:

```
pip install jupyter
```

### Start Jupyter Notebook:

```
jupyter notebook
```


### Connect to PostgreSQL Using SQLAlchemy:
Within your Jupyter Notebook, you can connect to the PostgreSQL database using SQLAlchemy. Here's a basic example:


```
from sqlalchemy import create_engine

# Replace with your credentials and database details
engine = create_engine(f"postgresql://oasis:oasis@pg-database:5432/ny_taxi")

# Connect to the database
connection = engine.connect()

# Execute queries and analyze data using pandas or other libraries
taxi_data = pd.read_sql_query("SELECT * FROM green_taxi_data", connection)
# ... explore the data using pandas methods and visualizations

# Close the connection
connection.close()
```



### Data Validation:

After ingesting the data into the PostgreSQL database, it's important to validate that the data has been correctly loaded. You can do this by connecting to the PostgreSQL database using `pgcli` and running some SQL queries to inspect the data.

To connect to your database, use the following command in your terminal:

```
pgcli -h localhost -p 5435  -u oasis -d ny_taxi
```


This command connects to the PostgreSQL database running on localhost with port 5435, using oasis as the username and ny_taxi as the database name.

Once connected, execute SQL queries to check the data. For example:






Remember to replace the credentials and database details with your actual values.

### Utilize Docker for Scalability:
This project utilizes Docker for containerization, enabling easy deployment and scaling. You can create additional Docker containers for tasks like pre-processing data, running Spark Jobs, or serving the processed data through APIs.

### Further Resources:

SQLAlchemy documentation: https://docs.sqlalchemy.org/
pgcli documentation: https://www.pgcli.com/
Jupyter Notebook documentation: https://docs.jupyter.org/
Docker documentation: https://docs.docker.com/

### Conclusion:

This document provides a comprehensive overview of your data pipeline project, including installation steps, running instructions, and data exploration opportunities. Remember to customize the provided code examples and configurations with your specific details. For further exploration, consider investigating advanced data analysis techniques.

