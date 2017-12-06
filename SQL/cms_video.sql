/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : osvr_cms20170620

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2017-11-30 11:52:32
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for cms_video
-- ----------------------------
DROP TABLE IF EXISTS `CMS_video`;
CREATE TABLE `CMS_video` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(70) NOT NULL,
  `shortname` varchar(14) NOT NULL,
  `synopsis` longtext,
  `videocover` varchar(100) NOT NULL,
  `videopath_id` int(11) DEFAULT NULL,
  `videourl` varchar(200) DEFAULT NULL,
  `score` double,
  `filecapacity` double DEFAULT NULL,
  `viewingcount` int(11) DEFAULT NULL,
  `downloadcount` int(11) DEFAULT NULL,
  `label` varchar(255) DEFAULT NULL,
  `forum` varchar(200) DEFAULT NULL,
  `img` varchar(100) DEFAULT NULL,
  `img1` varchar(100) DEFAULT NULL,
  `img2` varchar(100) DEFAULT NULL,
  `img3` varchar(100) DEFAULT NULL,
  `img4` varchar(100) DEFAULT NULL,
  `img5` varchar(100) DEFAULT NULL,
  `sorting` int(11) NOT NULL,
  `is_panoramic` tinyint(1) NOT NULL,
  `is_copyright` tinyint(1) NOT NULL,
  `is_recommend` tinyint(1) NOT NULL,
  `is_latest` tinyint(1) NOT NULL,
  `is_hottest` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `Genres_id` int(11) DEFAULT NULL,
  `playcount` int(11),
  `videotime` int(11),
  `starring` varchar(255),
  PRIMARY KEY (`id`),
  UNIQUE KEY `CMS_video_videopath_id_105e4b4d_uniq` (`videopath_id`),
  KEY `CMS_video_Genres_id_a3af1a9d_fk_CMS_videogenres_id` (`Genres_id`),
  CONSTRAINT `CMS_video_Genres_id_a3af1a9d_fk_CMS_videogenres_id` FOREIGN KEY (`Genres_id`) REFERENCES `CMS_videogenres` (`id`),
  CONSTRAINT `CMS_video_videopath_id_105e4b4d_fk_filer_file_id` FOREIGN KEY (`videopath_id`) REFERENCES `filer_file` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- -- ----------------------------
-- -- Records of cms_video
-- -- ----------------------------
-- INSERT INTO `cms_video` VALUES ('1', '将军在上', '一镜一视界巴黎第1集', '一镜一视界巴黎第1集', 'video/cover/2017/11/27/1.jpg', '36', 'http://www.baidu.com', '4.5', '11', '0', '0', '', '', 'video/img/2017/11/27/1_63HhU41.jpg', '', '', '', '', '', '8', '0', '0', '1', '0', '0', '2017-11-27 15:01:42.028000', '2017-11-29 15:55:16.282000', '5', '0', '11', '匿名');
-- INSERT INTO `cms_video` VALUES ('2', '猎场', '猎场', '猎场', 'video/cover/2017/11/27/2.jpg', '39', 'http://www.baidu.com', '5', '11', '0', '0', '', '', 'video/img/2017/11/27/2_1T6NadJ.jpg', '', '', '', '', '', '1', '1', '0', '1', '0', '0', '2017-11-27 15:02:23.183000', '2017-11-29 15:55:07.392000', '5', '0', '11', '匿名');
-- INSERT INTO `cms_video` VALUES ('3', '海上牧云记', '一镜一视界巴黎第3集', '一镜一视界巴黎第3集', 'video/cover/2017/11/27/3.jpg', '40', 'http://www.baidu.com', '4.7', '2', '0', '0', '', '', 'video/img/2017/11/27/3_3UdNaOP.jpg', '', '', '', '', '', '2', '0', '0', '1', '0', '0', '2017-11-27 15:02:54.623000', '2017-11-28 17:33:29.074000', '5', '0', '11', '匿名');
-- INSERT INTO `cms_video` VALUES ('4', '奇葩说', '一镜一视界巴黎第4集', '一镜一视界巴黎第4集', 'video/cover/2017/11/27/4.jpg', '35', 'http://www.baidu.com', '4.9', '11', '0', '0', '', '', 'video/img/2017/11/27/4_RHyE1EY.jpg', '', '', '', '', '', '3', '0', '0', '1', '0', '0', '2017-11-27 15:03:27.744000', '2017-11-28 17:33:29.081000', '5', '0', '11', '匿名');
-- INSERT INTO `cms_video` VALUES ('5', '青春旅行', 'Min Flash', 'Min Flash', 'video/cover/2017/11/27/5.jpg', '43', 'http://www.baidu.com', '4.1', '1', '0', '0', '', '', 'video/img/2017/11/27/5_Z35KnHq.jpg', '', '', '', '', '', '4', '0', '0', '1', '0', '0', '2017-11-27 15:45:25.167000', '2017-11-28 09:47:43.348000', '1', '0', '11', '匿名');
-- INSERT INTO `cms_video` VALUES ('6', '长城', 'Travel journal', 'Travel journal 3D字幕版', 'video/cover/2017/11/27/6.jpg', '41', 'http://www.baidu.com', '4.1', '1', '0', '0', '', '', 'video/img/2017/11/27/6_Rvmernm.jpg', '', '', '', '', '', '5', '0', '1', '1', '0', '0', '2017-11-27 15:46:06.231000', '2017-11-28 17:33:29.087000', '5', '0', '11', '匿名');
-- INSERT INTO `cms_video` VALUES ('7', '我的老婆未成年', 'Sargadelos字幕版.', 'Sargadelos字幕版.mov', 'video/cover/2017/11/27/7.jpg', '42', 'http://www.baidu.com', '4.6', '222', '0', '0', '', '', 'video/img/2017/11/27/7_8cClqwm.jpg', '', '', '', '', '', '6', '0', '0', '1', '0', '0', '2017-11-27 15:47:05.524000', '2017-11-28 17:33:29.093000', '3', '0', '11', '匿名');
-- INSERT INTO `cms_video` VALUES ('8', '我的体育老师', '3D chef', '3D chef', 'video/cover/2017/11/27/8.jpg', '45', 'http://www.baidu.com', '4.9', '11', '0', '0', '', '', 'video/img/2017/11/27/8_yhqk0Zc.jpg', '', '', '', '', '', '7', '0', '0', '1', '0', '0', '2017-11-27 15:47:59.754000', '2017-11-28 17:33:29.099000', '3', '0', '11', '匿名');
