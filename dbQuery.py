import sqlite3
from time import gmtime, strftime

connection=None

class dbHelper:
	"""docstring for dbHelper"""
	def insertCopiedText(self, copied_text):
		try:
			connection=sqlite3.connect('/home/partho/py/clip-sync/clipData.db')
			print "connected"
			cursor=connection.cursor()
		except Exception as e:
			print e
		finally:
			curTime=strftime("%Y-%m-%d %H:%M:%S", gmtime());
			
			try:
			    cursor.execute('INSERT INTO copied_data(copied_text, copy_time, uploaded) VALUES(?, ?, 0)', (copied_text, curTime))
			    connection.commit()
			    connection.close()
			    print("inserted")
			except Exception as e:
			    raise e

	def getSingleData(object):
		q="SELECT * FROM copied_data WHERE uploaded=0 ORDER BY ID DESC LIMIT 1";
		try:
			connection=sqlite3.connect('/home/partho/py/clip-sync/clipData.db')
			cursor=connection.cursor()
		except Exception as e:
			print e
		finally:
			cursor.execute(q)
			for row in cursor:
				print row[1]
				print row[2]

		
