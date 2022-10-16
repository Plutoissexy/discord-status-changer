import requests
import json
from discord.ext import commands

token = input("Enter your token here: ")
text = input("Enter the text for your status: ")
emoji = input("Enter in emoji format your emoji: ")

url = 'https://discord.com/api/v9/users/@me/settings'

res = requests.patch(url, data=json.dumps({"custom_status":{"text":f"{text}","emoji_name":f"{emoji}"}}), headers={"authorization": token, "content-type": "application/json"})

print(res.text)
