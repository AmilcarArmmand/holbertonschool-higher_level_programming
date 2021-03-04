-- MySQL script that uses database hbtn_0d_tvshows
-- list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- USE `hbtn_0d_tvshows`;
SELECT DISTINCT name FROM tv_genres AS g
       INNER JOIN tv_show_genres AS s
       ON g.id = s.genre_id

       INNER JOIN tv_shows AS t
       ON s.show_id = t.id
       WHERE g.name NOT IN(
       	     SELECT name FROM tv_genres AS g
       	     INNER JOIN tv_show_genres AS s
       	     ON g.id = s.genre_id
	     INNER JOIN tv_shows AS t
	     ON s.show_id = t.id
	     WHERE t.title = 'Dexter')
       ORDER BY g.name ASC;
