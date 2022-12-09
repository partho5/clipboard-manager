import urllib2


class library(object):
	def isInternet(object):
		try:
			urllib2.urlopen("http://216.58.192.142", timeout=1)
			return True
		except Exception as e:
			return False

'''
if __name__=="__main__":
	myLibrary=library()
	if myLibrary.isInternet():
		print("internet connected")
	else:
		print("NOT connected")
'''