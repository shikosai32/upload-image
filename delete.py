import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

URL = os.environ["URL"]
TOKEN = os.environ["TOKEN"]

sys.stdout.write("ファイル名を入力してください: ")
file_name = input().strip()

res = requests.delete(
        f"{URL}/{file_name}",
        headers = {
            "token": TOKEN
        }
    )

print(res, res.text)
