-- MySQL script that uses database hbtn_0d_tvshows
-- lists all Comedy shows
-- USE `hbtn_0d_tvshows`;
SELECT t.title FROM tv_shows AS t
       INNER JOIN tv_show_genres AS g
       ON t.id = g.show_id
       INNER JOIN tv_genres AS s
       ON s.id = g.genre_id
       WHERE s.name = 'Comedy'
       ORDER BY t.title ASC;
