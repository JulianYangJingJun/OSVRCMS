/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : osvr_cms20170620

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2017-11-30 11:17:47
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for cms_imagegenres
-- ----------------------------
DROP TABLE IF EXISTS `CMS_imagegenres`;
CREATE TABLE `CMS_imagegenres` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `shortname` varchar(10) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of cms_imagegenres
-- ----------------------------
INSERT INTO `CMS_imagegenres` VALUES ('1', '2D普通', '2D普通', '2017-10-24 15:35:37.778000', '2017-10-24 15:35:37.778000');
INSERT INTO `CMS_imagegenres` VALUES ('2', '3D左右普通', '3D左右', '2017-10-24 15:36:26.255000', '2017-11-29 10:58:20.285000');
INSERT INTO `CMS_imagegenres` VALUES ('3', '3D上下普通', '3D上下', '2017-10-24 15:36:40.301000', '2017-11-29 10:58:25.217000');
INSERT INTO `CMS_imagegenres` VALUES ('4', '2D 360', '2D 360', '2017-10-24 15:36:48.572000', '2017-10-24 15:36:48.572000');
INSERT INTO `CMS_imagegenres` VALUES ('5', '3D左右 360', '3D左右 360', '2017-10-24 15:36:57.519000', '2017-10-24 15:36:57.519000');
INSERT INTO `CMS_imagegenres` VALUES ('6', '3D上下 360', '3D上下 360', '2017-10-24 15:37:09.455000', '2017-10-24 15:37:09.455000');
