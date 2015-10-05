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
	#latestPeopleAlreadyFollowed={}
 	print "Num followers:"+str(len(followers))
 	print "Num freid:"+str(len(followers))
	for f in friends:
		if f not in followers:
			print "Unfollow {0}?".format(api.get_user(f).screen_name)
			#if raw_input("Y/N?") == 'y' or 'Y':
			userName=api.get_user(f).screen_name
			latestPeopleAlreadyFollowed[userName]=0
			pickle.dump(latestPeopleAlreadyFollowed, open("latestPeopleAlreadyFollowed_"+SCREEN_NAME+".p", "wb"))
			api.destroy_friendship(f)
	FILE=open("peopleOnceFollowed_"+SCREEN_NAME+".csv",'w')
	for p in latestPeopleAlreadyFollowed:
		FILE.write(str(p)+"\n")
	FILE.close()

#l = StdOutListener()
#Mujeres__Fem
#SCREEN_NAME="MujeresFemBot"
SCREEN_NAME="Mujeres__Fem"
unFollowSuckers(SCREEN_NAME)
latestPeopleAlreadyFollowed=pickle.load(open("latestPeopleAlreadyFollowed_"+SCREEN_NAME+".p", "rb"))
FILE=open("peopleOnceFollowed_"+SCREEN_NAME+".csv",'w')
for p in latestPeopleAlreadyFollowed:
	FILE.write(str(p)+"\n")
FILE.close()
#unFollowSuckers(SCREEN_NAME)



#api,auth=authenticateBot()
#getPeopleToFollow(api)
#unFollowSuckers(SCREEN_NAME)
#stream = tweepy.Stream(auth, l)

#publicKeyWords = ['feminismo']
#stream.filter(track=publicKeyWords)