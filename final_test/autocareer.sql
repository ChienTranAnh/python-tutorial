/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 50733
 Source Host           : localhost:3306
 Source Schema         : autocareer

 Target Server Type    : MySQL
 Target Server Version : 50733
 File Encoding         : 65001

 Date: 08/10/2024 22:07:29
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for employees
-- ----------------------------
DROP TABLE IF EXISTS `employees`;
CREATE TABLE `employees`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'họ tên nhân viên',
  `birth` date NULL DEFAULT NULL COMMENT 'ngày tháng năm sinh',
  `sex` tinyint(1) NULL DEFAULT NULL COMMENT 'giới tính',
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'thư điện tử',
  `phone` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'điện thoại liên hệ',
  `position` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'chức vụ',
  `enterprise_id` int(11) NULL DEFAULT NULL COMMENT 'mã doanh nghiệp',
  `user_id` int(11) NULL DEFAULT NULL COMMENT 'mã tài khoản',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `email`(`email`) USING BTREE,
  INDEX `enterprise_id`(`enterprise_id`) USING BTREE,
  INDEX `user_id`(`user_id`) USING BTREE,
  INDEX `ix_employees_id`(`id`) USING BTREE,
  CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`enterprise_id`) REFERENCES `enterprises` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `employees_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of employees
-- ----------------------------
INSERT INTO `employees` VALUES (1, 'choén', '1991-01-19', 1, 'tran.chien@jvb.com', '0914912019', 'developer', 3, 1);
INSERT INTO `employees` VALUES (3, 'rose', '1991-10-16', 0, 'rose@gmail.com', 'string', 'string', 1, NULL);
INSERT INTO `employees` VALUES (4, 'Monlonton', '2019-12-06', 1, 'mon@monlonton.com', '091491', 'string', 2, NULL);

-- ----------------------------
-- Table structure for enterprises
-- ----------------------------
DROP TABLE IF EXISTS `enterprises`;
CREATE TABLE `enterprises`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'tên công ty',
  `address` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'địa chỉ công ty',
  `phone` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'điện thoại công ty',
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'thư điện tử',
  `password` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'mật khẩu đăng nhập',
  `website` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'trang web công ty',
  `industry` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'ngành nghề',
  `scale` int(11) NULL DEFAULT NULL COMMENT 'quy mô công ty',
  `about` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'giới thiệu công ty',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `email`(`email`) USING BTREE,
  INDEX `ix_enterprises_id`(`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of enterprises
-- ----------------------------
INSERT INTO `enterprises` VALUES (1, 'chay phuc an', 'thuy phuong', '(+84) 96', 'le@gmail.com', '$2b$12$TcHEzJTsJ7Pi2u/pBKhl4edFmJrTyF6FreiX/xdQmUJqYKDrViueK', 'chayphucan.com', 'ecomerce', 3, 'binh binh pham pham cho doi hanh phuc an nhien');
INSERT INTO `enterprises` VALUES (2, 'jvb', 'roman plaza', '(+84) 243', 'jvb@jvb-corp.com', '$2b$12$klGCLlYuHgS0mBLTG.cgXec0E9roG9d96CfyQ3MpJNKYXoUfaYWJa', 'cjvb-corp.com', 'information technology', 100, 'bring you a distinctive solution');
INSERT INTO `enterprises` VALUES (3, 'thai minh corp', 'tho thap', '(+84) 2434', 'tmp@tmp.com', '$2b$12$X3sywX9vIp.Jq7C5r8UFqOjN.1rNnLlyRYgbBBAahSpFksMxJGeiS', 'tmp.com', 'phamarcy', 1000, '. . . .');

-- ----------------------------
-- Table structure for recruitments
-- ----------------------------
DROP TABLE IF EXISTS `recruitments`;
CREATE TABLE `recruitments`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_title` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'tiêu đề tin tuyển dụng',
  `job_description` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT 'Nội dung',
  `skill_required` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT 'yêu cầu ứng viên',
  `job_position` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'vị trí tuyển dụng',
  `location` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'nơi làm việc',
  `salary_range` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'mức lương',
  `job_type` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'loại hình công việc',
  `enterprise_id` int(11) NULL DEFAULT NULL COMMENT 'mã công ty',
  `start_date` date NULL DEFAULT NULL COMMENT 'ngày đăng tuyển',
  `end_date` date NULL DEFAULT NULL COMMENT 'ngày hết hạn',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `enterprise_id`(`enterprise_id`) USING BTREE,
  INDEX `ix_recruitments_id`(`id`) USING BTREE,
  CONSTRAINT `recruitments_ibfk_1` FOREIGN KEY (`enterprise_id`) REFERENCES `enterprises` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of recruitments
-- ----------------------------

-- ----------------------------
-- Table structure for students
-- ----------------------------
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'tên sinh viên',
  `last_name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'họ đệm sinh viên',
  `birth` date NULL DEFAULT NULL COMMENT 'ngày tháng năm sinh',
  `sex` tinyint(1) NULL DEFAULT NULL COMMENT 'giới tính',
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'thư điện tử',
  `phone` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'điện thoại liên hệ',
  `classes` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'lớp',
  `major` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'nghành học',
  `graduation_year` int(11) NULL DEFAULT NULL COMMENT 'năm tốt nghiệp',
  `university_id` int(11) NULL DEFAULT NULL COMMENT 'mã trường đại học',
  `skill` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'kỹ năng',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `email`(`email`) USING BTREE,
  INDEX `university_id`(`university_id`) USING BTREE,
  INDEX `ix_students_id`(`id`) USING BTREE,
  CONSTRAINT `students_ibfk_1` FOREIGN KEY (`university_id`) REFERENCES `universities` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of students
-- ----------------------------

-- ----------------------------
-- Table structure for ung_tuyen
-- ----------------------------
DROP TABLE IF EXISTS `ung_tuyen`;
CREATE TABLE `ung_tuyen`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `recruitment_id` int(11) NULL DEFAULT NULL COMMENT 'mã tin tuyển dụng',
  `students_id` int(11) NULL DEFAULT NULL COMMENT 'mã sinh viên',
  `date_apply` date NULL DEFAULT NULL COMMENT 'ngày ứng tuyển',
  `status` tinyint(4) NULL DEFAULT NULL COMMENT 'trạng thái 0: nhà tuyển dụng chưa đọc, 1: nhà tuyển dụng đã đọc, 2: từ chối, 3: chấp nhận',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `recruitment_id`(`recruitment_id`) USING BTREE,
  INDEX `students_id`(`students_id`) USING BTREE,
  INDEX `ix_ung_tuyen_id`(`id`) USING BTREE,
  CONSTRAINT `ung_tuyen_ibfk_1` FOREIGN KEY (`recruitment_id`) REFERENCES `recruitments` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `ung_tuyen_ibfk_2` FOREIGN KEY (`students_id`) REFERENCES `students` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of ung_tuyen
-- ----------------------------

-- ----------------------------
-- Table structure for universities
-- ----------------------------
DROP TABLE IF EXISTS `universities`;
CREATE TABLE `universities`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uni_name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'tên trường',
  `address` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'địa chỉ',
  `phone` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'điện thoại',
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'thư điện tử',
  `website` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'trang web trường đại học',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `email`(`email`) USING BTREE,
  INDEX `ix_universities_id`(`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of universities
-- ----------------------------

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'họ tên người dùng',
  `birth` date NULL DEFAULT NULL COMMENT 'ngày tháng năm sinh',
  `user_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'tên đăng nhập',
  `password` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'mật khẩu đăng nhập',
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'thư điện tử',
  `role` int(11) NULL DEFAULT NULL COMMENT 'quyền tài khoản',
  `acc_type` int(11) NULL DEFAULT NULL COMMENT 'loại tài khoản',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `email`(`email`) USING BTREE,
  INDEX `ix_users_id`(`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (1, 'choens', '1991-01-19', 'chienchoen', 'chienchoen', 'tran.chien@jvb.com', 0, 0);
INSERT INTO `users` VALUES (2, 'lon ton', '2019-12-06', 'monlonton', '$2b$12$GXzhR7MpRXaZ2.umYN9hh.kjPyrYZn6cY9o0DrPuwLxpir.9Jl1dG', 'mon@lonton.com', 1, 0);

SET FOREIGN_KEY_CHECKS = 1;
