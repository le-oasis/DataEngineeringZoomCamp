SELECT COUNT(*) AS trip_count
FROM green_taxi_data
WHERE lpep_pickup_datetime >= '2019-09-18 00:00:00' AND lpep_pickup_datetime < '2019-09-19 00:00:00';
