```python
import requests
from src.backend import UserSchema

class InstagramIntegration:
    def __init__(self, user_credentials):
        self.user_credentials = user_credentials
        self.base_url = "https://graph.instagram.com/"

    def authenticate(self):
        url = f"{self.base_url}oauth/access_token"
        payload = {
            "client_id": self.user_credentials['instagram']['client_id'],
            "client_secret": self.user_credentials['instagram']['client_secret'],
            "grant_type": "authorization_code",
            "redirect_uri": "https://localhost",
            "code": self.user_credentials['instagram']['code']
        }
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            self.user_credentials['instagram']['access_token'] = response.json()['access_token']
            return True
        else:
            return False

    def get_posts(self):
        url = f"{self.base_url}{self.user_credentials['instagram']['user_id']}/media?access_token={self.user_credentials['instagram']['access_token']}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['data']
        else:
            return []

    def post_content(self, post_data):
        url = f"{self.base_url}{self.user_credentials['instagram']['user_id']}/media?access_token={self.user_credentials['instagram']['access_token']}"
        payload = {
            "image_url": post_data['image_url'],
            "caption": post_data['caption']
        }
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            return True
        else:
            return False

    def get_comments(self, post_id):
        url = f"{self.base_url}{post_id}/comments?access_token={self.user_credentials['instagram']['access_token']}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['data']
        else:
            return []

    def post_comment(self, post_id, comment_data):
        url = f"{self.base_url}{post_id}/comments?access_token={self.user_credentials['instagram']['access_token']}"
        payload = {
            "message": comment_data['message']
        }
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            return True
        else:
            return False

    def get_messages(self):
        # Instagram API does not support fetching of private messages
        return []

    def send_message(self, recipient_id, message_data):
        # Instagram API does not support sending of private messages
        return False
```