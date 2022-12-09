import time
import subprocess
import sqlite3
from dbQuery import dbHelper

myList=[]
dbHelper=dbHelper()
while True:
    lastCopy=subprocess.check_output('xsel -b', shell=True)
    if(lastCopy not in myList):
    	myList.append(lastCopy)
    	print("Clipboard changed  : "+lastCopy)
    	try:
    		dbHelper.insertCopiedText(lastCopy)
    	except Exception as e:
    		print(e)
    time.sleep(0.5)
