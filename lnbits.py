# Modules
import logging
import requests

# Functions and variables
from var import ws_switch

#https://send.laisee.org/bitcoinswitch/api/v1/lnurl/{bitcoinswitch_id}
#wss://send.laisee.org/api/v1/ws/WB4kjkTtQRVWdSL7FeV6b3

#lnbits_server = "signet.laisee.org"
lnbits_server = "send.laisee.org"
url_base_switch = "https://" + lnbits_server + "/bitcoinswitch/api/v1"
url_base_payments = "https://" + lnbits_server + "/api/v1/payments"
#x_api_key = "235eb950955d40ee90998891a161a7db" #invoice key
x_api_key = "be3025cd178a46379c392f07f085c471" #admin key
#x_api_key = "80b5f93507b142f4a60bdb5e07eb79e6" #signet admin key

def params():
        params =	{"title": False,
                 	"wallet": wallet,
					"currency": "sat",
                	"switches": [
                  		{}
                  	],
                	"password": "string",
    				"disabled": false,
    				"disposable": true}
        logging.debug(f"Invoice parameters: {params}")
        return params

headers = {"X-Api-Key" : x_api_key,
           "Content-type" : "application/json"}

def get_switches():
	print(url_base)
	print(headers)
	switches = requests.get(url_base_switch, headers=headers)
	print(switches)
	print("WOHOO")

def get_lnurl():
	print(url_base)
	print(headers)
	#params = {"pin": 5}
	url = url_base + "/" + "WB4kjkTtQRVWdSL7FeV6b3"
	lnurl_request = requests.get(url, headers=headers)
	lnurl = lnurl_request.json()
	print(lnurl)
	print("WOHOO")

def get_payments():
	payments_request = requests.get(url_base_payments, headers=headers)
	payments = payments_request.json()
	#global amount
	amount = payments[0]['amount']/1000
	logging.info(f"Payment received: {amount} satoshi")
	return amount

#https://send.laisee.org/bitcoinswitch/api/v1/lnurl/{bitcoinswitch_id}
#https://send.laisee.org/bitcoinswitch/api/v1/public/{bitcoinswitch_id}

'''
1. Get list of Bitcoin Switches
2. Check if switch already exists (identified by name)
3. Register switch
4. Update switch
5. Retrieve LNURL
6. Listen to websockets

https://send.laisee.org/bitcoinswitch/api/v1
{

    "title": "string",
    "wallet": "string",
    "currency": "string",
    "switches": [
        {}
    ],
    "password": "string",
    "disabled": false,
    "disposable": true

}


https://send.laisee.org/bitcoinswitch/api/v1/{bitcoinswitch_id}
{

    "title": "string",
    "wallet": "string",
    "currency": "string",
    "switches": [
        {}
    ],
    "password": "string",
    "disabled": false,
    "disposable": true

}
'''