import webbrowser

# SAH Added starring and rating to default movie class
class Movie():
    def __init__(self,movie_title,movie_storyline,poster_url,trailer_youtube, starring, rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_youtube
        self.starring = starring
        self.rating = rating

    def show_trailer(self):
    	"""open the url for the movie trailer"""
        webbrowser.open(self.trailer_url)

# no longer required - was there to test
#    def to_string(self):
#        return self.title + ": " + self.storyline
