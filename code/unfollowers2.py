import tweepy
from secrets import *
import time
from time import gmtime, strftime
import datetime
import pickle

print "hello"



def authenticateBot():
	auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
	auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
	api = tweepy.API(auth)
	return api,auth


def getPeopleToFollow(api):
	for follower in tweepy.Cursor(api.followers).items():
		follower.follow()
		print follower.screen_name

def unFollowSuckers(SCREEN_NAME):
	print SCREEN_NAME
	auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
	auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
	api = tweepy.API(auth)
	followers = api.followers_ids(SCREEN_NAME)
	friends = api.friends_ids(SCREEN_NAME)
	latestPeopleAlreadyFollowed=pickle.load(open("latestPeopleAlreadyFollowed_"+SCREEN_NAME+".p","rb"))
 	print "Num followers:"+str(len(followers))
 	print "Num freid:"+str(len(followers))
	for f in friends:
		if f not in followers:
			print "Unfollow {0}?".format(api.get_user(f).screen_name)
			#if raw_input("Y/N?") == 'y' or 'Y':
			#
			latestPeopleAlreadyFollowed[f]=0
			pickle.dump(latestPeopleAlreadyFollowed, open("latestPeopleAlreadyFollowed_"+SCREEN_NAME+".p", "wb"))
			api.destroy_friendship(f)

#l = StdOutListener()
SCREEN_NAME="MujeresFemBot"
api,auth=authenticateBot()
getPeopleToFollow(api)
#unFollowSuckers(SCREEN_NAME)
#stream = tweepy.Stream(auth, l)

#publicKeyWords = ['feminismo']
#stream.filter(track=publicKeyWords)