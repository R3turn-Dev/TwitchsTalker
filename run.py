import logging
from CfTwMonitor import Monitor

logging.basicConfig(level=logging.INFO)



mon.setup()
mon.sanic.load_routes(
    [
        "routes.root",
        "routes.api"
    ]
)
print(" Sanic routes ", mon.sanic.router)
mon.discord.load_extension("cogs.logger")

mon.run()
