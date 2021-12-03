from api_client import ApiClient


class DispatchClient:

    def __init__(self, client: ApiClient):
        self.client: ApiClient = client

