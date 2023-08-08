```python
import random
from src.social_media.facebook_integration import FacebookAPI
from src.social_media.instagram_integration import InstagramAPI
from src.social_media.twitter_integration import TwitterAPI

class RandomWinnerSelection:
    def __init__(self, user_credentials):
        self.facebook_api = FacebookAPI(user_credentials['facebook'])
        self.instagram_api = InstagramAPI(user_credentials['instagram'])
        self.twitter_api = TwitterAPI(user_credentials['twitter'])

    def select_winner(self, platform, condition):
        if platform == 'facebook':
            return self.select_facebook_winner(condition)
        elif platform == 'instagram':
            return self.select_instagram_winner(condition)
        elif platform == 'twitter':
            return self.select_twitter_winner(condition)
        else:
            raise ValueError("Invalid platform. Choose from 'facebook', 'instagram', or 'twitter'.")

    def select_facebook_winner(self, condition):
        users = self.facebook_api.get_users(condition)
        winner = random.choice(users)
        return winner

    def select_instagram_winner(self, condition):
        users = self.instagram_api.get_users(condition)
        winner = random.choice(users)
        return winner

    def select_twitter_winner(self, condition):
        users = self.twitter_api.get_users(condition)
        winner = random.choice(users)
        return winner
```