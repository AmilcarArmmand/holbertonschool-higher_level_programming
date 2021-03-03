-- MySQL script that lists all shows in the database hbtn_0d_tvshows
-- display all genres number of shows linked
-- Display: <TV Show genre> - <Number of shows linked to this genre>
-- First column is called genre, second column is called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked
-- USE `hbtn_0d_tvshows`;
SELECT g.name AS genre, COUNT(*) AS number_of_shows
       FROM tv_genres AS g
       INNER JOIN tv_show_genres AS t
       ON g.id = t.genre_id
       GROUP BY g.name ORDER BY number_of_shows DESC;
