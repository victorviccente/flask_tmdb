# models/movie.py
class Movie:
    def __init__(self, data):
        self.id = data.get('id')
        self.title = data.get('title')
        self.overview = data.get('overview')
        self.poster_path = data.get('poster_path')
        self.release_date = data.get('release_date')
        self.vote_average = data.get('vote_average')
        self.backdrop_path = data.get('backdrop_path')
        self.genres = data.get('genres', [])
        
    @property
    def poster_url(self):
        if self.poster_path:
            return f"https://image.tmdb.org/t/p/w500{self.poster_path}"
        return None

    @property
    def backdrop_url(self):
        if self.backdrop_path:
            return f"https://image.tmdb.org/t/p/original{self.backdrop_path}"
        return None