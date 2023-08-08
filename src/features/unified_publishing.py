```python
from src.social_media import facebook_integration, instagram_integration, twitter_integration
from src.user_interface import preview_post
from src.backend import PostSchema, post_data

def publish_post(post_data):
    """
    Function to publish posts on Facebook, Instagram, and Twitter simultaneously.
    """
    # Validate post data
    post_schema = PostSchema()
    errors = post_schema.validate(post_data)
    if errors:
        raise ValueError(errors)

    # Preview the post
    preview = preview_post(post_data)
    print(f"Post Preview: {preview}")

    # Publish the post
    facebook_integration.publish_post(post_data)
    instagram_integration.publish_post(post_data)
    twitter_integration.publish_post(post_data)

    print("Post published successfully on all platforms.")
    return True
```