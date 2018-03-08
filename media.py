class Movie():
    """This class provides a way to store movie related information"""

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, release_year):
        '''The constructor that is called when a new Movie object is created.
        self - The object that is being created
        movie_title - The title of the movie
        movie_storyline - The storyline of the movie
        poster_image - Link to an image that is a poster of the movie
        trailer_youtube - Link to a youtube movie trailer for the movie
        release_year - The year the movie was released in theaters'''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_year = release_year
