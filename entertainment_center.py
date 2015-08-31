import media
import fresh_tomatoes

# adding 3 movies
aliens = media.Movie("Aliens",
     "Stranded on a hostile environment, the crew of the Nostromo struggle for survival against an unknown force",
     "https://upload.wikimedia.org/wikipedia/en/thumb/f/fb/Aliens_poster.jpg/220px-Aliens_poster.jpg",
     "https://www.youtube.com/watch?v=zNE0dlHcmgA",
     "Sigourney Weaver",
     "4.8 Xenomorphs")

jurassic_world = media.Movie("Jurassic World",
      "Once again, someone tries to help life find a way, and Starlord has to step in to save the day",
      "https://upload.wikimedia.org/wikipedia/en/thumb/6/6e/Jurassic_World_poster.jpg/220px-Jurassic_World_poster.jpg",
      "https://www.youtube.com/watch?v=RFinNxS5KN4",
      "Chris Pratt (Starlord)",
      "Waiting for it to come out on Bluray")

terminator = media.Movie("Terminator: Genisys",
      "I'm showing my age - I still remember when this came out the first time.  It was Awesome.",
      "https://upload.wikimedia.org/wikipedia/en/thumb/b/bc/Terminator_Genisys.JPG/220px-Terminator_Genisys.JPG",
      "https://www.youtube.com/watch?v=jNU_jrPxs-0",
      "Arnie - he'll be back.  I'm sure of it.",
      "T-1000")

# creating an array of 3 movies to pass to fresh_tomatoes
movies_array = [aliens,jurassic_world,terminator]
# fresh tomatoes will generate a static HTML page based on the movies passed in through the array above.
fresh_tomatoes.open_movies_page(movies_array)

