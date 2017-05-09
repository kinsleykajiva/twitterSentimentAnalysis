import matplotlib.pyplot as plt

import matplotlib.dates as mdates
import matplotlib.animation as animation
import time
from dateutil import parser
from matplotlib import style
style.use('fivethirtyeight')
import numpy as np
import pandas as pd
import Utils as utils




def readFromCSv(file_name):
	return pd.read_csv('saved/'+file_name)

def showCSVTable(file_name):
	readFromCSv(file_name).head()

def graph_data_1(x,y):
	"""x and y are lists are """
	fig = plt.figure()
	ax1 = fig.add_subplot(111)
	#fig.set_size_inches(30, fig.get_figheight(), forward=True)
	ax1.clear()
	ax1.set_title('Sentiment Review for topic on :'+utils.topic)
	ax1.set_xlabel('number of tweets')
	ax1.set_ylabel('tweets Sentiment Polarity')	
	ax1.plot(x,y)
	#ani = animation.FuncAnimation(fig, animate, interval=1000)
	plt.show()
    



if __name__ == '__main__':
	#showCSVTable("sentiments__20170506-130543.csv")
	import sqDb as db
	#DB=db.DB()
	x=[]
	y=[]

	x_=0
	y_=0

	data=db.DB().getSavedQuery("topic")
	for i in data:
		x_+=1		
		if i[2] < 0:
			y_+=1
		elif i[2]>0:
			y_-=1
		

		x.append(x_)
		y.append(y_)

	graph_data_1(x,y)






