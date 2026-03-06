# Modules
import asyncio
import logging
import websockets
from time import sleep

# Functions and variables
from display import initialize, shutdown
from lnbits import get_payments
from screens import make_confirmation_screen, make_errorscreen, make_idlescreen, make_success_overlay
from trigger import pulse
from var import suceess_screen_expiry, ws_switch

####### VARIABLES ########


async def listener():
    logging.info(f"Listening on {ws_switch}")

async def listener():
    while True:
        try:
            async with websockets.connect(ws_switch) as websocket:
                logging.info(f"Connected to {ws_switch}. Listening for incoming payments.")
                make_idlescreen()
                response_str = await websocket.recv()
                print(response_str)
                response = response_str.split("-")
                pin = response[0]
                duration = int(response[1])
                # Check for a comment
                global comment
                try:
                    response[2]
                except IndexError:
                    comment = ""
                    logging.debug("No comment submitted.")
                else:
                    comment = response[2]
                logging.debug(f"Incoming message: {response}")
                amount = get_payments()
                initialize()
                make_success_overlay()
                pulse(pin, duration)
                logging.debug(f"Waiting {suceess_screen_expiry}s")
                sleep(suceess_screen_expiry)
                make_confirmation_screen(amount, comment)
                logging.debug(f"Waiting {suceess_screen_expiry}s")
                sleep(suceess_screen_expiry)
        except websockets.exceptions.ConnectionClosed as e:
            logging.debug(f"Connection closed: {e}")
            initialize()
            make_errorscreen()
            sleep(suceess_screen_expiry)
        except websockets.exceptions.InvalidStatus as e:
            logging.debug(f"Failed to make connection: {e}")
            initialize()
            make_errorscreen()
            sleep(suceess_screen_expiry)
        except asyncio.CancelledError:
            shutdown()