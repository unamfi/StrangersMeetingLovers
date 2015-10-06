import tweepy
from secrets import *
import time
from time import gmtime, strftime
import datetime
import pickle

def authenticateBot():
	auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
	auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
	api = tweepy.API(auth)
	return api,auth


def gettweetIDs(screen_name,api,idsToFind):
   
    alltweets = []
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1
    tweetsFound={}
     
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        for t in new_tweets:
        	print "Tweeter:"+str(t.id)
        	return "meow"
        	tStringID=str(t.id)
        	if tStringID in idsToFind:
        		print "FOUDN IT"
        		tweetsFound[tStringID]=t.text



        	#for t2 in idsToFind:
        	#	print ""
        	#if idToFind==t.id:
        	#	print "FOUDN IT"
        	#	print t.text
        	#	return t.text

        return tweetsFound
        alltweets.extend(new_tweets)
         
        oldest = alltweets[-1].id - 1
         
 
 
        print "...%s tweets downloaded so far" % (len(alltweets))
     
    
    return  "Nothing!:("

def get_all_tweets(screen_name,api):
    #directorio="timelinePoliticos/"
    #Twitter only allows access to a users most recent 3240 tweets with this method
     
    #authorize twitter, initialize tweepy
    #auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    #auth.set_access_token(access_token_key, access_token_secret)
    #api = tweepy.API(auth)
     
    #initialize a list to hold all the tweepy Tweets
    alltweets = []
     
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
     
    #save most recent tweets
    alltweets.extend(new_tweets)
     
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
     
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)
         
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
         
        #save most recent tweets
        alltweets.extend(new_tweets)
         
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
         
 
 
        print "...%s tweets downloaded so far" % (len(alltweets))
     
    #transform the tweepy tweets into a 2D array that will populate the csv 
    outtweets = [[tweet.id_str, tweet.created_at, tweet.source, tweet.text.encode("utf-8")] for tweet in alltweets]
     
    #write the csv  
    #with open(directorio+'%s_tweets.csv' % screen_name, 'wb') as f:
    #    writer = csv.writer(f)
    #    writer.writerow(["id","created_at", "source", "text"])
    #    writer.writerows(outtweets)
     
    #pass
    print "Collected:"+str(len(alltweets))
    

    pickle.dump(alltweets, open("alltweets_"+str(screen_name)+".p", "wb"))
    #screen_name,api
    return  alltweets


def  getPeopleWhoReply(screen_name):
	
	api,auth=authenticateBot()
	peopleWhoReplied={}
	peopleWhoRepliedText={}
	peopleWhoRepliedIDs={}
	mentions = api.mentions_timeline()
	for mention in mentions:
		#print mention.text
		#break
		personID=mention.user.id
		person=mention.user.screen_name
		print person
		text=mention.text
		peopleWhoReplied.setdefault(str(person),0)
		peopleWhoRepliedText.setdefault(str(person),[])
		peopleWhoRepliedText[str(person)].append(text)
		peopleWhoReplied[str(person)]+=1
		peopleWhoRepliedIDs[personID]=0
	print len(peopleWhoReplied)
	date=datetime.datetime.now()

	pickle.dump(peopleWhoReplied, open("peopleWhoReplied_"+str(screen_name)+".p", "wb"))
	pickle.dump(peopleWhoRepliedIDs, open("peopleWhoRepliedIDs_"+str(screen_name)+".p", "wb"))
	pickle.dump(peopleWhoRepliedText, open("peopleWhoRepliedText_"+str(screen_name)+".p", "wb"))
	#pickle.dump(peopleWhoReplied, open("peopleWhoReplied_"+str(screen_name)+"_"+str(date)+".p", "wb"))
	#pickle.dump(peopleWhoRepliedIDs, open("peopleWhoRepliedIDs_"+str(screen_name)+"_"+str(date)+".p", "wb"))
	#pickle.dump(peopleWhoRepliedText, open("peopleWhoRepliedText_"+str(screen_name)+"_"+str(date)+".p", "wb"))

def getMentionsStored(screen_name):
	peopleWhoRepliedText=pickle.load(open("peopleWhoRepliedText_"+str(screen_name)+".p", "rb"))
	for p in peopleWhoRepliedText:
		print p
		posts=peopleWhoRepliedText[p]
		for p in posts:
			print p
def getNames(text):
	names={}

	words=text.split()
	for w in words:
		if "@" in w:
			names.setdefault(w,0)
			names[w]+=1
	return names


def getTweetsWithText(tweets):
	cleanTweets={}
	for t in tweets:
		if not t==None:
			if not t=="":
				
				cleanTweets[str(t)]=0
	return cleanTweets


		#			gettweetID(p,api,t)
		#			break
	#pass
	#for page in tweepy.Cursor(api.user_timeline, id="253346744").pages(1):
    #for item in page:
     #       if item.in_reply_to_user_id_str == "151791801":
      #          print item.text
       #         a = api.get_status(item.in_reply_to_status_id_str)
        #        print a.text

def getTextPeoppleWhoReply(screen_name):
	api,auth=authenticateBot()
	peopleWhoReplied=pickle.load(open("peopleWhoRepliedTweets_"+str(screen_name)+".p", "rb"))
	print len(peopleWhoReplied)
	for p in peopleWhoReplied:
		#print p
		tweets=peopleWhoReplied[p]
		cleanTweets=getTweetsWithText(tweets)
		#gettweetIDs(p,api,tweets)
		value=gettweetIDs(p,api,cleanTweets)
		print "Found this many:"+str(len(value))
		print value

		#print value
		#for t in cleanTweets:
		#	print t
		#	break
		break
		#gettweetID(p,api,tweets)
		#for t in tweets:
		#	if not t==None:
		#		if not t=="":
		#			print p+","+str(t)
		#			gettweetID(p,api,t)
		#			break
		#break
					#gettweetID(p,api,t)

def getRepliesBot(screen_name):
	peopleWhoReplied={}
	alltweets=pickle.load(open("alltweets_"+str(screen_name)+".p", "rb"))
	for t in alltweets:
		#print t.text
		#print t
		replyTweetID=t.in_reply_to_status_id_str
		#break
		if len(t.entities["user_mentions"])>0:
			#print len(t.entities["user_mentions"])
			#print t.entities["user_mentions"][0]
			user=t.entities["user_mentions"][0]["screen_name"]
			peopleWhoReplied.setdefault(user,[])
			peopleWhoReplied[user].append(replyTweetID)
			#print user

	
	pickle.dump(peopleWhoReplied, open("peopleWhoRepliedTweets_"+str(screen_name)+".p", "wb"))

#screen_name="MujeresFemBot"
#getMentionsStored(screen_name)
#getPeopleWhoReply(screen_name)
#api,auth=authenticateBot()
screen_name="Mujeres__Fem"
getRepliesBot(screen_name)
getTextPeoppleWhoReply(screen_name)

#getMentionsStored(screen_name)
#get_all_tweets(screen_name,api)
#getPeopleWhoReply(screen_name)



	#print len(peopleWhoReplied)
	#pickle.dump(peopleWhoReplied, open("peopleWhoReplied_"+str(screen_name)+".p", "wb"))
	#pickle.dump(peopleWhoRepliedIDs, open("peopleWhoRepliedIDs_"+str(screen_name)+".p", "wb"))