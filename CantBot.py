import praw
import time

r = praw.Reddit(user_agent = "GrammarDoh! by FR3ED0M")
r.login('Red_Bot102','testtest12345',disable_warning = True)

words_to_match = ['cant','can,t','kant',"caan't",'cnt']
cache = []

def run_bot():
	print("Grabbing subreddit...")
	subreddit = r.get_subreddit("test")
	print("Grabbing comments...")
	comments = subreddit.get_comments(limit=25)
	for comment in comments:
		comment_text = comment.body.lower()
		isMatch = any(string in comment_text for string in words_to_match)
		if comment.id not in cache and isMatch:
			print("Match found! Comment ID: " + comment.id)
			comment.reply("I think you meant to say 'can't'")
			print("Reply successful!")
			cache.append(comment.id)
	print("Comments loop finished, time to sleep")

while True:
	run_bot()
	time.sleep(10)