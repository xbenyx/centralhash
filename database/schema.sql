CREATE TABLE IF NOT EXISTS `User` (
  `userId`             INT AUTO_INCREMENT PRIMARY KEY,
  `username`           VARCHAR(100) NOT NULL UNIQUE,
  `email`              VARCHAR(150) NOT NULL,
  `passwordHash`       VARCHAR(256) NOT NULL,
  `passwordSalt`       VARCHAR(256) NOT NULL,
  `isValid`            BOOLEAN NOT NULL,
  `isComputedPassword` BOOLEAN NOT NULL,
  `lastLoginDate`      BIGINT NOT NULL,
  `registeredSince`    BIGINT NOT NULL,
  `sessionLifetime`    INT NOT NULL,
  `rightGroupId`       INT NOT NULL
);