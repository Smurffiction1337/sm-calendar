```python
import pandas as pd
from src.social_media import facebook_integration, instagram_integration, twitter_integration

class AdvancedAnalyticsDashboard:
    def __init__(self):
        self.analytics_data = None

    def fetch_analytics_data(self):
        facebook_data = facebook_integration.get_analytics_data()
        instagram_data = instagram_integration.get_analytics_data()
        twitter_data = twitter_integration.get_analytics_data()

        self.analytics_data = pd.concat([facebook_data, instagram_data, twitter_data], ignore_index=True)

    def get_post_performance(self):
        post_performance = self.analytics_data.groupby('post_id').agg({'engagement': 'sum', 'reach': 'sum'})
        return post_performance

    def get_engagement_metrics(self):
        engagement_metrics = self.analytics_data.groupby('platform').agg({'likes': 'sum', 'comments': 'sum', 'shares': 'sum'})
        return engagement_metrics

    def get_audience_demographics(self):
        audience_demographics = self.analytics_data.groupby('platform').agg({'age': 'mean', 'gender': 'value_counts'})
        return audience_demographics

    def get_platform_specific_metrics(self, platform):
        platform_metrics = self.analytics_data[self.analytics_data['platform'] == platform]
        return platform_metrics

    def get_overall_performance_metric(self):
        overall_performance = self.analytics_data.agg({'engagement': 'sum', 'reach': 'sum'})
        return overall_performance

    def update_analytics(self):
        self.fetch_analytics_data()
        print('Analytics updated successfully.')

advanced_analytics_dashboard = AdvancedAnalyticsDashboard()
```