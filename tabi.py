import requests
import capsolver
import sys
import os
 
# Proxy configuration
PROXIES = {"http": sys.argv[1], "https": sys.argv[1]}
address = sys.argv[2]

def get_token(address):
    url = f"https://faucet-api.testnet.tabichain.com/api/faucet"
    headers = {
        "Host": "faucet-api.testnet.tabichain.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Accept": "*/*",
        "Accept-Language": "en-GB,en;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://faucet.testnet.tabichain.com",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        "Content-Type": "application/json",
        "Content-Length": "56",
        "Origin": "https://faucet.testnet.tabichain.com",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Gpc": "1"
    }

    data = {"address": address}

    response = requests.post(url, json=data, headers=headers, proxies=PROXIES)
#    response = requests.post(url, json=data, headers=headers)
#    print(url)
#    print(data)
#    print(PROXIES)
#    print(headers)
    print(response.status_code, response.text)

get_token(address)
