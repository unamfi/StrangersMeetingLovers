import tweepy
import sys
import operator
reload(sys)
sys.setdefaultencoding("utf-8")

#MujeresFemBot
consumer_key = "U9BfrQUfq2ZYoUzguihU0vb1W"
consumer_secret = "44SvMoJhVolsaKvu1gyJStTnO7qwCOo95PHMYzsVw3HTCAvbXP"
access_token = "3754637839-oMtjXQaRm8X1Zh84O0vcgTqys4dNKTu94neEnVj"
access_token_secret = "SMwDSe95015Yk3C3rCB5sOJsdzGSv5PIMn0dEvSZhmBvG"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Mujeres__Fem
femconsumer_key = "gQBMwz0Wr7N7W1ktrH69qWgqs"
femconsumer_secret = "n06iH76oWL53jq26e4BZFjmArLUv5NCS7BaMANXsFmWZ7UMqU1"
femaccess_token = "3754491014-p9V41yXNgZ3fwdzlkhPqJzhjmRemcYJzzCYsyMT"
femaccess_token_secret = "PorWL4M8x2KvzooBu2TG7CPNOeT4L7aDoh8xFdY5zvoAu"
femauth = tweepy.OAuthHandler(femconsumer_key, femconsumer_secret)
femauth.set_access_token(femaccess_token, femaccess_token_secret)
femapi = tweepy.API(femauth)
#Search query

def search_and_save_tweets():
    query = raw_input("Which words do you want to search ?")
    max_tweets = input("How many tweets do you want to retrieve? ")
    searched_tweets = [status for status in tweepy.Cursor(api.search, q=query, lang='es',since="2015-01-01",
    until="2015-12-01").items(max_tweets)]
    output = open('searchtweets3.txt', 'w')
    dict={}

    for elem in searched_tweets:
        dict[str(elem.text)]= elem.favorite_count

    sorted_x = sorted( ((v,k) for k,v in dict.iteritems()), reverse=True)

    for k, v in sorted_x:
        output.write(str(k) + '***' + str(v) + '\n')
        #print(str(k) + ',' + str(v) + '\n')

    output.close()


def publish_tweet():
    #Read from file only if tweet has more than 2 favorites
    archivo = open('searchtweets3.txt', 'r')
    for line in archivo:
        x = line.split("***")
        try:
            print("Most favorite tweet ")
            print(x[1])
            publish = raw_input("Publish? [Y]es  to publish [N]o to pass or [E]xit to exit ")
            print(publish.lower())
            if publish.lower() == 'y':
                api.update_status(status=str(x[1]))
                femapi.update_status(status=str(x[1]))
                print('yes')
            elif publish.lower() == 'n':
                print('no')
                pass
            elif publish.lower() == 'e':
                break
        except IndexError:
                pass
    archivo.close()

search_and_save_tweets()
publish_tweet()

#api.update_status(status="Buenos y Feministas Dias")
#femapi.update_status(status="Buenos y Feministas Dias")

#to print the recovered tweet from file:
    #api.update_status(status=x[1])
    #femapi.update_status(status=x[1])