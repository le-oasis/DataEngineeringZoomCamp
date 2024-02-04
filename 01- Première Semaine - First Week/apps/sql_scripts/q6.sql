-- Find the drop-off zone with the largest tip for trips picked up in Astoria in September 2019
SELECT
    -- Specify the name of the drop-off zone
    zdo."Zone" AS dropoff_zone,  
    -- Calculate the maximum tip amount for each zone
    MAX(tip_amount) AS max_tip  
-- Primary table containing trip data
FROM green_taxi_data t  
-- Join with zones table for pickup location information
JOIN zones zpu  
-- Match pickup locations between tables
    ON t."PULocationID" = zpu."LocationID"  
    -- Join with zones table for dropoff location information
JOIN zones zdo  
-- Match dropoff locations between tables
    ON t."DOLocationID" = zdo."LocationID"  
    -- Filter for trips with pickup zone 'Astoria'
WHERE
    zpu."Zone" = 'Astoria'  
    AND lpep_pickup_datetime >= '2019-09-01' AND lpep_pickup_datetime < '2019-10-01'  -- Filter for trips in September 2019
GROUP BY
    zdo."Zone"  -- Group trips by drop-off zone to aggregate tip amounts
ORDER BY
    max_tip DESC  -- Sort results by maximum tip in descending order
LIMIT 1;  -- Display only the zone with the highest maximum tip
