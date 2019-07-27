import logging
from CfTwMonitor import Monitor

logging.basicConfig(level=logging.INFO)



mon.setup()
mon.discord.load_extension("cogs.logger")
mon.run()
