DROP DATABASE IF EXISTS ems;
CREATE  DATABASE ems DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE ems;

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for ems_department
-- ----------------------------
DROP TABLE IF EXISTS `ems_department`;
CREATE TABLE `ems_department` (
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL COMMENT '组名称',
  `parent_id` int(11) DEFAULT NULL COMMENT '上级部门ID',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `parent_id` (`parent_id`),
  CONSTRAINT `ems_department_ibfk_1` FOREIGN KEY (`parent_id`) REFERENCES `ems_department` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of ems_department
-- ----------------------------
BEGIN;
INSERT INTO `ems_department` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 1, '伏羲实验室', NULL);
INSERT INTO `ems_department` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 2, '用户画像组', 1);
INSERT INTO `ems_department` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 3, '图像组', 1);
INSERT INTO `ems_department` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 4, '平台架构组', 1);
INSERT INTO `ems_department` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 5, '强化学习组', 1);
INSERT INTO `ems_department` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 6, '虚拟人组', 1);
INSERT INTO `ems_department` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 7, '数据组', 4);
INSERT INTO `ems_department` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 8, 'web开发组', 4);
INSERT INTO `ems_department` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 9, '丹炉组', 4);
COMMIT;

-- ----------------------------
-- Table structure for ems_employee
-- ----------------------------
DROP TABLE IF EXISTS `ems_employee`;
CREATE TABLE `ems_employee` (
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL COMMENT '人员姓名',
  `_gender` int(11) DEFAULT NULL COMMENT '性别',
  `department_id` int(11) DEFAULT NULL COMMENT '部门ID',
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `ems_employee_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `ems_department` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of ems_employee
-- ----------------------------
BEGIN;
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 1, '刘丽丽', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 2, '施凯', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 3, '杜凯', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 4, '郭旭', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 5, '周慧', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 6, '徐慧', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 7, '温文', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 8, '秦璐', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 9, '孙凤英', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 10, '王杰', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 11, '余倩', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 12, '杨丽华', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 13, '韩彬', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 14, '吕飞', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 15, '何丽华', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 16, '朱玉', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 17, '杜柳', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 18, '朱建军', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 19, '李玲', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 20, '熊坤', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 21, '贾林', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 22, '陈瑞', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 23, '陈飞', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:24', '2020-03-18 16:00:24', 24, '孔玉华', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 25, '龚淑兰', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 26, '许杨', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 27, '陈志强', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 28, '余勇', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 29, '杜玉兰', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 30, '黄东', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 31, '李艳', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 32, '谭淑英', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 33, '刘琴', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 34, '金杨', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 35, '魏斌', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 36, '陈红', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 37, '余桂荣', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 38, '周红', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 39, '张刚', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 40, '周杨', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 41, '曾淑英', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 42, '冯璐', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 43, '王阳', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 44, '谭燕', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 45, '邵璐', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 46, '陈丽华', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 47, '魏秀荣', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 48, '周桂荣', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 49, '王峰', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 50, '冉婷婷', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 51, '楚洁', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 52, '母丹', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 53, '葛俊', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 54, '白岩', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 55, '魏秀华', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 56, '易勇', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 57, '刘俊', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 58, '杨伟', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:25', '2020-03-18 16:00:25', 59, '孟柳', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 60, '石柳', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 61, '陈凤英', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 62, '寇刚', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 63, '郑欢', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 64, '万勇', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 65, '赵超', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 66, '张林', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 67, '张杰', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 68, '李倩', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 69, '郑洋', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 70, '张华', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 71, '吴志强', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 72, '向凯', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 73, '徐鑫', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 74, '陈丽丽', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 75, '陈梅', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 76, '冯红', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 77, '靳丽', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 78, '陈明', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 79, '熊军', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 80, '杨帅', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 81, '范雷', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 82, '冯桂荣', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 83, '李俊', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 84, '王欢', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 85, '王欢', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 86, '陈洋', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 87, '林桂花', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 88, '何凯', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 89, '侯秀芳', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 90, '林静', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 91, '陆坤', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 92, '赵桂芳', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 93, '栾龙', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:26', '2020-03-18 16:00:26', 94, '华斌', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:27', '2020-03-18 16:00:27', 95, '刘涛', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:27', '2020-03-18 16:00:27', 96, '吕丽华', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:27', '2020-03-18 16:00:27', 97, '田金凤', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:27', '2020-03-18 16:00:27', 98, '倪丹', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:27', '2020-03-18 16:00:27', 99, '纪凤英', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-18 16:00:27', '2020-03-18 16:00:27', 100, '林秀兰', 1, 7);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
