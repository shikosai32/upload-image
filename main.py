import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

URL = os.environ["URL"]
TOKEN = os.environ["TOKEN"]

sys.stdout.write("ファイル名を入力してください: ")
file_name = input().strip()

res = requests.post(
        f"{URL}/{file_name}",
        headers = {
            "token": TOKEN
        },
        files = {
            "file": (f"{file_name}.png", open(f"tmp/{file_name}.png", "rb").read(), "image/png")
        }
    )

print(res, res.text)
