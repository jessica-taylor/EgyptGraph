#! /usr/bin/env python

# after you've linked this script to your account using the access keys
# you can post to your account by running 
#			./post_status.py '<message here>'

import sys
import tweepy

CONSUMER_KEY = 'mJ6vPoSPrseFBsE2noKg'
CONSUMER_SECRET = 'oFxu6wKrWVLRvy2kHzVvPKpEhT9XuSrz6bcmcluDbw'

## replace the following two lines with what link_acct.py gave you
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
api.update_status(sys.argv[1])

