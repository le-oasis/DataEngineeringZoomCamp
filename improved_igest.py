import pandas as pd
from sqlalchemy import create_engine
import argparse


parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

# user, password, host, port, db name, table name, url of the csv

parser.add_argument('user', help='username for postgres')
parser.add_argument('pass', help='password for postgres')
parser.add_argument('host', help='host for postgres')
parser.add_argument('port', help='port for postgres')
parser.add_argument('db', help='database name for postgres')
parser.add_argument('table-name', help='table for postgres')
parser.add_argument('url', help='url of the csv file')



parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))


# Create database connection
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

# Read data in chunks and write to database
chunksize = 100000
with engine.connect() as connection:
    for chunk in pd.read_csv("data/green_tripdata_2019-09.csv", chunksize=chunksize):
        # Transform datetime columns within the loop
        chunk[['lpep_pickup_datetime', 'lpep_dropoff_datetime']] = chunk[['lpep_pickup_datetime', 'lpep_dropoff_datetime']].apply(pd.to_datetime)

        # Write chunk to database efficiently
        chunk.to_sql("green_taxi_data", con=connection, if_exists='append', index=False)

# Print schema as a separate step
print(pd.io.sql.get_schema(chunk, name="green_taxi_data", con=engine))
