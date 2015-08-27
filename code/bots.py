import tweepy
from secrets import *

def authenticateBot():
	auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
	auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
	api = tweepy.API(auth)
	return api

def setMessage(api,message):
	api.update_status(status=message)
	print "Tweeting!"




api=authenticateBot()
message="Together we can improve the knowledge of the world!"
setMessage(api,message)
