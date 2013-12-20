import MySQLdb
import keyring

db = MySQLdb.connect(host=keyring.db_host, user=keyring.db_user, passwd=keyring.db_pass)
cur = db.cursor()

#Enter SQL Stmt
cur.execute("""
	CREATE DATABASE HT_Nerd;
	USE HT_Nerd;

	CREATE TABLE Tweets
	(
		tweetIndex int AUTO_INCREMENT PRIMARY KEY,
		tweetID bigint(255) UNIQUE,
		hashTag varchar(100),
		userID bigint(255), 
		createdTime varchar(100),
		tweetText varchar(200), 
		reTweet int
	);

	CREATE TABLE Users
	(
		userIndex int AUTO_INCREMENT PRIMARY KEY,
	 	userID bigint(255),
	 	userImage varchar(500), 
	 	userScreenName varchar(200),
	 	userRealName varchar(200)
	 );

	CREATE TABLE TweetText
	(
		wordIndex int AUTO_INCREMENT PRIMARY KEY,
		wordMaster varchar(200),
		wordCount int
	);

""")
