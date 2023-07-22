import requests
from requests import Response
from exceptions import ApiError

class Endpoint:
    api_url = "https://api.themoviedb.org/3"

    def _checkStatus(self, res: Response) -> str:
        if res.status_code > 299 or res.status_code < 200:
            raise ApiError(f"Not a valid api response: {res.status_code}")
        
        return res.json()

    def get(self, endpoint: str, headers: dict, p: dict) -> str:
        r = requests.get(f"{self.api_url}{endpoint}", params=p, headers=headers)

        return self._checkStatus(r)