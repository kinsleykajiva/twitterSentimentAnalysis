import sqlite3 as sq
import Utils as utils


class DB(object):
	"""docstring for DB"""
	def __init__(self):		
		self.conn = sq.connect(utils.DB_NAME)
		self.curser = self.conn.cursor()

		self.createDefaultTables()


	def createDefaultTables(self):
		self.curser.execute(
			"CREATE TABLE IF NOT EXISTS "
			+utils.TABLE_TITLE+"("+utils.COLUNM_TOPIC+" TEXT,"+utils.COLUNM_TWEET+" TEXT,"
			+utils.COLUNM_POLARITY+" REAL,"
			+utils.COLUNM_SENTIMENT_SUBJECTIVITY+" REAL)"
			)

	def saveAnalsis(self,topic_,tweet,sentiment_polarity,sentiment_subjectivity):
		self.curser.execute("INSERT INTO "+utils.TABLE_TITLE+" VALUES ('"+topic_+"','"+tweet+"','"+sentiment_polarity+"','"+sentiment_subjectivity+"')")
		self.conn.commit()

	def getSavedQuery(self,query):
		self.curser.execute("SELECT * FROM " + utils.TABLE_TITLE + " WHERE " + utils.COLUNM_TOPIC + " =  '" + query + "' ")		
		return self.curser.fetchall()

	def getSavedTopics(self):
		self.curser.execute("SELECT "	+ utils.COLUNM_TOPIC +	" FROM " + utils.TABLE_TITLE +	" ")		
		return self.curser.fetchall()

	    

	def closeClassConnection(self):
		self.conn.close()

	def deletTable(self):
		self.curser.execute("DROP TABLE "+utils.TABLE_TITLE)

		
