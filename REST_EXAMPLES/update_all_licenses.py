import requests
import time
import json
import yf_auth

YF_BASE_URLS = [
]

for YF_BASE_URL in YF_BASE_URLS:
    if not yf_auth.is_yf_running(YF_BASE_URL):
        print(f"I had trouble connecting to {YF_BASE_URL}")
        continue

    REFRESH_TOKEN = yf_auth.get_refresh_token(YF_BASE_URL)
    ACCESS_TOKEN = yf_auth.get_access_token(YF_BASE_URL, REFRESH_TOKEN)
    LICENCE_PATH = ""

    UPLOAD_LICENSE_URL = f"{YF_BASE_URL}/api/rpc/licence-management/upload-licence"

    payload = {}

    with open(LICENCE_PATH, "rb") as license_file:

        files = [
            (
                "newLicence",
                (
                    "jsolly.lic",
                    license_file,
                    "application/octet-stream",
                ),
            )
        ]

        millis = int(round(time.time() * 1000))
        headers = {
            "Accept": "application/vnd.yellowfin.api-v1+json",
            "Authorization": f"YELLOWFIN ts={millis}, nonce=random, token={ACCESS_TOKEN}",
        }

        r = requests.request(
            "POST", url=UPLOAD_LICENSE_URL, headers=headers, data=payload, files=files
        )
        assert r.status_code == 200, f"That didn't work, I got this instead: {r.text}"
        print("License uploaded sucessfully ✅")
