import requests
import json
from discord.ext import commands

token = input("Enter your token here: ")

url = 'https://discord.com/api/v9/users/@me/settings'

res = requests.patch(url, data=json.dumps({"custom_status":{"text":"glock is hot","emoji_name":"😈"}}), headers={"authorization": token, "content-type": "application/json"})

print(res.text)