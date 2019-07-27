import logging
from json import load
from CfTwMonitor import Monitor

logging.basicConfig(level=logging.INFO)

settings = load(open("settings.json"))


mon = Monitor(
    token=settings['credentials']['discord']['bot'],
    host="0.0.0.0",
    port=80,
    debug=True,
    prefix="에낙아 "
)

mon.setup()
mon.sanic.load_routes(
    [
        "routes.root",
        "routes.api"
    ]
)
print(" Sanic routes ", mon.sanic.router)

mon.discord.load_extension("cogs.logger")
mon.discord.load_extension("cogs.helper")

mon.run()
