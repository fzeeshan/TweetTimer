-- phpMyAdmin SQL Dump
-- version 3.4.10.1deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 10, 2013 at 12:40 PM
-- Server version: 5.5.34
-- PHP Version: 5.3.10-1ubuntu3.8

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `tweet_biscuit`
--

-- --------------------------------------------------------

--
-- Table structure for table `tweets`
--

CREATE TABLE IF NOT EXISTS `tweets` (
  `tweetID` int(100) NOT NULL AUTO_INCREMENT,
  `twitterID` varchar(50) NOT NULL,
  `hashTag` varchar(100) NOT NULL,
  `userImage` varchar(200) NOT NULL,
  `userScreenName` varchar(100) NOT NULL,
  `userName` varchar(100) NOT NULL,
  `createdTime` varchar(50) NOT NULL,
  `tweetText` varchar(500) NOT NULL,
  `reTweet` varchar(100) NOT NULL,
  PRIMARY KEY (`tweetID`),
  UNIQUE KEY `tweetID` (`tweetID`),
  UNIQUE KEY `twitterID` (`twitterID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=188 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
