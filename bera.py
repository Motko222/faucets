import requests
import capsolver
import sys
import os
#print("proxy: ",sys.argv[1]," address:",sys.argv[2] )

# Proxy configuration
PROXIES = {"http": sys.argv[1], "https": sys.argv[1]}
address = sys.argv[2]

#print(PROXIES)
#print(address)

def get_captcha():
    capsolver.api_key = sys.argv[3]  # capsolver.com
    capsolver_data = {
        "type": "ReCaptchaV3TaskProxyLess",
        "websiteURL": "https://artio.faucet.berachain.com/",
        "websiteKey": "6LfOA04pAAAAAL9ttkwIz40hC63_7IsaU2MgcwVH",
        "pageAction": 'submit'
    }
    solution = capsolver.solve(capsolver_data)
    return solution['gRecaptchaResponse']


token = get_captcha()
#print(token)

def get_token(address):
    url = f"https://artio-80085-ts-faucet-api-2.berachain.com/api/claim?address={address}"
    headers = {
        "Host": "artio-80085-ts-faucet-api-2.berachain.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://artio.faucet.berachain.com/",
        "Authorization": f"Bearer {token}",
        "Content-Type": "text/plain;charset=UTF-8",
        "Content-Length": "56",
        "Origin": "https://artio.faucet.berachain.com",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "TE": "trailers",
    }

    data = {"address": address}

    response = requests.post(url, json=data, headers=headers, proxies=PROXIES)
#    response = requests.post(url, json=data, headers=headers)

    print(response.status_code, response.text)


get_token(address)
