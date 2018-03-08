import media
import fresh_tomatoes

lotr = media.Movie("The Lord of the Rings: Fellowship of the Ring",
 "A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.",
 "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
 "https://www.youtube.com/watch?v=LJ4mM3YIqx0", 2001)

lotr2 = media.Movie("The Lord of the Rings: The Two Towers",
"While Frodo and Sam edge closer to Mordor with the help of the shifty Gollum, the divided fellowship makes a stand against Sauron's new ally, Saruman, and his hordes of Isengard.",
"https://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg",
"https://www.youtube.com/watch?v=ve5HZfrrUqc", 2002)

godfather = media.Movie("The Godfather",
"The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
"https://images-na.ssl-images-amazon.com/images/M/MV5BY2Q2NzQ3ZDUtNWU5OC00Yjc0LThlYmEtNWM3NTFmM2JiY2VhXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY268_CR3,0,182,268_AL_.jpg",
"https://www.youtube.com/watch?v=sY1S34973zA", 1972)

godfatherII = media.Movie("The Godfather Part II",
"The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate",
"https://images-na.ssl-images-amazon.com/images/M/MV5BMjZiNzIxNTQtNDc5Zi00YWY1LThkMTctMDgzYjY4YjI1YmQyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UY268_CR3,0,182,268_AL_.jpg",
"https://www.youtube.com/watch?v=OA1ij0alE0w&t=14s", 1974)

enemy_at_the_gates = media.Movie("Enemy at the Gates",
"A Russian and a German sniper play a game of cat-and-mouse during the Battle of Stalingrad.",
"https://images-na.ssl-images-amazon.com/images/M/MV5BYWFlY2E3ODQtZWNiNi00ZGU4LTkzNWEtZTQ2ZTViMWRhYjIzL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
"https://www.youtube.com/watch?v=xqwlIaOyBSA", 2001)

the_matrix = media.Movie("The Matrix",
"A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
"https://images-na.ssl-images-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg",
"https://www.youtube.com/watch?v=Q8g9zL-JL8E", 1999)

movies = [lotr, lotr2, godfather, godfatherII, enemy_at_the_gates, the_matrix]

#Uses the provided movies array to generate a webpage
fresh_tomatoes.open_movies_page(movies)
