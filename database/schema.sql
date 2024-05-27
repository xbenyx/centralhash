-- Common table creation script for User table

{% if DATABASE_TYPE == 0 %}
-- MySQL
CREATE TABLE IF NOT EXISTS `Users` (
  `user_id` INT AUTO_INCREMENT PRIMARY KEY,
  `username` VARCHAR(100) NOT NULL UNIQUE,
  `f_name` VARCHAR(150) NULL,
  `l_name` VARCHAR(150) NULL,
  `email` VARCHAR(150) NOT NULL,
  `password` VARCHAR(256) NOT NULL,
  `remember_token` VARCHAR(256) NULL,
  `status` BOOLEAN NOT NULL,
  `updated_at` BIGINT NOT NULL,
  `created_at` BIGINT NOT NULL,
  `session_max` INT NOT NULL,
  `perm_group_id` INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `UserStatus` (
  `user_status_id` INT AUTO_INCREMENT PRIMARY KEY,
  `name` NVARCHAR(150) NOT NULL
);

{% elif DATABASE_TYPE == 1 %}
-- MSSQL
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Users' AND xtype='U')
BEGIN
    CREATE TABLE [Users] (
        [user_id] INT IDENTITY(1,1) PRIMARY KEY,
        [username] NVARCHAR(100) NOT NULL UNIQUE,
        [f_name] NVARCHAR(150) NULL,
        [l_name] NVARCHAR(150) NULL,
        [email] NVARCHAR(150) NOT NULL,
        [password] NVARCHAR(256) NOT NULL,
        [remember_token] NVARCHAR(256) NULL,
        [status] BIT NOT NULL,
        [updated_at] BIGINT NOT NULL,
        [created_at] BIGINT NOT NULL,
        [session_max] INT NOT NULL,
        [perm_group_id] INT NOT NULL
    );
END;

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='UserStatus' AND xtype='U')
BEGIN
    CREATE TABLE [UserStatus] (
        [user_status_id] INT IDENTITY(1,1) PRIMARY KEY,
        [name] NVARCHAR(150) NOT NULL
    );
END;

{% elif DATABASE_TYPE == 2 %}
-- PostgreSQL
CREATE TABLE IF NOT EXISTS "Users" (
  "user_id" SERIAL PRIMARY KEY,
  "username" VARCHAR(100) NOT NULL UNIQUE,
  "f_name" VARCHAR(150) NULL,
  "l_name" VARCHAR(150) NULL,
  "email" VARCHAR(150) NOT NULL,
  "password" VARCHAR(256) NOT NULL,
  "remember_token" VARCHAR(256) NULL,
  "status" BOOLEAN NOT NULL,
  "updated_at" BIGINT NOT NULL,
  "created_at" BIGINT NOT NULL,
  "session_max" INT NOT NULL,
  "perm_group_id" INT NOT NULL
);

CREATE TABLE IF NOT EXISTS "UserStatus" (
  "user_status_id" SERIAL PRIMARY KEY,
  "name" VARCHAR(150) NOT NULL
);

{% endif %}
