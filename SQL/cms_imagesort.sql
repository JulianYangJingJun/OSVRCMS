/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : osvr_cms20170620

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2017-11-30 11:17:53
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for cms_imagesort
-- ----------------------------
DROP TABLE IF EXISTS `CMS_imagesort`;
CREATE TABLE `CMS_imagesort` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `shortname` varchar(10) NOT NULL,
  `enname` varchar(30) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `folder_id` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `CMS_imagesort_enname_02b429fa_uniq` (`enname`),
  UNIQUE KEY `CMS_imagesort_name_d61148ce_uniq` (`name`),
  UNIQUE KEY `CMS_imagesort_shortname_fdfde6f5_uniq` (`shortname`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of cms_imagesort
-- ----------------------------
INSERT INTO `CMS_imagesort` VALUES ('40', '风景', '风景', '风景', '2017-11-21 10:04:17.333000', '2017-11-21 10:04:17.334000', '93');
INSERT INTO `CMS_imagesort` VALUES ('41', '美女', '美女', '美女', '2017-11-21 10:04:25.724000', '2017-11-21 10:04:25.724000', '94');
INSERT INTO `CMS_imagesort` VALUES ('42', '创意', '创意', '创意', '2017-11-21 10:04:32.472000', '2017-11-21 10:04:32.472000', '95');
INSERT INTO `CMS_imagesort` VALUES ('43', '汽车', '汽车', '汽车', '2017-11-21 10:04:46.572000', '2017-11-21 10:04:46.572000', '96');
INSERT INTO `CMS_imagesort` VALUES ('44', '田园', '田园', '田园', '2017-11-21 10:04:56.465000', '2017-11-21 10:04:56.465000', '97');
INSERT INTO `CMS_imagesort` VALUES ('45', '影视', '影视', '影视', '2017-11-27 17:18:00.302000', '2017-11-27 17:18:00.302000', '98');
