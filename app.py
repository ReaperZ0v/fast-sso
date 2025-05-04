from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
import requests
from jose import jwt
from dotenv import load_dotenv
import os 

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

load_dotenv()

# for the routes, make the user be able to import route and add it to their project via add_router
# user should be able to set their google client_id, secret and redirect uri

GOOGLE_CLIENT_ID = os.environ['GOOGLE_CLIENT_ID']
GOOGLE_CLIENT_SECRET = os.environ['GOOGLE_CLIENT_SECRET']
GOOGLE_REDIRECT_URI = os.environ['GOOGLE_REDIRECT_URI']


@app.get("/login/google")
async def login_google():
    return {
        "url": f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={GOOGLE_CLIENT_ID}&redirect_uri={GOOGLE_REDIRECT_URI}&scope=openid%20profile%20email%20https://www.googleapis.com/auth/gmail.readonly&access_type=offline"
    }

@app.get("/auth/google")
async def auth_google(code: str):
    # Exchange the authorization code for an access token
    token_url = "https://accounts.google.com/o/oauth2/token"
    data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    response = requests.post(token_url, data=data)
    tokens = response.json()
    access_token = tokens.get("access_token")

    # Fetch user info
    user_info = requests.get(
        "https://www.googleapis.com/oauth2/v1/userinfo",
        headers={"Authorization": f"Bearer {access_token}"}
    )

    # Fetch user's Gmail messages
    gmail_messages = requests.get(
        "https://www.googleapis.com/gmail/v1/users/me/messages",
        headers={"Authorization": f"Bearer {access_token}"}
    )

    # from here make a background task to extract all emails by thread ID

    return {
        "user_info": user_info.json(),
        "gmail_messages": gmail_messages.json()  # List of message IDs
    }

@app.get("/token")
async def get_token(token: str = Depends(oauth2_scheme)):
    return jwt.decode(token, GOOGLE_CLIENT_SECRET, algorithms=["HS256"])

