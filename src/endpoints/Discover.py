from endpoint import Endpoint
from ..models.movie import Movie

class DiscoverEndpoint(Endpoint):
    endpoint = "/discover"

    def getMoviesByProvider(self, provider: str) -> list[Movie]:
        return []