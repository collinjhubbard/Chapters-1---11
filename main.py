import tweepy

authenticator = tweepy.OAuth2BearerHandler("AAAAAAAAAAAAAAAAAAAAAGapnwEAAAAAc9VznYTTHLeWcC39QXlURCVsrqc%3Dz5avHJRcX1bJ6sgW4goYjWuzlABeVMra7ZAUeBYsWLY6JZz08m")
api = tweepy.API(authenticator)

#api_key = 'Immw1WyrXjS3ErFQQlucXAvPf'
#api_key_secret = 'jhF9S58bLTTjaguBPcnKFOGC51c65x2xqkTC5Znv7yDZdWJ7GN'
#access_token = '1664373890309664773-7zz453hLUIludiicwxl53YruaqX6Pf'
#access_token_secret = 'O34ANkjnS7Rd899OzJuHDFExfcBVab4t1U7dASt1qCY6r'
#bearer_token = 'AAAAAAAAAAAAAAAAAAAAAGapnwEAAAAA2Ad0PTGVUbbDQZIaGIXrukMyxAc%3DXefYTXV7T6q1LL55V4NTERhzp7IyHzjkDXDXleB3lQZSmqfVxz'

#authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
#authenticator.set_access_token(access_token, access_token_secret)

#client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAAGapnwEAAAAAc9VznYTTHLeWcC39QXlURCVsrqc%3Dz5avHJRcX1bJ6sgW4goYjWuzlABeVMra7ZAUeBYsWLY6JZz08m")
api = tweepy.API(authenticator, wait_on_rate_limit=True)

api.update_status_with_media(status="status update: chilling with python", filename='Detroit', file='C:\\Users\\colli\\Pictures\\Paradise&BlackBottom.jpg', possibly_sensitive=False)