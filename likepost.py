import facebook
import re
token = "your token goes here"
profile = graph.get_object("3ST Technologies")
posts = graph.get_connections(profile['id'],"posts")

for post in posts['data']:
	try:
		graph.put_object(post['id'],"likes")
		print "Liking the topic: "+post['message']
	except:
		continue
