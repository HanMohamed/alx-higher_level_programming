-- Import the database dump from hbtn_0d_tvshows
-- a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- The tv_shows table contains only one record where title = Dexter
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- tv_genres(id, name)
-- tv_show_genres(show_id, genre_id)
-- tv_shows(id, title)
SELECT tv_genres.name AS name
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
