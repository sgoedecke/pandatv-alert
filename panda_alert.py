#! /usr/bin/env python
import urllib2
import json
import smtplib
import time

# the program looks for these keywords in the list of current streamers
STREAMER_LIST = ["Arteezy","Envy", "arteezy", "envy", "puppey","Puppey","Bulba","bulba","pieliedie","Pieliedie"]
REFRESH_RATE = 300 #sleep for 300 seconds between each check

def find_dota_streamers():
	# returns a list of names of the top Dota 2 streamers

	# get the json-format data
	print "Getting data from panda.tv..."
	raw_data = urllib2.urlopen('http://api.m.panda.tv/ajax_get_live_list_by_cate?cate=dota2&order=person_num&pageno=1&pagenum=100&status=2')
	json_data = json.loads(raw_data.read())
	print "Got data!"
	# print json.dumps(json_data, sort_keys=True, indent=4, separators=(',', ': '))

	# strip out the usernames from the json-format data
	items = json_data['data']['items']
	users = []
	for item in items:
		user = item['userinfo']
		users.append(user['nickName'])
	return users

def notify_user():
	# beeps to let the user know someone's streaming
	for x in range(0,3):
		print "Alert! \a" #beep
		time.sleep(1)
	print "Found a match!"
	return

def run_alerter():
	print "\nWelcome to the panda.tv alerter."
	print "Alright, looking now!"
	looking = True
	found = False
	while looking:
		users = find_dota_streamers()
		print "\nUser list"
		print "----------"
		for username in users:
			print username #display user list
			for keyword in STREAMER_LIST:
				if keyword in username:
					found = True
		if found == True:
			notify_user()
			found = False
		else:
			print "\nNo matches. Waiting five minutes..."
		time.sleep(REFRESH_RATE) # sleep for five minutes

# main loop
if __name__ == '__main__':
    try:
        run_alerter()
    except KeyboardInterrupt: # exit gracefully if user presses Ctrl+C
        pass
    finally:
        print "\nThank you for using the panda.tv alerter."
