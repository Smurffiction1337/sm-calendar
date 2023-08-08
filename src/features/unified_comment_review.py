```python
from src.social_media import facebook_integration, instagram_integration, twitter_integration

class UnifiedCommentReview:
    def __init__(self):
        self.comment_data = []
        self.comment_dashboard = None

    def fetch_comments(self):
        facebook_comments = facebook_integration.get_comments()
        instagram_comments = instagram_integration.get_comments()
        twitter_comments = twitter_integration.get_comments()

        self.comment_data = facebook_comments + instagram_comments + twitter_comments

    def display_comments(self):
        self.comment_dashboard = self.comment_data

    def review_comment(self, comment_id, response):
        for comment in self.comment_data:
            if comment['id'] == comment_id:
                comment['response'] = response
                if comment['platform'] == 'facebook':
                    facebook_integration.post_comment_response(comment_id, response)
                elif comment['platform'] == 'instagram':
                    instagram_integration.post_comment_response(comment_id, response)
                elif comment['platform'] == 'twitter':
                    twitter_integration.post_comment_response(comment_id, response)
                break

    def update_comment_dashboard(self):
        self.fetch_comments()
        self.display_comments()
```