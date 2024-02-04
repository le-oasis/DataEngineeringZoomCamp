#############################################################
#   CSV Data Ingestion to PostgreSQL Database Script
#   Author: Mahmud.O
#   Date: 2024-01-28
#   Description: Downloads a compressed CSV file from a URL,
#               decompresses it, reads the data in chunks,
#               and efficiently inserts it into a PostgreSQL
#               database table, handling datetime conversions.
#############################################################
# For data manipulation
import pandas as pd
# For database interaction
from sqlalchemy import create_engine
# For command-line argument parsing
import argparse
# For file system operations
import os
# For timing operations
from time import time
# For handling compressed files
import gzip


def main(params):
    """Main function to handle CSV download and database ingestion."""

    # Extract parameters from parsed arguments
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url 

    # Download and decompress the file
    csv_name = 'output.csv'
    os.system(f"wget -O - {url} | gzip -d > {csv_name}")

    # Connect to the database
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    with engine.connect() as connection:
        # Read data in chunks
        df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

        # Transform datetime columns once
        for chunk in df_iter:
            chunk[['lpep_pickup_datetime', 'lpep_dropoff_datetime']] = chunk[['lpep_pickup_datetime', 'lpep_dropoff_datetime']].apply(pd.to_datetime)

            # Write chunk to database
            chunk.to_sql(name=table_name, con=connection, if_exists='append', index=False)

# Main Function
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    # Parse command-line arguments
    parser.add_argument('--user', help='username for postgres', type=str)
    parser.add_argument('--password', help='password for postgres', type=str)
    parser.add_argument('--host', help='host for postgres', type=str)
    parser.add_argument('--port', help='port for postgres', type=int)
    parser.add_argument('--db', help='database name for postgres', type=str)
    parser.add_argument('--table_name', help='table for postgres', type=str)
    parser.add_argument('--url', help='url of the csv file', type=str)

    args = parser.parse_args()

     # Call the main function
    main(args)
