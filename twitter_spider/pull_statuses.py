#! /usr/bin/env python

import sys
import tweepy

CONSUMER_KEY = 'mJ6vPoSPrseFBsE2noKg'
CONSUMER_SECRET = 'oFxu6wKrWVLRvy2kHzVvPKpEhT9XuSrz6bcmcluDbw'
## replace the following two lines with what link_acct.py gave you
ACCESS_KEY = ''
ACCESS_SECRET = ''

tw_no = 0;
tweet = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)
atl_tweets = api.user_timeline("as_te_li")

for tweet in atl_tweets:
	tw_no = tw_no + 1
	print "No",tw_no,":",tweet.text
tw_no = 0

