import tweepy
import sys
import operator
reload(sys)
sys.setdefaultencoding("utf-8")


consumer_key = "U9BfrQUfq2ZYoUzguihU0vb1W"
consumer_secret = "44SvMoJhVolsaKvu1gyJStTnO7qwCOo95PHMYzsVw3HTCAvbXP"
access_token = "3754637839-oMtjXQaRm8X1Zh84O0vcgTqys4dNKTu94neEnVj"
access_token_secret = "SMwDSe95015Yk3C3rCB5sOJsdzGSv5PIMn0dEvSZhmBvG"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#Search query

query = '#feminismo'
max_tweets = 30
searched_tweets = [status for status in tweepy.Cursor(api.search, q=query, lang='es',since="2015-01-01",
    until="2015-12-01").items(max_tweets)]

output = open('searchtweets3.txt', 'w')
dict={}
for elem in searched_tweets:
     dict[str(elem.text)]= elem.favorite_count


sorted_x = sorted( ((v,k) for k,v in dict.iteritems()), reverse=True)

for k, v in sorted_x:
    output.write(str(k) + ',' + str(v) + '\n')

output.close()

#Read from file only if tweet has more than 2 favorites
archivo = open('searchtweets3.txt', 'r')
for line in archivo:
    x = line.split(",")
    print(x[1])
archivo.close()
#api.update_status(status="Buenas y Feministas Tardes")
#to print the recovered tweet from file:
#api.update_status(status=x[1])