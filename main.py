# Modules
import asyncio
import logging

# Functions and variables
from display import check_display, initialize, shutdown
from lnbits import get_lnurl, get_switches
from payments import listener
from screens import make_idlescreen

####### MAIN ########

# The main function is run, showing the idle screen and waiting for incoming payments

async def main():
	try:
		logging.info("Starting Zapshutter")
		check_display()
		initialize()
		#get_switches()
		#get_lnurl()
		await listener()

	except KeyboardInterrupt:
		shutdown()

asyncio.run(main())