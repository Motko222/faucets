import requests
import capsolver
import sys
import os

# Proxy configuration
PROXIES = {"http": sys.argv[1], "https": sys.argv[1]}
address = sys.argv[2]

def get_captcha():
    capsolver.api_key = sys.argv[3]  # capsolver.com
    capsolver_data = {
        "type": "HCaptchaTaskProxyLess",
        "websiteURL": "https://faucet.0g.ai/api/faucet",
        "websiteKey": "",
    }
    solution = capsolver.solve(capsolver_data)
    return solution['gRecaptchaResponse']


token = get_captcha()

def get_token(address):
    url = f"https://faucet.0g.ai/api/faucet"
    headers = {
        "Host": "faucet.0g.ai/api/faucet",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Referer": "https://faucet.0g.ai/",
        "Content-Type": "text/plain;charset=UTF-8",
        "Content-Length": "1919",
        "Origin": "https://faucet.0g.ai",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site"
    }

    data = {"address": address, "hcaptchaToken": token}
    print(token)
    response = requests.post(url, json=data, headers=headers, proxies=PROXIES)
#    response = requests.post(url, json=data, headers=headers)
    print(response.status_code, response.text)

get_token(address)
