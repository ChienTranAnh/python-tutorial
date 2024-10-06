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

 Date: 05/10/2024 23:36:19
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for businesses
-- ----------------------------
DROP TABLE IF EXISTS `businesses`;
CREATE TABLE `businesses`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'tên công ty',
  `address` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'địa chỉ',
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'thư điện tử',
  `industry` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'ngành nghề',
  `scale` int(11) NULL DEFAULT NULL COMMENT 'quy mô',
  `description` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT 'mô tả',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `email`(`email`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = 'thông tin doanh nghiệp' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of businesses
-- ----------------------------

-- ----------------------------
-- Table structure for recruitment
-- ----------------------------
DROP TABLE IF EXISTS `recruitment`;
CREATE TABLE `recruitment`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `businesses_id` int(11) NULL DEFAULT NULL COMMENT 'doanh nghiệp id',
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'tiêu đề doanh nghiệp',
  `description` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT 'mô tả công việc',
  `candidate` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT 'yêu cầu ứng viên',
  `salary` decimal(15, 2) NULL DEFAULT NULL COMMENT 'mức lương',
  `job_position` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'chức vụ',
  `start_date` date NULL DEFAULT NULL COMMENT 'ngày đăng tuyển',
  `end_date` date NULL DEFAULT NULL COMMENT 'ngày hết hạn',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `businesses_id`(`businesses_id`) USING BTREE,
  CONSTRAINT `recruitment_ibfk_1` FOREIGN KEY (`businesses_id`) REFERENCES `businesses` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = 'thông tin tuyển dụng' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of recruitment
-- ----------------------------

-- ----------------------------
-- Table structure for students
-- ----------------------------
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'tên',
  `last_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'họ đệm',
  `birth` date NULL DEFAULT NULL,
  `sex` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'giới tính 0: nữ, 1: nam',
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'thử điện tử',
  `phone` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'điện thoại liên hệ',
  `class` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'lớp',
  `major` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'ngành học',
  `university_id` int(11) NULL DEFAULT NULL COMMENT 'mã trường đại học',
  `skill` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT 'kỹ năng của bản thân',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `university_id`(`university_id`) USING BTREE,
  CONSTRAINT `students_ibfk_1` FOREIGN KEY (`university_id`) REFERENCES `university` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = 'thông tin sinh viên' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of students
-- ----------------------------

-- ----------------------------
-- Table structure for ung_tuyen
-- ----------------------------
DROP TABLE IF EXISTS `ung_tuyen`;
CREATE TABLE `ung_tuyen`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `recruitment_id` int(11) NULL DEFAULT NULL COMMENT 'thông tin tuyển dụng',
  `students_id` int(11) NULL DEFAULT NULL COMMENT 'thông tin sinh viên',
  `date_apply` date NULL DEFAULT NULL COMMENT 'ngày ứng tuyển',
  `status` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'trạng thái 0: nhà tuyển dụng chưa đọc, 1: nhà tuyển dụng đã đọc, 2: từ chối, 3: chấp nhận',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `recruitment_id`(`recruitment_id`) USING BTREE,
  INDEX `students_id`(`students_id`) USING BTREE,
  CONSTRAINT `ung_tuyen_ibfk_1` FOREIGN KEY (`recruitment_id`) REFERENCES `recruitment` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `ung_tuyen_ibfk_2` FOREIGN KEY (`students_id`) REFERENCES `students` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of ung_tuyen
-- ----------------------------

-- ----------------------------
-- Table structure for university
-- ----------------------------
DROP TABLE IF EXISTS `university`;
CREATE TABLE `university`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uni_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'tên trường',
  `address` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'địa chỉ trường',
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'thư điện tử',
  `website` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'web trường',
  `type` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'loại trường',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = 'thông tin trường đại học - cao đẳng' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of university
-- ----------------------------

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'tên đăng nhập',
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'mật khẩu đăng nhập',
  `role` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'quyền tài khoản',
  `acc_type` int(11) NULL DEFAULT NULL COMMENT 'loại tài khoản',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = 'tài khoản của hệ thống autocareer' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
