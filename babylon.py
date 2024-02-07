import http.client
import sys
import json
from http.client import HTTPSConnection

user = sys.argv[1] #discord user
token = sys.argv[2] #token
message = "!faucet " + sys.argv[3] #wallet

server = "1046686458070700112"
channel = "1075371070493831259"

header_data = {
    "content-type": "application/json",
    "user-id": "{user}",
    "authorization": f"{token}",
    "host": "discordapp.com",
    "referrer": "https://discord.com/channels/{server}/{channel}"
}

message_data = json.dumps({"content": message})

def get_connection():
    return HTTPSConnection("discordapp.com", 443)

def send_message(conn, channel_id, message_data):
    try:
        conn.request("POST", f"/api/v6/channels/{channel_id}/messages", message_data, header_data)
        resp = conn.getresponse()
        if 199 < resp.status < 300:
            print("Message sent!")
    except Exception as e:
        print(f"Error sending message: {e}")

conn = get_connection()
send_message(conn, channel , message_data)
conn.close()
