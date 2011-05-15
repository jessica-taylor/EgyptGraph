#! /usr/bin/env python

# Python script to post to twitter as a given user.
# Depends on said library, so get it here:
# http://code.google.com/p/python-twitter/
# http://code.google.com/p/httplib2/

import sys
import tweepy

CONSUMER_KEY = 'mJ6vPoSPrseFBsE2noKg'
CONSUMER_SECRET = 'oFxu6wKrWVLRvy2kHzVvPKpEhT9XuSrz6bcmcluDbw'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth_url = auth.get_authorization_url()
print 'Please authorize: ' + auth_url
verifier = raw_input('PIN: ').strip()
auth.get_access_token(verifier)
print "ACCESS_KEY = '%s'" % auth.access_token.key
print "ACCESS_SECRET = '%s'" % auth.access_token.secret


