#! /usr/bin/env python

# Python script to pull twitter status posts from a given user.
# Just trying out the python-twitter library.
# Depends on said library, so get it here:
# http://code.google.com/p/python-twitter/

print "Twitter Spider"

tw_no = 0  #tweet iterator

import httplib2
import twitter

api = twitter.Api()

atl_status = api.GetUserTimeline("as_te_li")

for s in atl_status:
	tw_no = tw_no+1
	print "Tweet #",tw_no,":",s.text,""

