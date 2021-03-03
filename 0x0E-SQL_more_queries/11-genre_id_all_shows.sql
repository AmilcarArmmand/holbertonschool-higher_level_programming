-- MySQL script that lists all shows in the database hbtn_0d_tvshows
-- display: tv_shows.title - tv_show_genres.genre_id
-- Sort results in ascending order by tv_shows.title and tv_show_genres.genre_id
-- If a show doesn’t have a genre, display NULL
-- Use only one SELECT statement
-- USE `hbtn_0d_tvshows`;
SELECT s.title, g.genre_id FROM tv_shows AS s
       LEFT JOIN tv_show_genres AS g
       ON s.id = g.show_id
       ORDER BY s.title, g.genre_id ASC;
