-- MySQL script that lists all shows in the database hbtn_0d_tvshows
-- USE `hbtn_0d_tvshows`;
SELECT s.title, g.genre_id FROM tv_shows AS s
       INNER JOIN tv_show_genres AS g
       ON s.id = g.show_id
       ORDER BY s.title, g.genre_id ASC;
