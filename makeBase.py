#must update makeBase SQL struct

import MySQLdb
import keyring

db = MySQLdb.connect(host=keyring.db_host, user=keyring.db_user, passwd=keyring.db_pass, db=keyring.db_name)
cur = db.cursor()

cur.execute("SELECT tweetText, tweetIndex FROM Tweets")
counts = {}
cleanup = []  
removals = ["#", "@", "!", "/", ",", "\\", "-", "'", "$", "*", "&", "%", "http", "I", "but", "for", "if", ";)", "[", "]", "my", "to", "q", "o", "that", "the", "with", "a", "do"]

for row in cur.fetchall():
	for word in row[0].split():
	    if  word not in counts:
	            counts[word] = [0, ""]
	    counts[word][0] = counts[word][0] + 1
	    counts[word][1] += str(row[1])+"," 
  
for itm in counts:
	check = itm
	for rems in removals:
		if check[0:len(rems)].lower() == rems.lower():
			cleanup.append(check)

for itm in cleanup:
	counts.pop(itm)

for itm in counts:
	cur.execute("INSERT INTO TweetText (wordMaster, wordCount, tweetRefID) VALUES(%s, %s, %s)",(itm, counts[itm][0], counts[itm][1]))
db.commit()
db.close()
