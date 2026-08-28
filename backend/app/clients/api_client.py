import requests


class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def get(self, endpoint: str, **kwargs):
        return requests.get(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            **kwargs
        )

    def post(self, endpoint: str, **kwargs):
        return requests.post(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            **kwargs
        )

    def put(self, endpoint: str, **kwargs):
        return requests.put(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            **kwargs
        )

    def patch(self, endpoint: str, **kwargs):
        return requests.patch(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            **kwargs
        )

    def delete(self, endpoint: str, **kwargs):
        return requests.delete(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            **kwargs
        )