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
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL COMMENT '组名称',
  `parent_id` int(11) DEFAULT NULL COMMENT '上级部门ID',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of ems_department
-- ----------------------------
BEGIN;
INSERT INTO `ems_department` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 1, '伏羲实验室', NULL);
INSERT INTO `ems_department` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 2, '用户画像组', 1);
INSERT INTO `ems_department` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 3, '图像组', 1);
INSERT INTO `ems_department` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 4, '平台架构组', 1);
INSERT INTO `ems_department` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 5, '强化学习组', 1);
INSERT INTO `ems_department` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 6, '虚拟人组', 1);
INSERT INTO `ems_department` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 7, '数据组', 4);
INSERT INTO `ems_department` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 8, 'web开发组', 4);
INSERT INTO `ems_department` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 9, '丹炉组', 4);
COMMIT;

-- ----------------------------
-- Table structure for ems_employee
-- ----------------------------
DROP TABLE IF EXISTS `ems_employee`;
CREATE TABLE `ems_employee` (
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL COMMENT '人员姓名',
  `_gender` smallint(6) DEFAULT NULL COMMENT '性别',
  `department_id` int(11) DEFAULT NULL COMMENT '部门ID',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of ems_employee
-- ----------------------------
BEGIN;
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 1, '刘兰英', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 2, '金楠', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 3, '吕玉英', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 4, '王兵', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 5, '由杨', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 6, '邓颖', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 7, '陈帆', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 8, '娄建国', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 9, '刘桂芝', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 10, '胡玲', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 11, '陈峰', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 12, '叶欢', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 13, '陈云', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 14, '许斌', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 15, '李秀梅', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 16, '饶桂珍', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 17, '叶淑英', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 18, '游桂芝', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 19, '刘淑兰', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 20, '何浩', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 21, '宋秀华', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 22, '刘桂英', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 23, '刘旭', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 24, '郭想', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 25, '孙婷', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 26, '吴辉', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 27, '袁玉梅', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:50', '2020-03-13 19:36:50', 1, 28, '郑秀珍', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 29, '程云', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 30, '刘娜', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 31, '杜霞', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 32, '李鹏', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 33, '姜桂兰', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 34, '黄淑珍', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 35, '沈超', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 36, '王磊', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 37, '徐红梅', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 38, '宣慧', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 39, '王建', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 40, '蒋秀荣', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 41, '王红霞', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 42, '罗磊', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 43, '萧玉华', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 44, '刘英', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 45, '余刚', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 46, '张淑珍', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 47, '王玉', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 48, '刘鑫', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 49, '李欣', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 50, '王健', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 51, '洪旭', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 52, '王海燕', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 53, '史洁', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 54, '苏文', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 55, '赵燕', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 56, '胡春梅', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 57, '高军', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 58, '张丹', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 59, '王欣', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 60, '路瑞', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 61, '王博', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 62, '梁晶', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 63, '陈建华', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:51', '2020-03-13 19:36:51', 1, 64, '邱佳', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 65, '张杰', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 66, '张楠', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 67, '何艳', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 68, '蒋建军', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 69, '李婷婷', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 70, '鞠红', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 71, '张桂英', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 72, '蒲波', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 73, '吴畅', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 74, '郭倩', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 75, '邓龙', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 76, '常平', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 77, '张燕', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 78, '胡红梅', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 79, '李玉英', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 80, '谢凯', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 81, '朱平', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 82, '薛桂荣', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 83, '杜秀梅', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 84, '翁阳', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 85, '陈淑兰', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 86, '潘芳', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 87, '林楠', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 88, '魏金凤', 0, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 89, '张洁', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 90, '李畅', 0, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 91, '林利', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 92, '宋璐', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 93, '李凤英', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 94, '朱刚', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 95, '吴霞', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 96, '汪岩', 0, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 97, '丛鹏', 1, 7);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 98, '夏丽华', 1, 8);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:52', '2020-03-13 19:36:52', 1, 99, '孙燕', 1, 9);
INSERT INTO `ems_employee` VALUES ('2020-03-13 19:36:53', '2020-03-13 19:36:53', 1, 100, '王晨', 1, 9);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
