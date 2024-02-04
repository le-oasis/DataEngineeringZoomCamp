-- Identify the top 3 boroughs with the highest total revenue from taxi pickups on September 18th, 2019
SELECT
    "Borough",  -- Specify the borough for each trip
    SUM(total_amount) AS total_revenue  -- Calculate the total revenue for each borough
FROM
    green_taxi_data t  -- Primary table containing taxi trip data
    JOIN zones zpu  -- Join with zones table for pickup location information
        ON t."PULocationID" = zpu."LocationID"  -- Match pickup locations between tables
WHERE
    lpep_pickup_datetime >= '2019-09-18' AND lpep_pickup_datetime < '2019-09-19'  -- Filter for trips on September 18th, 2019
    AND "Borough" NOT IN ('Unknown')  -- Exclude trips with unknown boroughs
GROUP BY
    "Borough"  -- Group trips by borough to aggregate revenue
HAVING
    SUM(total_amount) > 50000  -- Retain only boroughs with total revenue over 50000
ORDER BY
    total_revenue DESC  -- Sort boroughs in descending order of total revenue
LIMIT 3;  -- Display only the top 3 boroughs
