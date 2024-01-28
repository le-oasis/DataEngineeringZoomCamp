import pandas as pd
from sqlalchemy import create_engine
import argparse



def main(params):

    user=params.user
    password=params.password
    host=params.host
    port=params.port
    db=params.db
    table_name = params.table_name





    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/ny_taxi')

    # Read Data
    df_iter = pd.read_csv("data/green_tripdata_2019-09.csv", iterator=True, chunksize=100000)

    df = next(df_iter)

    # Transform
    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

    # Populate Columns to Postgres Db
    df.head(n=0).to_sql(name="green_taxi_data",con=engine, if_exists='replace')

    df.to_sql(name="green_taxi_data", con=engine, if_exists='append')




parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

# user, password, host, port, db name, table name, url of the csv

parser.add_argument('user', help='username for postgres')
parser.add_argument('pass', help='password for postgres')
parser.add_argument('host', help='host for postgres')
parser.add_argument('port', help='port for postgres')
parser.add_argument('db', help='database name for postgres')
parser.add_argument('table_name', help='table for postgres')
parser.add_argument('url', help='url of the csv file') 

while True:
    t_start = time()

    df = next(df_iter)

    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)

    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

    df.to_sql(name="green_taxi_data", con=engine, if_exists='append')

    t_end = time()

    print('Inserted another chunk.. took %.3f seconds' % (t_end - t_start))