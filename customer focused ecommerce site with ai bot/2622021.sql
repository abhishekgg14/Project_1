/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - customerfocussedecommercesitewithaibot
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`customerfocussedecommercesitewithaibot` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `customerfocussedecommercesitewithaibot`;

/*Table structure for table `apprating` */

DROP TABLE IF EXISTS `apprating`;

CREATE TABLE `apprating` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `apprating` */

/*Table structure for table `brand` */

DROP TABLE IF EXISTS `brand`;

CREATE TABLE `brand` (
  `brandid` int(11) NOT NULL AUTO_INCREMENT,
  `brandname` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`brandid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `brand` */

insert  into `brand`(`brandid`,`brandname`) values 
(4,'pumaaaa'),
(5,'adidadaaa'),
(6,'sketchers'),
(7,'lp'),
(9,'swiss');

/*Table structure for table `cart` */

DROP TABLE IF EXISTS `cart`;

CREATE TABLE `cart` (
  `cartid` int(11) NOT NULL AUTO_INCREMENT,
  `productid` int(11) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  PRIMARY KEY (`cartid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `cart` */

insert  into `cart`(`cartid`,`productid`,`userid`) values 
(1,3,9);

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `caid` int(11) NOT NULL AUTO_INCREMENT,
  `catname` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`caid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`caid`,`catname`) values 
(7,'shawlsss'),
(8,'towel'),
(10,'shoe');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(200) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `productid` int(11) DEFAULT NULL,
  `respond` varchar(200) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`fid`,`feedback`,`userid`,`date`,`productid`,`respond`,`status`) values 
(1,'gvhdf',20,'2/2/2022',6,'replieddd','responded'),
(2,'sdhgsjkdsgd',20,'2/2/2022',6,'akjsfgakjsfa','responded');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`username`,`password`,`type`) values 
(1,'admin','1212','admin'),
(6,'arun@gmail.com','1010','user'),
(7,'arun@gmail.com','5678','user'),
(8,'abhi@gmail.com','2345','user');

/*Table structure for table `offer` */

DROP TABLE IF EXISTS `offer`;

CREATE TABLE `offer` (
  `offerid` int(11) NOT NULL AUTO_INCREMENT,
  `offeramount` int(11) DEFAULT NULL,
  `productid` int(11) DEFAULT NULL,
  PRIMARY KEY (`offerid`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `offer` */

insert  into `offer`(`offerid`,`offeramount`,`productid`) values 
(1,200,NULL),
(2,200,NULL),
(7,250,8),
(8,100,8),
(10,50,9),
(11,100,9),
(13,130,7);

/*Table structure for table `ordermain` */

DROP TABLE IF EXISTS `ordermain`;

CREATE TABLE `ordermain` (
  `omid` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `totalamount` int(11) DEFAULT NULL,
  PRIMARY KEY (`omid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `ordermain` */

insert  into `ordermain`(`omid`,`userid`,`date`,`totalamount`) values 
(1,20,'2022-02-20',3000),
(2,50,'2022-02-12',2000);

/*Table structure for table `ordersub` */

DROP TABLE IF EXISTS `ordersub`;

CREATE TABLE `ordersub` (
  `ordersubid` int(11) NOT NULL AUTO_INCREMENT,
  `omid` int(11) DEFAULT NULL,
  `count` int(11) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  `productid` int(11) DEFAULT NULL,
  PRIMARY KEY (`ordersubid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `ordersub` */

insert  into `ordersub`(`ordersubid`,`omid`,`count`,`amount`,`productid`) values 
(1,1,3,100,3),
(2,2,10,300,4);

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `paidid` int(11) NOT NULL AUTO_INCREMENT,
  `productid` int(11) DEFAULT NULL,
  `omid` int(11) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`paidid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `productid` int(11) NOT NULL AUTO_INCREMENT,
  `productname` varchar(50) DEFAULT NULL,
  `caid` int(11) DEFAULT NULL,
  `brandid` int(11) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `productsize` int(11) DEFAULT NULL,
  `productcolor` varchar(50) DEFAULT NULL,
  `productdescription` varchar(1000) DEFAULT NULL,
  `productimage` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`productid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`productid`,`productname`,`caid`,`brandid`,`price`,`productsize`,`productcolor`,`productdescription`,`productimage`) values 
(3,'adidas3',9,5,20000,6,'red','good quality','/static/product/shoe.jpg'),
(4,'nike prodsfs',4,5,5000,6,'red ','good quality',''),
(6,'sghghg',6,5,500,6,'red ','comfortable',''),
(7,'m2',7,6,600,7,'green ','good qualityyyyy','/static/product/3.jpg'),
(8,'m3',10,4,4000,6,'red','good quality','/static/product/shoe.jpg'),
(9,'z3',10,4,400,6,'red','comfortable','/static/product/2.jpg');

/*Table structure for table `productrateandreview` */

DROP TABLE IF EXISTS `productrateandreview`;

CREATE TABLE `productrateandreview` (
  `prateid` int(11) NOT NULL AUTO_INCREMENT,
  `preview` varchar(500) DEFAULT NULL,
  `prate` int(11) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`prateid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `productrateandreview` */

/*Table structure for table `registeruser` */

DROP TABLE IF EXISTS `registeruser`;

CREATE TABLE `registeruser` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` bigint(11) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(200) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `pin` int(10) DEFAULT NULL,
  `userlogid` int(11) DEFAULT NULL,
  `image` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `registeruser` */

insert  into `registeruser`(`userid`,`username`,`email`,`phone`,`place`,`post`,`gender`,`district`,`state`,`pin`,`userlogid`,`image`) values 
(9,'Arun bhai','arun@gmail.com  ',9876543241,'mavatt ','koyilandy ','Male','calicut ','tamilnad ',123456,7,'/static/user/3.jpg'),
(10,'abhishek gireesh','abhi@gmail.com ',3463646346,'mavatt ','arikkulam ','Male','thrissur','goa',634663,8,'/static/user/2.jpg');

/*Table structure for table `viewappreview` */

DROP TABLE IF EXISTS `viewappreview`;

CREATE TABLE `viewappreview` (
  `reviewid` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) DEFAULT NULL,
  `review` varchar(200) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`reviewid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `viewappreview` */

/*Table structure for table `wishlist` */

DROP TABLE IF EXISTS `wishlist`;

CREATE TABLE `wishlist` (
  `wlid` int(11) NOT NULL AUTO_INCREMENT,
  `productid` int(11) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  PRIMARY KEY (`wlid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `wishlist` */

insert  into `wishlist`(`wlid`,`productid`,`userid`) values 
(1,0,0);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
