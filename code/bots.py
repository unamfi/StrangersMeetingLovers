import tweepy
from secrets import *
import time
from time import gmtime, strftime
import datetime

currentTeams={}
teamsRecruited={}

def authenticateBot():
	auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
	auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
	api = tweepy.API(auth)
	return api,auth

def setMessage(api,message):
	api.update_status(status=message)
	print "Tweeting!"


def prepareDataIncomingMessage(status):
    
    typeQuestion="None"
    year=strftime("%Y", gmtime())
    month=strftime("%m", gmtime())
    day=strftime("%d", gmtime())
    hour=strftime("%H", gmtime())
    minute=strftime("%M", gmtime())
    sec=strftime("%S", gmtime())
            
    date= datetime.datetime(int(year),int(month),int(day),int(hour),int(minute),int(sec) )
    status.created_at = date
    screen_name=status.user.screen_name
    screen_name=screen_name.lower()
    message=status.text
    idTweet=status.id_str
    return date,status,screen_name,message,idTweet



class StdOutListener(tweepy.StreamListener):

	global currentTeams
	global teamsRecruited

    ''' Handles data received from the stream. '''
 
    def on_status(self, status):
        # Prints the text of the tweet
        print('Tweet text: ' + status.text)
        date,status,screen_name,message,idTweet=prepareDataIncomingMessage(status)
        print "User:"+str(screen_name)
        if len(currentTeams)<3:
        	currentTeams.setdefault(screen_name,0)
        	currentTeams[screen_name]+=1

        else:
        	print "Got everybody, ready to recruit!"

 
        # There are many options in the status object,
        # hashtags can be very easily accessed.
        
        #for hashtag in status.entries['hashtags']:
         #   print(hashtag['text'])
 
        return True
 
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening
 
    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening

#api=authenticateBot()
#message="Together we can improve the knowledge of the world!"
#setMessage(api,message)
print "time"
l = StdOutListener()
api,auth=authenticateBot()
stream = tweepy.Stream(auth, l)

publicKeyWords = ['UNAM']
stream.filter(track=publicKeyWords)
