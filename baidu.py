import urllib.request
def main():
	keyword=urllib.parse.urlencode({"wd":"test"})
	#keyword=keyword.encode("utf-8")
	url="http://www.baidu.com/s?%s" % keyword
	
	print(url)
	
	with urllib.request.urlopen(url) as req:
		print(req.read().decode("utf-8"))
		#pass

if __name__=="__main__":
	main()
