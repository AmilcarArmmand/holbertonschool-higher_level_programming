-- MySQL script that uses database hbtn_0d_tvshows
-- lists all shows, and all genres linked to that show
-- USE `hbtn_0d_tvshows`;
SELECT s.title, t.name FROM tv_shows AS s
       LEFT JOIN tv_show_genres AS g
       ON s.id = g.show_id
       LEFT JOIN tv_genres AS t
       ON t.id = g.genre_id
       ORDER BY s.title, t.name ASC;
