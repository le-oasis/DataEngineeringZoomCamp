-- This query retrieves taxi trip information, including timestamps, fares, and descriptive pickup/dropoff locations, by joining data from multiple tables.

SELECT
    lpep_pickup_datetime,      -- Timestamp of passenger pickup
    lpep_dropoff_datetime,     -- Timestamp of passenger dropoff
    total_amount,             -- Total fare for the trip
    CONCAT(zpu."Borough", ' / ', zpu."Zone") AS "pick_up_loc",      -- Combine borough and zone for descriptive pickup location
    CONCAT(zdo."Borough", ' / ', zdo."Zone") AS "dropoff_loc"      -- Combine borough and zone for descriptive dropoff location

FROM
    green_taxi_data t,         -- Table containing taxi trip data
    zones zpu,                 -- Table containing zone information (for pickup locations)
    zones zdo                  -- Table containing zone information (for dropoff locations)

WHERE
    t."PULocationID" = zpu."LocationID"  -- Match pickup location ID between taxi data and zone table
    AND t."DOLocationID" = zdo."LocationID";  -- Match dropoff location ID between taxi data and zone table
