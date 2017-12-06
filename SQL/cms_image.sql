/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : osvr_cms20170620

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2017-11-30 11:02:35
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for cms_image
-- ----------------------------
DROP TABLE IF EXISTS `CMS_image`;
CREATE TABLE `CMS_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `synopsis` longtext,
  `score` double DEFAULT NULL,
  `playcount` int(11) DEFAULT NULL,
  `is_recommend` tinyint(1) NOT NULL,
  `is_latest` tinyint(1) NOT NULL,
  `is_hottest` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `Genres_id` int(11) DEFAULT NULL,
  `imageurl_id` int(11) DEFAULT NULL,
  `Sort_id` int(11),
  `sorting` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `imageurl_id` (`imageurl_id`),
  KEY `CMS_image_Genres_id_d9d0be2f_fk_CMS_imagegenres_id` (`Genres_id`),
  KEY `CMS_image_Sort_id_7462e39f_fk_CMS_imagesort_id` (`Sort_id`),
  CONSTRAINT `CMS_image_Genres_id_d9d0be2f_fk_CMS_imagegenres_id` FOREIGN KEY (`Genres_id`) REFERENCES `CMS_imagegenres` (`id`),
  CONSTRAINT `CMS_image_Sort_id_7462e39f_fk_CMS_imagesort_id` FOREIGN KEY (`Sort_id`) REFERENCES `CMS_imagesort` (`id`),
  CONSTRAINT `CMS_image_imageurl_id_94423eb4_fk_filer_file_id` FOREIGN KEY (`imageurl_id`) REFERENCES `filer_file` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of cms_image
-- ----------------------------
INSERT INTO `CMS_image` VALUES ('4', '夺宝奇兵', '111', '11', '11', '0', '0', '0', '2017-11-27 17:20:14.845000', '2017-11-29 14:32:49.359000', '1', '57', '45', '255');
INSERT INTO `CMS_image` VALUES ('5', '飞行战船', '2', '2', '2', '0', '1', '0', '2017-11-27 17:20:27.730000', '2017-11-27 17:20:27.730000', '2', '56', '45', '255');
INSERT INTO `CMS_image` VALUES ('6', '美国队长', '4', '4', '4', '0', '1', '0', '2017-11-27 17:20:42.252000', '2017-11-27 17:20:42.252000', '3', '58', '45', '255');
INSERT INTO `CMS_image` VALUES ('7', '销魂战士', '4', '4', '4', '0', '0', '0', '2017-11-27 17:21:03.209000', '2017-11-27 17:21:03.209000', '4', '59', '45', '255');
INSERT INTO `CMS_image` VALUES ('8', '哈利波特7', '5', '5', '5', '0', '0', '0', '2017-11-27 17:21:16.695000', '2017-11-27 17:21:16.695000', '5', '60', '45', '15');
INSERT INTO `CMS_image` VALUES ('9', '土著革面', '6', '6', '6', '0', '0', '0', '2017-11-27 17:21:28.351000', '2017-11-27 17:21:28.351000', '6', '61', '45', '13');
INSERT INTO `CMS_image` VALUES ('10', '1', '2', '1', '2', '1', '0', '0', '2017-11-29 14:33:21.755000', '2017-11-29 14:48:58.676000', '1', '62', '41', '12');
INSERT INTO `CMS_image` VALUES ('11', '2', '333', '2', '3', '1', '0', '0', '2017-11-29 14:33:47.211000', '2017-11-29 14:33:47.211000', '2', '64', '41', '11');
INSERT INTO `CMS_image` VALUES ('12', '3', '55', '3', '5', '1', '0', '0', '2017-11-29 14:34:06.443000', '2017-11-29 14:34:06.443000', '3', '65', '41', '10');
INSERT INTO `CMS_image` VALUES ('13', '4', '5', '4', '5', '1', '0', '0', '2017-11-29 14:34:30.000000', '2017-11-29 14:34:33.000000', '4', '66', '41', '9');
INSERT INTO `CMS_image` VALUES ('14', '5', '7', '5', '6', '1', '0', '0', '2017-11-29 14:40:17.159000', '2017-11-29 14:40:17.159000', '5', '67', '41', '8');
INSERT INTO `CMS_image` VALUES ('15', '6', '7', '6', '7', '1', '0', '0', '2017-11-29 14:40:32.659000', '2017-11-29 14:40:32.659000', '6', '68', '41', '7');
INSERT INTO `CMS_image` VALUES ('16', '7', '8', '7', '8', '1', '0', '0', '2017-11-29 14:40:52.171000', '2017-11-29 14:40:52.171000', '1', '69', '41', '6');
INSERT INTO `CMS_image` VALUES ('17', '8', '11', '8', '1', '1', '0', '0', '2017-11-29 14:41:14.229000', '2017-11-29 14:41:14.229000', '2', '71', '41', '5');
INSERT INTO `CMS_image` VALUES ('18', '9', '11', '9', '1', '1', '0', '0', '2017-11-29 14:41:26.395000', '2017-11-29 14:41:26.395000', '3', '72', '41', '4');
INSERT INTO `CMS_image` VALUES ('19', '10', '14', '14', '14', '1', '0', '0', '2017-11-29 14:41:43.386000', '2017-11-29 14:41:43.387000', '4', '73', '41', '3');
INSERT INTO `CMS_image` VALUES ('20', '11', '1515', '15', '15', '1', '0', '0', '2017-11-29 14:42:03.698000', '2017-11-29 14:42:03.698000', '5', '74', '41', '2');
INSERT INTO `CMS_image` VALUES ('21', '12', '16', '16', '16', '1', '0', '0', '2017-11-29 14:42:37.620000', '2017-11-29 14:42:37.620000', '6', '76', '41', '1');
