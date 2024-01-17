-- Import the database dump from hbtn_0d_tvshows
--  a script that lists all Comedy shows in the database hbtn_0d_tvshows
-- The tv_genres table contains only one record where name = Comedy
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- tv_genres(id, name)
-- tv_show_genres(show_id, genre_id)
-- tv_shows(id, title)
SELECT tv_shows.title AS title
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY title;
