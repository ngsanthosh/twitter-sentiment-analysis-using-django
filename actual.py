import re
import tweepy
from textblob import TextBlob
from tweepy import OAuthHandler
import sys 

consumer_key = 'SEanXsZv5LC2C5gU9Jd4pT0EZ' #I am providing my API Credentials, hope you won't misuse it!
consumer_secret = 'bW39EDCGlTHEK59mJPS5P9JnpZ98OJBR9KeFgie5kKw1fvKzln'
access_token = '1142102037703712769-qlPw2BSu1b8vr4LKK06I9NC9y9JL7n'
access_token_secret = 'gv1vBXPrzULMHzsUfpaf9p2kZ102ieF0CBzYnfalkqZ64'

try:
    auth=OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api=tweepy.API(auth)
except:
    print("Huh., Authetication failed -- From Twitter")


a=sys.argv[1]
tweets=api.search(a)
for tweet in tweets:
    print(tweet.text)
    



analysis=TextBlob(tweet.text)

print(analysis.sentiment)
print(analysis.sentiment.polarity)
