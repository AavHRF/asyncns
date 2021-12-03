import aiohttp
from utils.ratelimit import Limiter

limiter = Limiter(limit=50, interval=30)


class ApiClient:
    """
    An API wrapper for the NationStates API.

    TODO: Write documentation
    """

    def __init__(self, useragent: str):
        self.useragent = useragent
        self.password = None
        self.headers = {
            "User-Agent": self.useragent,
        }
        self.session = aiohttp.ClientSession()

    @limiter
    async def _get(self, url: str, params: dict = None, private: bool = False):
        """
        Perform a GET request to the API.

        :param url: The URL to request
        :param params: The parameters to pass to the request
        :return: The response from the API
        :rtype: str
        """
        if not private:
            text = ""
            async with self.session.get(url, params=params) as response:
                text = await response.text()
            return text
        if private:
            text = ""
            self.headers.update({"X-Password": self.password})
            async with self.session.get(url, params=params, headers=self.headers) as response:
                text = await response.text()
            return text

    @limiter
    async def _post(self, url: str, data: dict = None, private: bool = False):
        """
        Perform a POST request to the API.

        :param url: The URL to request
        :param data: The data to pass to the request
        :return: The response from the API
        :rtype: str
        """

        if not private:
            text = ""
            async with self.session.post(url, data=data, headers=self.headers) as response:
                text = await response.text()
            return text
        if private:
            text = ""
            self.headers.update({"X-Password": self.password})
            async with self.session.post(url, data=data, headers=self.headers) as response:
                text = await response.text()
            return text

    async def get_nation(self, nation: str, shard: str = None):
        """
        Performs a lookup on a nation.

        :param shard: str
        :param nation: str
        :return: XML response from the API
        :rtype: str
        """
        if not shard:
            url = "https://www.nationstates.net/cgi-bin/api.cgi"
            params = {
                "nation": nation,
            }
            return await self._get(url, params=params)
        else:
            url = "https://www.nationstates.net/cgi-bin/api.cgi"
            params = {
                "nation": nation,
                "q": shard,
            }
            return await self._get(url, params=params)

    async def get_region(self, region: str, shard: str = None):
        """
        Performs a lookup on a region.

        :param shard: str
        :param region: str
        :return: XML response from the API
        :rtype: str
        """
        if not shard:
            url = "https://www.nationstates.net/cgi-bin/api.cgi"
            params = {
                "region": region,
            }
            return await self._get(url, params=params)
        else:
            url = "https://www.nationstates.net/cgi-bin/api.cgi"
            params = {
                "region": region,
                "q": shard,
            }
            return await self._get(url, params=params)

    async def world_api(self, shard: str):
        """
        Queries the World API.

        :param shard: str
        :return:
        """
        url = "https://www.nationstates.net/cgi-bin/api.cgi"
        params = {
            "q": shard,
        }
        return await self._get(url, params=params)