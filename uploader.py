from library import library
import time
from dbQuery import dbHelper
import requests

myLibrary=library()
dbHelper=dbHelper()

while True:
	if myLibrary.isInternet():
		print dbHelper.getSingleData()
		response=requests.post("http://localhost/eee-du/n", data={'cpTxt':"ddff", 'cpTime':"2:4"})
		print(response.content)
	time.sleep(3)