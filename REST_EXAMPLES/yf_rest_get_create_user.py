import yf_auth
import time
import requests
import json

YF_BASE_URL = "http://localhost:8081"
yf_auth.is_yf_running(YF_BASE_URL)
REFRESH_TOKEN = yf_auth.get_refresh_token(YF_BASE_URL)
ACCESS_TOKEN = yf_auth.get_access_token(YF_BASE_URL, REFRESH_TOKEN)

millis = int(round(time.time() * 1000))

headers = {
    "Accept": "application/vnd.yellowfin.api-v1+json",
    "Authorization": f"YELLOWFIN ts={millis}, nonce=random, token={ACCESS_TOKEN}",
    "Content-Type": "application/json",
}


GET_USER_URL = f"{YF_BASE_URL}/api/users/5"
r = requests.get(url=GET_USER_URL, headers=headers)
print(r.text)
