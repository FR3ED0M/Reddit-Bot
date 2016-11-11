# this is a template for a reddit bot for grammar checking comments
# make sure to have python 3.5 and pip installed
# run within cmd.exe if needed for test purposes

import praw 
import time

r = praw.Reddit(user_agent = "insert bot name and user name message")
r.login('username','password',disable_warning = True) 		# disable_warning disables the login screen during command window
								# should be created in different source to be made private

words_to_match = ['word1','word2','word3','...and so on'] 	# add words so that bot can check what to look for 
cache = []  										# array for storing already found mismatched words and their id

def run_bot():
	print("Grabbing subreddit...")
	subreddit = r.get_subreddit("subreddit name")  	# the name of which subreddit the bot will be working in
	print("Grabbing comments...")
	comments = subreddit.get_comments(limit=25)    	# the limit of how many comments to check for (don't go overboard, follow API guidelines)
	for comment in comments:					   	# for loop
		comment_text = comment.body.lower()		   	# make sure lower() is added to make all capitalized mismatched words in lowercase
		isMatch = any(string in comment_text for string in words_to_match)
		if comment.id not in cache and isMatch:	   							# if the comment has not been found in the cache and is a match, run this
			print("Match found! Comment ID: " + comment.id)
			comment.reply("I think you meant to say 'correct spelled word'")  # the correct spelling of the word your bot is checking for
			print("Reply successful!")
			cache.append(comment.id)				# add the comment id in the cache array so that bot doesn't reply to same comment more than once
	print("Comments loop finished, time to sleep")

while True:											# while loop that allows bot to stop and check for a new misspelled comment
	run_bot()
	time.sleep(10)									# bot needs to sleep. !!Reminder that sleep is measured in seconds!!
