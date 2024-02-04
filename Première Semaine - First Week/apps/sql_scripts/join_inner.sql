-- Get taxi trip details and descriptive locations
SELECT
    -- Time of passenger pickup
    lpep_pickup_datetime,
    -- Time of passenger dropoff
    lpep_dropoff_datetime,
    -- Total fare for the trip
    total_amount,
    -- Combine borough and zone for pickup location
    CONCAT(zpu."Borough", ' / ', zpu."Zone") AS "pick_up_loc",
    -- Combine borough and zone for dropoff location
    CONCAT(zdo."Borough", ' / ', zdo."Zone") AS "dropoff_loc"

FROM
    -- Table containing taxi trip data
    green_taxi_data t
    -- Join with zone table for pickup locations
    JOIN zones zpu ON t."PULocationID" = zpu."LocationID"
    -- Join with zone table for dropoff locations
    JOIN zones zdo ON t."DOLocationID" = zdo."LocationID";
