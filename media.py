import webbrowser

class Movie():
    def __init__(self,movie_title,movie_storyline,poster_url,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_url
        self.trailer_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_url)


    def to_string(self):
        return self.title + ": " + self.storyline
