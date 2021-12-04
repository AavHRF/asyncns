# Welcome to `asyncns`!

`asyncns` is a library for asynchronous requests to the NationStates API. It operates at a high level,
and is designed in a way to make your life easier while interacting with the API.

To that end, `asyncns` contains a `utils` module, which contains a number of utility functions for making requests easier,
like a parameter generator, and a built-in XML parser.

**WARNING** : `asyncns` is still in development, and may change in the future.
Functions may change or be removed without warning. If you like the way `asyncns` works,
pin your version to that particular version in your `requirements.txt` file.

*Some Notes*:
* `asyncns` adheres to [semantic versioning](https://semver.org/) for versioning. This means that
any breaking changes to the library will be reflected in the major (i.e. 1.0.0) version number.
* `asyncns` is written in [Python 3](https://www.python.org/downloads/). It will not work with Python 2.

[Main Page](index.md) | [`utils` Documentation](docs/utils.md) | [GitHub](https://github.com/AavHRF/asyncns) | [License](LICENSE.md)


# Getting Started
```python
# Example start for asyncns
import asyncio
from asyncns import ApiClient
client = ApiClient(useragent="Nation: YourNation")
# Get the event loop
loop = asyncio.get_event_loop()
# Find information on Europe
europe = loop.run_until_complete(client.get_region("europe"))
# You can also get a specific shard
europe2 = loop.run_until_complete(
    client.get_region(
        region="europe",
        shard="numnations"
    )
)
```

# API Reference

### `asyncns.api_client`

**Class**: `asyncns.api_client.ApiClient`

**Class Methods**:

*Async* `asyncns.api_client.ApiClient.dispatch()`

| Parameter | Type   | Description                 |
|-----------|--------|-----------------------------|
| `data`    | `dict` | The data to send to the API |

*Async* `asyncns.api_client.ApiClient.get_nation()`

| Parameter | Type  | Description                                                  |
|-----------|-------|--------------------------------------------------------------|
| `nation`  | `str` | The nation                                                   |
| `shard`   | `str` | The shard that you are requesting information on. (Optional) |

*Async* `asyncns.api_client.ApiClient.get_region()`

| Parameter | Type  | Description                                                  |
|-----------|-------|--------------------------------------------------------------|
| `region`  | `str` | The nation                                                   |
| `shard`   | `str` | The shard that you are requesting information on. (Optional) |

**Internal Methods**:

*Async* `asyncns.api_client.ApiClient._get()`
> Document later

*Async* `asyncns.api_client.ApiClient._post()`
> Document later