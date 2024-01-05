import httpx
import hashlib
import secrets
import string
import random


def get_api_token() -> str:
    api_token_response = httpx.request(method="GET", url="https://koetomo-bb8bb.firebaseio.com/api/api_token.json")
    return hashlib.sha256(str(api_token_response.json() + "KoeTomo").encode()).hexdigest()


response = httpx.request(method="POST",
                         url="https://api.meetscom.com/api/account/signup",
                         headers={
                             "Host": "api.meetscom.com",
                             "X-Api-Token": get_api_token(),
                             "Content-Type": "application/x-www-form-urlencoded",
                             "User-Agent": "okhttp/4.9.3"},
                         data={
                             "auth_token": "",
                             "version": "android_3.8.34",
                             "email": "".join([secrets.choice(string.ascii_letters + string.digits) for _ in range(15)]) + "@outlook.com",
                             "password": "".join(secrets.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(10)),
                             "name": "".join([random.choice(string.ascii_letters + string.ascii_uppercase) for _ in range(15)]),
                             "sex": random.choice(["1", "2"]),
                             "birthday": str(int(random.uniform(1970, 2001))) + "-" + str(int(random.uniform(1, 12))) + "-" + str(int(random.uniform(1, 28))),
                             "device_uid": secrets.token_hex(8)})
print(response, response.text)
