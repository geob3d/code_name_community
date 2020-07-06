CREATE TABLE `customer` (
  `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `lastname` VARCHAR(255) NOT NULL,
  `firstname` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `create_time` DATETIME NOT NULL,
  `last_login` VARCHAR(255) NOT NULL,
  `usertype` VARCHAR(255) NOT NULL,
  `username` VARCHAR(10) NOT NULL
);

CREATE TABLE `employee` (
  `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `firstname` VARCHAR(255) NOT NULL,
  `lastname` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `jobtitle` VARCHAR(255) NOT NULL,
  `storelocation` VARCHAR(255) NOT NULL
);

CREATE TABLE `inventory` (
  `id` INTEGER PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE `product` (
  `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `categoryid` VARCHAR(255) NOT NULL
);

CREATE TABLE `productcategory` (
  `id` INTEGER PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE `purchase` (
  `id` INTEGER PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE `storeinfo` (
  `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL
);

CREATE TABLE `storelocation` (
  `locationid` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `address` VARCHAR(255) NOT NULL,
  `city` VARCHAR(255) NOT NULL,
  `state` VARCHAR(255) NOT NULL,
  `country` VARCHAR(255) NOT NULL,
  `zipcode` VARCHAR(255) NOT NULL,
  `phonenumber` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `storeid` INTEGER
);

CREATE INDEX `idx_storelocation__storeid` ON `storelocation` (`storeid`);

ALTER TABLE `storelocation` ADD CONSTRAINT `fk_storelocation__storeid` FOREIGN KEY (`storeid`) REFERENCES `storeinfo` (`id`) ON DELETE SET NULL