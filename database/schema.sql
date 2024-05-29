{% if DATABASE_TYPE == 0 %}
-- MySQL Creation
CREATE TABLE IF NOT EXISTS `Users` (
  `user_id` INT AUTO_INCREMENT PRIMARY KEY,
  `username` VARCHAR(50) NOT NULL UNIQUE,
  `f_name` VARCHAR(50) NULL,
  `l_name` VARCHAR(50) NULL,
  `email` VARCHAR(150) NOT NULL,
  `password` VARCHAR(256) NOT NULL,
  `remember_token` VARCHAR(256) NULL,
  `status` BOOLEAN NOT NULL,
  `updated_at` BIGINT NOT NULL,
  `created_at` BIGINT NOT NULL,
  `session_max` INT NOT NULL,
  `role` INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `UserStatus` (
  `user_status_id` INT AUTO_INCREMENT PRIMARY KEY,
  `name` NVARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS `Logs` (
    `log_id` INT AUTO_INCREMENT PRIMARY KEY,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `status` VARCHAR(255),
    `user_id` INT,
    `type` VARCHAR(255),
    `message` TEXT,
    FOREIGN KEY (`user_id`) REFERENCES `Users`(`user_id`)
);

-- MySQL Alter, foreign keys

-- MySQL insert initial data

{% elif DATABASE_TYPE == 1 %}
-- MSSQL
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Users' AND xtype='U')
BEGIN
    CREATE TABLE [Users] (
        [user_id] INT IDENTITY(1,1) PRIMARY KEY,
        [username] NVARCHAR(50) NOT NULL UNIQUE,
        [f_name] NVARCHAR(50) NULL,
        [l_name] NVARCHAR(50) NULL,
        [email] NVARCHAR(150) NOT NULL,
        [password] NVARCHAR(256) NOT NULL,
        [remember_token] NVARCHAR(256) NULL,
        [status] BIT NOT NULL,
        [updated_at] BIGINT NOT NULL,
        [created_at] BIGINT NOT NULL,
        [session_max] INT NOT NULL,
        [role] INT NOT NULL
    );
END;

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='UserStatus' AND xtype='U')
BEGIN
    CREATE TABLE [UserStatus] (
        [user_status_id] INT IDENTITY(1,1) PRIMARY KEY,
        [name] NVARCHAR(50) NOT NULL
    );
END;

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Logs' AND xtype='U')
BEGIN
    CREATE TABLE [Logs] (
        [log_id] INT IDENTITY(1,1) PRIMARY KEY,
        [created_at] DATETIME DEFAULT GETDATE(),
        [status] NVARCHAR(255),
        [user_id] INT,
        [type] NVARCHAR(255),
        [message] NVARCHAR(MAX),
        FOREIGN KEY ([user_id]) REFERENCES [Users]([user_id])
    );
END;

{% elif DATABASE_TYPE == 2 %}
-- PostgreSQL
CREATE TABLE IF NOT EXISTS "Users" (
  "user_id" SERIAL PRIMARY KEY,
  "username" VARCHAR(50) NOT NULL UNIQUE,
  "f_name" VARCHAR(50) NULL,
  "l_name" VARCHAR(50) NULL,
  "email" VARCHAR(150) NOT NULL,
  "password" VARCHAR(256) NOT NULL,
  "remember_token" VARCHAR(256) NULL,
  "status" BOOLEAN NOT NULL,
  "updated_at" BIGINT NOT NULL,
  "created_at" BIGINT NOT NULL,
  "session_max" INT NOT NULL,
  "role" INT NOT NULL
);

CREATE TABLE IF NOT EXISTS "UserStatus" (
  "user_status_id" SERIAL PRIMARY KEY,
  "name" VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS "Logs" (
    "log_id" SERIAL PRIMARY KEY,
    "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "status" VARCHAR(255),
    "user_id" INT,
    "type" VARCHAR(255),
    "message" TEXT,
    FOREIGN KEY ("user_id") REFERENCES "Users"("user_id")
);

{% endif %}
