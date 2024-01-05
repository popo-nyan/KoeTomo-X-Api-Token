import httpx
import hashlib


def get_api_token():
    response = httpx.request(method="GET", url="https://koetomo-bb8bb.firebaseio.com/api/api_token.json")
    return hashlib.sha256(str(response.json() + "KoeTomo").encode()).hexdigest()


if __name__ == "__main__":
    print(get_api_token())
