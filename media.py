import webbrowser


# SAH Added starring and rating to default movie class
class Movie():
    """ Class Movie
    This adds the init module to create an object of type, 'Movie'
    which contains it's title. storyline, poster image, trailer,
    star and an arbitrary rating.
    """
    def __init__(self, movie_title, movie_storyline, poster_url,
                 trailer_youtube, starring, rating):
        """ docstring for the init constructor
        this allows us to store all the standard variables for the default
        movie class
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_youtube
        self.starring = starring
        self.rating = rating

    def show_trailer(self):
        """show_trailer() docstring
        this returns a webbrowser call to open the provided url
        """
        webbrowser.open(self.trailer_url)

# no longer required - was there to test
#    def to_string(self):
#        return self.title + ": " + self.storyline
