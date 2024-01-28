-- This query retrieves a limited set of data from three tables, merging information based on location IDs.

SELECT *  -- Select all columns from the resulting joined table.

FROM  -- Specify the tables to join:
       green_taxi_data t,  -- Table containing taxi trip data
       zones zpu,          -- Table containing zone information for passenger pickup locations
       zones zdo          -- Table containing zone information for passenger dropoff locations

WHERE                       -- Define the conditions for joining the tables:
       t."PULocationID" = zpu."LocationID"  -- Match passenger pickup location ID in taxi data with zone table
       AND t."DOLocationID" = zdo."LocationID"  -- Match passenger dropoff location ID in taxi data with zone table

LIMIT 100;  -- Restrict the output to the first 100 rows of the result set.
