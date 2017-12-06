/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : osvr_cms20170620

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2017-11-30 10:55:49
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for cms_ad
-- ----------------------------
DROP TABLE IF EXISTS `CMS_ad`;
CREATE TABLE `CMS_ad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `local` int(11) NOT NULL,
  `ad_img` varchar(100) NOT NULL,
  `sorting` int(11) NOT NULL,
  `ad_url` varchar(200) DEFAULT NULL
  `clickcount` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `score` int(11),
  `title` varchar(255),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of cms_ad
-- ----------------------------
INSERT INTO `cms_ad` VALUES ('1', '1', 'Ad/img/2017/11/27/jx1.jpg', '255', 'http://www.cctv.asdf', '22', '2017-11-27 10:32:25.249000', '2017-11-27 10:43:01.051000', '5', '神龙战甲');
INSERT INTO `cms_ad` VALUES ('2', '1', 'Ad/img/2017/11/27/jx2_ErIar42.jpg', '255', 'http://www.baidu.com', '333', '2017-11-27 10:32:59.177000', '2017-11-27 14:07:06.133000', '4', '极品飞车7');
INSERT INTO `cms_ad` VALUES ('3', '1', 'Ad/img/2017/11/27/jx3.jpg', '255', 'http://www.baidu.com', '33', '2017-11-27 10:33:08.866000', '2017-11-27 13:37:25.040000', '5', '时光战舞');
INSERT INTO `cms_ad` VALUES ('4', '2', 'Ad/img/2017/11/27/ys1.jpg', '255', 'http://www.baidu.com', '44', '2017-11-27 10:38:01.541000', '2017-11-27 13:37:25.044000', '5', '影视1');
INSERT INTO `cms_ad` VALUES ('5', '2', 'Ad/img/2017/11/27/ys2.jpg', '255', 'http://www.baidu.com', '55', '2017-11-27 10:38:12.077000', '2017-11-27 13:37:25.048000', '5', '影视2');
INSERT INTO `cms_ad` VALUES ('6', '2', 'Ad/img/2017/11/27/ys3.jpg', '255', 'http://www.baidu.com', '55', '2017-11-27 10:38:22.080000', '2017-11-27 13:37:25.053000', '5', '影视3');
