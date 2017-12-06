/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : osvr_cms20170620

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2017-11-30 10:48:26
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=98 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2017-06-26 10:46:35.097000');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2017-06-26 10:46:35.790000');
INSERT INTO `django_migrations` VALUES ('3', 'filer', '0001_initial', '2017-06-26 10:46:37.393000');
INSERT INTO `django_migrations` VALUES ('4', 'filer', '0002_auto_20150606_2003', '2017-06-26 10:46:37.501000');
INSERT INTO `django_migrations` VALUES ('5', 'filer', '0003_thumbnailoption', '2017-06-26 10:46:37.547000');
INSERT INTO `django_migrations` VALUES ('6', 'filer', '0004_auto_20160328_1434', '2017-06-26 10:46:37.644000');
INSERT INTO `django_migrations` VALUES ('7', 'filer', '0005_auto_20160623_1425', '2017-06-26 10:46:38.006000');
INSERT INTO `django_migrations` VALUES ('8', 'filer', '0006_auto_20160623_1627', '2017-06-26 10:46:38.099000');
INSERT INTO `django_migrations` VALUES ('9', 'filer', '0007_auto_20161016_1055', '2017-06-26 10:46:38.127000');
INSERT INTO `django_migrations` VALUES ('10', 'CMS', '0001_initial', '2017-06-26 10:46:40.308000');
INSERT INTO `django_migrations` VALUES ('11', 'admin', '0001_initial', '2017-06-26 10:46:40.504000');
INSERT INTO `django_migrations` VALUES ('12', 'admin', '0002_logentry_remove_auto_add', '2017-06-26 10:46:40.556000');
INSERT INTO `django_migrations` VALUES ('13', 'contenttypes', '0002_remove_content_type_name', '2017-06-26 10:46:40.797000');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0002_alter_permission_name_max_length', '2017-06-26 10:46:40.940000');
INSERT INTO `django_migrations` VALUES ('15', 'auth', '0003_alter_user_email_max_length', '2017-06-26 10:46:41.078000');
INSERT INTO `django_migrations` VALUES ('16', 'auth', '0004_alter_user_username_opts', '2017-06-26 10:46:41.114000');
INSERT INTO `django_migrations` VALUES ('17', 'auth', '0005_alter_user_last_login_null', '2017-06-26 10:46:41.203000');
INSERT INTO `django_migrations` VALUES ('18', 'auth', '0006_require_contenttypes_0002', '2017-06-26 10:46:41.212000');
INSERT INTO `django_migrations` VALUES ('19', 'auth', '0007_alter_validators_add_error_messages', '2017-06-26 10:46:41.258000');
INSERT INTO `django_migrations` VALUES ('20', 'auth', '0008_alter_user_username_max_length', '2017-06-26 10:46:41.353000');
INSERT INTO `django_migrations` VALUES ('21', 'authtoken', '0001_initial', '2017-06-26 10:46:41.500000');
INSERT INTO `django_migrations` VALUES ('22', 'authtoken', '0002_auto_20160226_1747', '2017-06-26 10:46:41.735000');
INSERT INTO `django_migrations` VALUES ('23', 'easy_thumbnails', '0001_initial', '2017-06-26 10:46:42.036000');
INSERT INTO `django_migrations` VALUES ('24', 'easy_thumbnails', '0002_thumbnaildimensions', '2017-06-26 10:46:42.154000');
INSERT INTO `django_migrations` VALUES ('25', 'sessions', '0001_initial', '2017-06-26 10:46:42.219000');
INSERT INTO `django_migrations` VALUES ('26', 'statistics', '0001_initial', '2017-06-26 10:46:42.272000');
INSERT INTO `django_migrations` VALUES ('27', 'statistics', '0002_appheart_interval', '2017-06-26 13:37:46.833000');
INSERT INTO `django_migrations` VALUES ('28', 'statistics', '0003_auto_20170626_1339', '2017-06-26 13:39:04.698000');
INSERT INTO `django_migrations` VALUES ('29', 'sites', '0001_initial', '2017-06-27 13:05:54.292000');
INSERT INTO `django_migrations` VALUES ('30', 'flatpages', '0001_initial', '2017-06-27 13:05:54.589000');
INSERT INTO `django_migrations` VALUES ('31', 'sites', '0002_alter_domain_unique', '2017-06-27 13:05:54.632000');
INSERT INTO `django_migrations` VALUES ('32', 'statistics', '0004_auto_20170627_1305', '2017-06-27 13:05:54.654000');
INSERT INTO `django_migrations` VALUES ('33', 'dash', '0001_initial', '2017-06-27 13:24:41.419000');
INSERT INTO `django_migrations` VALUES ('34', 'dash', '0002_auto_20170126_1816', '2017-06-27 13:24:41.621000');
INSERT INTO `django_migrations` VALUES ('35', 'dash', '0003_auto_20170311_1449', '2017-06-27 13:24:42.267000');
INSERT INTO `django_migrations` VALUES ('36', 'statistics', '0005_appinstall', '2017-06-28 09:38:17.993000');
INSERT INTO `django_migrations` VALUES ('37', 'statistics', '0006_appheart_onfirst', '2017-06-28 11:32:34.743000');
INSERT INTO `django_migrations` VALUES ('38', 'CMS', '0002_manufactor_logo_path', '2017-07-03 09:54:08.016000');
INSERT INTO `django_migrations` VALUES ('39', 'CMS', '0003_auto_20171024_1440', '2017-10-24 14:40:12.093000');
INSERT INTO `django_migrations` VALUES ('40', 'CMS', '0004_video_sort', '2017-10-24 14:47:35.588000');
INSERT INTO `django_migrations` VALUES ('41', 'CMS', '0005_auto_20171024_1456', '2017-10-24 14:56:31.744000');
INSERT INTO `django_migrations` VALUES ('42', 'CMS', '0006_auto_20171024_1502', '2017-10-24 15:03:00.866000');
INSERT INTO `django_migrations` VALUES ('43', 'CMS', '0007_auto_20171024_1513', '2017-10-24 15:13:11.798000');
INSERT INTO `django_migrations` VALUES ('44', 'CMS', '0008_auto_20171024_1513', '2017-10-24 15:13:38.725000');
INSERT INTO `django_migrations` VALUES ('45', 'CMS', '0009_auto_20171024_1514', '2017-10-24 15:14:19.241000');
INSERT INTO `django_migrations` VALUES ('46', 'CMS', '0010_auto_20171024_1515', '2017-10-24 15:15:12.647000');
INSERT INTO `django_migrations` VALUES ('47', 'CMS', '0011_auto_20171024_1515', '2017-10-24 15:15:53.614000');
INSERT INTO `django_migrations` VALUES ('48', 'CMS', '0012_auto_20171024_1516', '2017-10-24 15:16:34.139000');
INSERT INTO `django_migrations` VALUES ('49', 'CMS', '0013_imagegenres_imagesort', '2017-10-24 15:25:51.046000');
INSERT INTO `django_migrations` VALUES ('50', 'CMS', '0014_image', '2017-10-24 16:37:53.327000');
INSERT INTO `django_migrations` VALUES ('51', 'CMS', '0015_auto_20171024_1642', '2017-10-24 16:42:16.806000');
INSERT INTO `django_migrations` VALUES ('52', 'CMS', '0016_auto_20171024_1703', '2017-10-24 17:03:12.255000');
INSERT INTO `django_migrations` VALUES ('53', 'CMS', '0017_auto_20171024_1703', '2017-10-24 17:03:37.245000');
INSERT INTO `django_migrations` VALUES ('54', 'CMS', '0018_auto_20171025_0946', '2017-10-25 09:47:12.108000');
INSERT INTO `django_migrations` VALUES ('55', 'CMS', '0019_fittings', '2017-10-25 09:53:19.809000');
INSERT INTO `django_migrations` VALUES ('56', 'CMS', '0020_game_fittings', '2017-10-25 09:56:37.530000');
INSERT INTO `django_migrations` VALUES ('57', 'CMS', '0021_game_playcount', '2017-10-25 09:58:31.126000');
INSERT INTO `django_migrations` VALUES ('58', 'CMS', '0022_auto_20171025_1341', '2017-10-25 13:47:17.453000');
INSERT INTO `django_migrations` VALUES ('59', 'CMS', '0023_auto_20171025_1342', '2017-10-25 13:47:17.623000');
INSERT INTO `django_migrations` VALUES ('60', 'CMS', '0024_auto_20171025_1343', '2017-10-25 13:47:17.806000');
INSERT INTO `django_migrations` VALUES ('61', 'CMS', '0025_auto_20171025_1343', '2017-10-25 13:47:17.961000');
INSERT INTO `django_migrations` VALUES ('62', 'CMS', '0026_auto_20171025_1345', '2017-10-25 13:47:18.153000');
INSERT INTO `django_migrations` VALUES ('63', 'CMS', '0027_auto_20171025_1346', '2017-10-25 13:47:18.374000');
INSERT INTO `django_migrations` VALUES ('64', 'CMS', '0028_auto_20171025_1347', '2017-10-25 13:47:57.220000');
INSERT INTO `django_migrations` VALUES ('65', 'CMS', '0029_auto_20171025_1413', '2017-10-25 14:17:31.890000');
INSERT INTO `django_migrations` VALUES ('66', 'CMS', '0030_auto_20171025_1414', '2017-10-25 14:17:32.073000');
INSERT INTO `django_migrations` VALUES ('67', 'CMS', '0031_auto_20171025_1415', '2017-10-25 14:17:32.253000');
INSERT INTO `django_migrations` VALUES ('68', 'CMS', '0032_auto_20171025_1416', '2017-10-25 14:17:32.431000');
INSERT INTO `django_migrations` VALUES ('69', 'CMS', '0033_auto_20171025_1417', '2017-10-25 14:17:32.673000');
INSERT INTO `django_migrations` VALUES ('70', 'CMS', '0034_auto_20171025_1445', '2017-10-25 14:45:35.360000');
INSERT INTO `django_migrations` VALUES ('71', 'statistics', '0007_auto_20171025_1028', '2017-10-25 15:15:35.993000');
INSERT INTO `django_migrations` VALUES ('72', 'CMS', '0035_auto_20171026_0930', '2017-10-26 09:30:54.174000');
INSERT INTO `django_migrations` VALUES ('73', 'CMS', '0036_auto_20171026_1105', '2017-10-26 11:05:10.464000');
INSERT INTO `django_migrations` VALUES ('74', 'CMS', '0037_auto_20171120_1423', '2017-11-20 14:24:03.101000');
INSERT INTO `django_migrations` VALUES ('75', 'CMS', '0038_remove_imagesort_folder_id', '2017-11-20 15:18:58.485000');
INSERT INTO `django_migrations` VALUES ('76', 'CMS', '0039_auto_20171120_1537', '2017-11-20 15:37:24.506000');
INSERT INTO `django_migrations` VALUES ('77', 'CMS', '0040_imagesort_folder_id', '2017-11-20 15:55:05.428000');
INSERT INTO `django_migrations` VALUES ('78', 'captcha', '0001_initial', '2017-11-21 13:30:29.090000');
INSERT INTO `django_migrations` VALUES ('79', 'CMS', '0041_auto_20171122_0836', '2017-11-22 08:37:00.961000');
INSERT INTO `django_migrations` VALUES ('87', 'CMS', '0041_auto_20171124_1405', '2017-11-24 14:05:25.281000');
INSERT INTO `django_migrations` VALUES ('88', 'CMS', '0042_auto_20171124_1407', '2017-11-24 14:08:00.145000');
INSERT INTO `django_migrations` VALUES ('89', 'CMS', '0043_usertoken_expire_date', '2017-11-24 14:10:15.095000');
INSERT INTO `django_migrations` VALUES ('90', 'CMS', '0044_auto_20171127_0935', '2017-11-27 09:35:25.031000');
INSERT INTO `django_migrations` VALUES ('91', 'CMS', '0045_auto_20171127_1041', '2017-11-27 10:41:29.283000');
INSERT INTO `django_migrations` VALUES ('92', 'CMS', '0046_video_starring', '2017-11-27 16:11:02.029000');
INSERT INTO `django_migrations` VALUES ('93', 'CMS', '0047_goodsimage', '2017-11-27 16:28:25.712000');
INSERT INTO `django_migrations` VALUES ('94', 'CMS', '0048_auto_20171127_1639', '2017-11-27 16:39:39.135000');
INSERT INTO `django_migrations` VALUES ('95', 'CMS', '0049_delete_goodsimage', '2017-11-27 16:48:41.685000');
INSERT INTO `django_migrations` VALUES ('96', 'CMS', '0050_auto_20171127_1651', '2017-11-27 16:51:17.574000');
INSERT INTO `django_migrations` VALUES ('97', 'CMS', '0051_image_sorting', '2017-11-27 17:15:37.418000');
