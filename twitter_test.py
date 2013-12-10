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
    twitterID = tweet['id']
    twitterProImg = tweet['user']['profile_image_url']
    twitterScreenName = tweet['user']['screen_name']
    twitterUserName = tweet['user']['name'].encode('utf8')
    twitterCreated = tweet['created_at']
    twitterText = tweet['text'].encode('utf8')
    twitterRecount = tweet['retweet_count']
    cur.execute("INSERT IGNORE INTO tweets (twitterID, hashTag, userImage, userScreenName, userName, createdTime, tweetText, reTweet) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",(twitterID, twitterProImg, searchHash, twitterScreenName, twitterUserName, twitterCreated, twitterText, twitterRecount))
    print str(twitterID)
    print twitterProImg
    print twitterScreenName,
    print "("+twitterUserName+")"
    print twitterCreated
    print twitterText
    print "RT: " + str(twitterRecount)
    print "--------------------------------------------------------------------"
db.commit()
db.close()
print "Complete!"
