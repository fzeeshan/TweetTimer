from twitter import *
import MySQLdb
import keyring

searchHash = "#nerd"
searchCount = 10

db = MySQLdb.connect(host=keyring.db_host, user=keyring.db_user, passwd=keyring.db_pass, db=keyring.db_name)
cur = db.cursor()

t = Twitter(auth=OAuth(keyring.t_at, keyring.t_ats, keyring.t_c, keyring.t_cs))
x = t.search.tweets(q=searchHash, count=searchCount)
tweets = x['statuses']

for tweet in tweets:
    tweetID = tweet['id']
    tweetCreated = tweet['created_at']
    tweetText = tweet['text'].encode('utf8')
    tweetRecount = tweet['retweet_count']

    userID = tweet['user']['id']
    userImage = tweet['user']['profile_image_url']
    userScreenName = tweet['user']['screen_name']
    userRealName = tweet['user']['name'].encode('utf8')

    cur.execute("INSERT IGNORE INTO Tweets (tweetID, hashTag, userID, createdTime, tweetText, reTweet) VALUES(%s, %s, %s, %s, %s, %s)",(tweetID, searchHash, userID, tweetCreated, tweetText, tweetRecount))
    cur.execute("INSERT IGNORE INTO Users (userID, userImage, userScreenName, userRealName) VALUES(%s, %s, %s, %s)",(userID, userImage, userScreenName, userRealName))
    print "tweetID: "+str(tweetID)
    print userScreenName,
    print "("+userRealName+")- ",
    print str(userID)
    print tweetCreated
    print tweetText
    print "RT: " + str(tweetRecount)
    print "--------------------------------------------------------------------"
db.commit()
db.close()
print "Complete!"
