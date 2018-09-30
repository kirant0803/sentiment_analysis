from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s
print "importing sentiment_mod is done!!"

#consumer key, consumer secret, access token, access secret.
ckey="AnAXUJG4cdSNIQfBA27rSYaVV"
csecret="9PZcfR57YioHLumzwc1bvx9uBwsB9foEBTy4fGZsR3ChEWSXSy"
atoken="138676273-apJnX7MGcrYo9YuMJreze9quwKz2sP5sxgzPNn2x"
asecret="RcsLt4PO8kbAgGmkmi4JZSTmDjSOabKXeJYuKUUcChi2u"

class listener(StreamListener):

    def on_data(self, data):
    	#print data
    	all_data = json.loads(data)

    	tweet = all_data["text"]
    	# print tweet
    	sentiment_value, confidence = s.sentiment(tweet)
    	print tweet, sentiment_value, confidence

    	if confidence*100>= 80:
    		output = open("/Users/kiran/Desktop/Kiran/Data Science/TwitterAnalysis/tweets-out.txt","a")
    		output.write(sentiment_value)
    		output.write('\n')
    		output.close()
        return True


    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["asia cup"])