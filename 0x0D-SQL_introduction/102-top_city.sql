-- script that displays the top 3 of cities temperature
-- during July and August ordered by temperature (descending)
-- from the MySQL database hbtn_0c_0 in MySQL server
SELECT city, AVG(value) AS avg_temp FROM temperatures
       WHERE month=7 OR month=8
       GROUP By city
       ORDER BY avg_temp DESC
       LIMIT 3;
