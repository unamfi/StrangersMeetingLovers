import tweepy
from secrets import *
import time
from time import gmtime, strftime
import datetime
import pickle
import time 

currentTeams2={}
teamsRecruited={}
teamsRecruitedFinal={}
peopleRecruited={}



botTransScreenName={}
botTransScreenName["bot"]="MujeresFemBot"
botTransScreenName["cause"]="Mujeres__Fem"


botKeyInfo={}
botKeyInfo["Mujeres__Fem"]={}
botKeyInfo["Mujeres__Fem"]["C_KEY"]="VQmFOYXWmEbhbzOE8cpeTg8Rr"
botKeyInfo["Mujeres__Fem"]["C_SECRET"]="VQmFOYXWmEbhbzOE8cpeTg8Rr"
botKeyInfo["Mujeres__Fem"]["A_TOKEN"]="VQmFOYXWmEbhbzOE8cpeTg8Rr"
botKeyInfo["Mujeres__Fem"]["A_TOKEN_SECRET"]="VQmFOYXWmEbhbzOE8cpeTg8Rr"


#C_KEY = "T48gHlgfSgEFuOS76N2gy7bj9"  
#C_SECRET = "7ntJ1xPdSxTjR2bvKVMO0flCvn0xM9AHrhg0DzY77iGnbB6Rzw"  
#A_TOKEN = "3754637839-BcqriLQ0xS9EJzqzkz5KKZg94lsGmY8kqS2S6Rb"  
#A_TOKEN_SECRET = "sI9YoXx6zqOdlOFgyhPTVKZ7hgqAPGwNza1FKAdyJL1pt" 

botKeyInfo["MujeresFemBot"]={}
botKeyInfo["MujeresFemBot"]["C_KEY"]="T48gHlgfSgEFuOS76N2gy7bj9"
botKeyInfo["MujeresFemBot"]["C_SECRET"]="7ntJ1xPdSxTjR2bvKVMO0flCvn0xM9AHrhg0DzY77iGnbB6Rzw"
botKeyInfo["MujeresFemBot"]["A_TOKEN"]="3754637839-BcqriLQ0xS9EJzqzkz5KKZg94lsGmY8kqS2S6Rb"
botKeyInfo["MujeresFemBot"]["A_TOKEN_SECRET"]="sI9YoXx6zqOdlOFgyhPTVKZ7hgqAPGwNza1FKAdyJL1pt"









def authenticateBot():
    global currentBot
    screen_name=botTransScreenName[currentBot]
    C_KEY=botKeyInfo[screen_name]["C_KEY"]
    C_SECRET=botKeyInfo[screen_name]["C_SECRET"]
    A_TOKEN=botKeyInfo[screen_name]["A_TOKEN"]
    A_TOKEN_SECRET=botKeyInfo[screen_name]["A_TOKEN_SECRET"]

    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
    api = tweepy.API(auth)
    return api,auth

def setMessage(api,message):
	api.update_status(status=message)
	#print "Tweeting!"


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

def prepareNameString(currentTeams):
    #print "enter prepareNameString"
    names=""
    for n in currentTeams:
        print n
        names+="@"+str(n)
        names+=" "
    #print "returning Names:"+str(names)
    return names

def prepareRecruitMessage(names,recruitMessage):
    tweet=names+recruitMessage
   # print "LEN TWEET:"+str(len(tweet))
    if len(tweet)<140:
        return tweet,True
    else:
        return tweet,False


class StdOutListener(tweepy.StreamListener):

    global currentTeams2
    global teamsRecruited
    global api

    #''' Handles data received from the stream. '''
 
    def on_status(self, status):
        global currentTeams2
        global teamsRecruited
        global api
        
        #print('Tweet text: ' + status.text)
        date,status,screen_name,message,idTweet=prepareDataIncomingMessage(status)
       # print "User:"+str(screen_name)
        if len(currentTeams2)<2:
            if not screen_name in peopleRecruited:
                #print "Les than 3"
                currentTeams2.setdefault(screen_name,0)
                currentTeams2[screen_name]+=1
                #print "Current Teams:"+str(currentTeams2)

        else:
            #print "Listo Reclutar!!"
            names=prepareNameString(currentTeams2)
            #print "back from names!"
            recruitMessage="Busco cambiar Wikipedia cubriendo mas mujeres! Que Gran Mujer deberia tener Wiki que no tenga ahorita?"
            tweet,canPostIt=prepareRecruitMessage(names,recruitMessage)
            #print "Will almost post this!:"+str(tweet)
            #print "I can post? "+str(canPostIt)
            if canPostIt:
            
                namesClean=names
                namesClean.replace("@","")
                namesClean=sorted(namesClean.split(), key=str.lower)
                keyNames=str(namesClean)
                if not keyNames in teamsRecruitedFinal:
                    teamsRecruitedFinal[keyNames]=tweet
                    #print "Ready to send Tweet!"
                    #print "People:"+names
                    #print "Tweets:"+tweet
                    setMessage(api,tweet)
                    pickle.dump(teamsRecruitedFinal, open("teamsRecruitedFinal.p", "wb"))
                    #pickle.dump(teamsRecruitedFinal,"teamsRecruited.p")
                    #print "SEND OUT TWEET"
                    for n in currentTeams2:
                        peopleRecruited.setdefault(n,0)
                    pickle.dump(peopleRecruited, open("peopleRecruited.p", "wb"))
                    
                    currentTeams2={}
                    time.sleep(60) 
            else:
                pass

           
 
        
 
        return True
 
    def on_error(self, status_code):
        #print('Got an error with status code: ' + str(status_code))
        return True # To continue listening
 
    def on_timeout(self):
        #print('Timeout...')
        return True # To continue listening

#api=authenticateBot()
#message="Together we can improve the knowledge of the world!"
#setMessage(api,message)
#print "time"
#a="@mary @nathan @gann"
#a.replace("@","")
#print sorted(a.split(), key=str.lower)
#pickle.dump(a,"a.p")
#pickle.dump(a, open("a.p", "wb"))


l = StdOutListener()
api,auth=authenticateBot()
stream = tweepy.Stream(auth, l)

publicKeyWords = ['feminismo']
stream.filter(track=publicKeyWords)

