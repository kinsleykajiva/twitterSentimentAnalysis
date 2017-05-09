"""this is just to keep constants and reduce the rounds of code update"""




import re 
import sqDb   



DB_NAME="saved/sentiments.db"
TABLE_TITLE="sentimentor"
COLUNM_TWEET="tweet"
COLUNM_SENTIMENT_SUBJECTIVITY="sentiment_subjectivity"
COLUNM_POLARITY="sentiment_polarity"
COLUNM_TOPIC="topic"
topic="mugabe"
REMOTE_SERVER__FOR__CONNECTION_CHECKING="www.google.com"


WINDOW_TITLE="Political Sentiment Analysis on Tweeter !!!"
CSV_HEADER=['tweet','sentiment_polarity','sentiment_subjectivity']
subjectivity ="the subjectivity or objectivity of the tweet. 0 is very objective, 1 is very subjective."
polarity ="the sentiment of the tweet, from -1, to 1. 1 indicates strong positivity, -1 strong negativity."

def getQueryTweets(txtQuery):
	""" this is just to get a few tweets as opposed to get a live stream or a continous
		Stream .This is because or internet connection it may fail to  keep up but the few will will use 
		even save them to file or for demo reasons commit them in memory 
	"""
	import tweepy
	return_tweets=[]
	consumer_key =  '8fMHmOraNH1J5fFYBFFzXlz0e'
	consumer_secret = 'em3l9zq196EK8o0XsqUFEGj5ojGqnF7vql36LmgKdL7Koo3xJD'

	access_token = '1741416668-OiGrvcaKmeoXtZVptjeQWMTsROj3x4fBNMNTJkT'
	access_token_secret = '2Jqfc0aW6EGIUy4RKe5utfV5lIigJVAtSgTfOpgMeaLy8'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	#Step 3 - Retrieve Tweets
	if len(txtQuery)==0 or len(txtQuery)<0:
		return "empty"

	public_tweets = api.search(txtQuery)

	for tweeet_msgs in public_tweets:
		return_tweets.append(tweeet_msgs.text)

	return return_tweets

def list_of_ReturnsLists( * args):
	return [args[0],args[1],args[2]]
def removeDuplicates(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def analiseTweetSentment(txttweet):
	from textblob import TextBlob
	list_mesgs=[]
	list_polarity=[]
	list_subjectivity=[]
	
	db=sqDb.DB() # save the tweet infomation as we loop in the analysis 
	for xtract in txttweet:
		list_mesgs.append(xtract)
		list_polarity.append(str(TextBlob(xtract).sentiment.polarity))
		list_subjectivity.append(str(TextBlob(xtract).sentiment.subjectivity))
		

		db.saveAnalsis(	topic,
			xtract.translate(str.maketrans({"'":None})),
			str(TextBlob(xtract).sentiment.polarity),
			str(TextBlob(xtract).sentiment.subjectivity)
			) # escaped sinlge qoute chars as the have issues with sqlite database at writting time 

	
	return list_mesgs,list_polarity,list_subjectivity



def saveToCSV(tweet_lists,sentiment_polarity,sentiment_subjectivity):
	import csv
	__file='saved/'+fileNamer()

	with open(__file, 'w',encoding='utf-8') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		filewriter.writerow([CSV_HEADER[0], CSV_HEADER[1],CSV_HEADER[2]])
		for i in range(len(tweet_lists)):
			filewriter.writerow([tweet_lists[i], sentiment_polarity[i],sentiment_subjectivity[i]])

	


def fileNamer():
	import time
	return "sentiments__"+str(time.strftime("%Y%m%d-%H%M%S"))+".csv"

def processLinner():
	print("\n\n==================================================")
	print("==================================================")
	print("==========*****Processing Please Wait*****========")
	print("==================================================")	
	print("==================================================\n\n")

if __name__ == '__main__':
	

	fromtweeter=getQueryTweets(topic)
	tweeet_msgs,polarity,subjectivity=analiseTweetSentment(fromtweeter)
	print (tweeet_msgs)
	print (polarity)
	print(subjectivity)
	
	#saveToCSV(a,b,c)
	"""DB=sqDb.DB()
	for i in range(len(a)):
		DB.saveAnalsis(	topic,a[i],b[i],str(c[i]) )

	DB.closeClassConnection()"""
	
	"""sample1=["sdfsd",123,"123222dsfsdfds"]
	sample2=["sdfsd",4567,"er54e5w"]
	sample3=["sdfsd",7897,"cxfghre6"]
	sample4=["sdfsd",879087,"xzcv df"]
	dataa=[sample1,sample2,sample3,sample4]
	items = [{'header1': 'value', 'header2': 'value2'},
         {'header1': 'blah1', 'header2': 'blah2'}]
	import csv
	# saveTotxtFile_CSV([sample1,sample2,sample3,sample4])
	daaa=[]

	try:
	    with open(fileNamer(), 'wt', newline='') as csv_file:
	        writer = csv.DictWriter(csv_file, ['header1', 'header2'])
	        writer.writeheader()
	        for item in items:
	            writer.writerow(item)
	except TypeError:
	    with open('test.csv', 'wb') as csv_file:
	        writer = csv.DictWriter(csv_file, ['header1', 'header2'])
	        writer.writeheader()
	        for item in items:
	            writer.writerow(item)"""


	# print(fileNamer())

	



