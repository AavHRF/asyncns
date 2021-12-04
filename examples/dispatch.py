import asyncio
from asyncns import ApiClient
from asyncns.utils import ParamGenerator

# Create a client
client = ApiClient(
    useragent="Nation: Your Nation Here"  # Set your useragent to something descriptive, like your nation name.
)
# Update the client password
client.password = "password"  # Use your password here

# Create a generator
generator = ParamGenerator()

# Get the event loop
loop = asyncio.get_event_loop()

# Read in our dispatch text
with open("dispatch.txt", "r") as f:
    dispatch = f.read()

# Execute the dispatch
loop.run_until_complete(
    client.dispatch(
        generator.dispatch_params(
            action="add",
            title="Test Dispatch Please Ignore",
            text=dispatch,
            category=1,
            subcategory=105,
        )
    )
)
