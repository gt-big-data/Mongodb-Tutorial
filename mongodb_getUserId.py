import sys
import json
import tweepy
from tweepy import OAuthHandler

def loadCredentials():
	f = open('credentials.json')
	credentials = json.load(f)
	f.close()

	consumer_key = credentials["APP_KEY"]
	consumer_secret = credentials["APP_SECRET"]
	access_token = credentials["ACCESS_TOKEN"]
	access_secret = credentials["ACCESS_TOKEN_SECRET"]

	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)

	return auth

def main():
	if len(sys.argv) != 2:
		print "Incorrect number of arguments"
		return
	screen_name = sys.argv[1]

	auth = loadCredentials()
	api = tweepy.API(auth)

	tweet = api.user_timeline(screen_name=screen_name, count=1)
	id_str = tweet[0].user.id_str

	print id_str
	

if __name__ == "__main__":
	main()