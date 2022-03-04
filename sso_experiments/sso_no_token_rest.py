import requests
import time
import json

YF_BASE_URL = "http://localhost:9696"

# ## Make Sure YF Instance is up and running!


r = requests.get(url=f"{YF_BASE_URL}/logonCheck.i4", verify=False)
assert r.status_code == 401, "Hmm, I can't seem to access the instance. Is it running?"
print(f"{YF_BASE_URL} is up and running! 💪")


millis = time.time() * 1000

headers = {
    "Authorization": f"YELLOWFIN ts={millis}, nonce=random",
    "Content-Type": "application/json",
    "Accept": "application/vnd.yellowfin.api-v1+json",
}

payload = json.dumps(
    {
        "username": "",
        "password": "",
        "clientOrgRef": "default_org",
    }
)

response = requests.request("POST", YF_BASE_URL, headers=headers, data=payload)

print(response.text)
