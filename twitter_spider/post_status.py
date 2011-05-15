#! /usr/bin/env python

# Python script to post to twitter as a given user.
# Depends on said library, so get it here:
# http://code.google.com/p/python-twitter/
# http://code.google.com/p/httplib2/

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

