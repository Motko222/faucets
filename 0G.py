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
        "websiteURL": "https://faucet.0g.ai",
        "websiteKey": "06ee6b5b-ef03-4491-b8ea-01fb5a80256f",
    }
    solution = capsolver.solve(capsolver_data)
    return solution['gRecaptchaResponse']


token = get_captcha()

def get_token(address):
    url = f"https://faucet.0g.ai/api/faucet"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "sk-SK,sk;q=0.9,cs;q=0.8,en-US;q=0.7,en;q=0.6",
        "Content-Length": "2265",
        "Content-Type": "text/plain;charset=UTF-8",
        "Origin": "https://faucet.0g.ai",
        "Priority": "u=1, i",
        "Referer": "https://faucet.0g.ai/",
        "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "Windows",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }

    data = {"address": address, "hcaptchaToken": token}
#    print(token)
    response = requests.post(url, json=data, headers=headers, proxies=PROXIES)
#    response = requests.post(url, json=data, headers=headers)
    print(response.status_code, response.text)

get_token(address)
