import json
import requests
import time


def is_yf_running(yf_base_url):
    r = requests.get(url=f"{yf_base_url}/logonCheck.i4", verify=False)
    if r.status_code == 401:
        return True
    return False


def get_refresh_token(yf_base_url):
    millis = int(round(time.time() * 1000))

    headers = {
        "Authorization": f"YELLOWFIN ts={millis}, nonce=random",
        "Content-Type": "application/json",
        "Accept": "application/vnd.yellowfin.api-v1+json",
    }

    payload = json.dumps(
        {
            "userName": "",
            "password": "",
            "clientOrgRef": "default_org",
        }
    )

    refresh_token_url = f"{yf_base_url}/api/refresh-tokens"

    r = requests.request("POST", url=refresh_token_url, headers=headers, data=payload)
    r_dict = json.loads(r.text)
    return r_dict["securityToken"]


def get_access_token(yf_base_url, refresh_token):
    ACCESS_TOKEN_URL = f"{yf_base_url}/api/access-tokens"

    millis = int(round(time.time() * 1000))
    headers = {
        "Accept": "application/vnd.yellowfin.api-v1+json",
        "Authorization": f"YELLOWFIN ts={millis}, nonce=random, token={refresh_token}",
        "Content-Type": "application/json",
    }

    r = requests.post(url=ACCESS_TOKEN_URL, headers=headers)
    r_dict = json.loads(r.text)
    return r_dict["securityToken"]


if __name__ == "__main__":
    YF_BASE_URL = "http://localhost:8081"
    is_yf_running(YF_BASE_URL)
