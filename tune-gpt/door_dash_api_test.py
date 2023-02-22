"""
DOOR DASH API
"""
import os
import openai
from dotenv import load_dotenv
from pprint import pprint
import jwt.utils
import time
import math

load_dotenv()  # take environment variables from .env.
accessKey = {
    "developer_id": os.getenv("DOOR_DASH_DEVOPER_ID"),
    "key_id": os.getenv("DOOR_DASH_KEY_ID"),
    "signing_secret": os.getenv("DOOR_DASH_SIGNING_SECRET")
}
token = jwt.encode(
    {
        "aud": "doordash",
        "iss": accessKey["developer_id"],
        "kid": accessKey["key_id"],
        "exp": str(math.floor(time.time() + 60)),
        "iat": str(math.floor(time.time())),
    },
    jwt.utils.base64url_decode(accessKey["signing_secret"]),
    algorithm="HS256",
    headers={"dd-ver": "DD-JWT-V1"})

print(token)
