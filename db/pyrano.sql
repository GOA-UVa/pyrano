SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";

SET AUTOCOMMIT = 0;

START TRANSACTION;

SET time_zone = "+00:00";

--

-- Databases: `pyrano`

--

DROP DATABASE IF EXISTS `pyrano`;

CREATE DATABASE
    IF NOT EXISTS `pyrano` DEFAULT CHARACTER SET utf32 COLLATE utf32_unicode_ci;

USE `pyrano`;

-- --------------------------------------------------------
--
-- Table `site` structure
--

CREATE TABLE
    `site` (
        `station` varchar(100) COLLATE utf32_unicode_ci NOT NULL,
        `latitude` decimal(10, 7) NOT NULL,
        `longitude` decimal(10, 7) NOT NULL,
        `elevation` decimal(8, 2) NOT NULL,
        `description` varchar(500) COLLATE utf32_unicode_ci NOT NULL,
        `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
    ) ENGINE = InnoDB DEFAULT CHARSET = utf32 COLLATE = utf32_unicode_ci;

--
-- Primary key for `site`
--

ALTER TABLE `site` ADD PRIMARY KEY (`station`);

-- --------------------------------------------------------
--
-- Table `instrument` structure
--

CREATE TABLE
    `instrument` (
        `instr_id` varchar(100) COLLATE utf32_unicode_ci NOT NULL,
        `type` ENUM('SMP10-V') NOT NULL,
        `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
    ) ENGINE = InnoDB DEFAULT CHARSET = utf32 COLLATE = utf32_unicode_ci;

--
-- Primary key for `instrument`
--

ALTER TABLE `instrument` ADD PRIMARY KEY (`instr_id`);

-- --------------------------------------------------------
--
-- Table `installation` structure
--

CREATE TABLE
    `installation` (
        `station` varchar(100) COLLATE utf32_unicode_ci NOT NULL,
        `instr_id` varchar(100) COLLATE utf32_unicode_ci NOT NULL,
        `install_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
        `radtype` ENUM('global', 'direct', 'diffuse') NOT NULL,
    ) ENGINE = InnoDB DEFAULT CHARSET = utf32 COLLATE = utf32_unicode_ci;

--
-- Primary key for `installation`
--

ALTER TABLE `installation` ADD PRIMARY KEY (`station`, `instr_id`, `install_time`);

-- --------------------------------------------------------
--
-- Table `calibration` structure
--

CREATE TABLE
    `calibration` (
        `station` varchar(100) COLLATE utf32_unicode_ci NOT NULL,
        `instr_id` varchar(100) COLLATE utf32_unicode_ci NOT NULL,
        `install_time` datetime NOT NULL,
        `factor` DOUBLE NOT NULL,
    ) ENGINE = InnoDB DEFAULT CHARSET = utf32 COLLATE = utf32_unicode_ci;

--
-- Primary key for `calibration`
--

ALTER TABLE `calibration` ADD PRIMARY KEY (`station`, `instr_id`, `install_time`);

-- --------------------------------------------------------
--
-- Table `measurement` structure
--

CREATE TABLE
    `measurement` (
        `station` varchar(100) COLLATE utf32_unicode_ci NOT NULL,
        `instr_id` varchar(100) COLLATE utf32_unicode_ci NOT NULL,
        `install_time` datetime NOT NULL,
        `measured_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
        `value` DOUBLE NOT NULL,
    ) ENGINE = InnoDB DEFAULT CHARSET = utf32 COLLATE = utf32_unicode_ci;

--
-- Primary key for `measurement`
--

ALTER TABLE `measurement` ADD PRIMARY KEY (`station`, `instr_id`, `install_time`, `measured_at`);

-- --------------------------------------------------------
--

-- Foreign keys

ALTER TABLE `installation`
ADD
    CONSTRAINT `fk_installation_1` FOREIGN KEY (`station`) REFERENCES `site` (`station`) ON DELETE RESTRICT ON UPDATE CASCADE,
ADD
    CONSTRAINT `fk_installation_2` FOREIGN KEY (`instr_id`) REFERENCES `instrument` (`instr_id`) ON DELETE RESTRICT ON UPDATE CASCADE;

ALTER TABLE `calibration`
ADD
    CONSTRAINT `fk_calibration_1` FOREIGN KEY (`station`, `instr_id`, `install_time`) REFERENCES `installation` (`station`, `instr_id`, `install_time`) ON DELETE RESTRICT ON UPDATE CASCADE,

ALTER TABLE `measurement`
ADD
    CONSTRAINT `fk_measurement_1` FOREIGN KEY (`station`, `instr_id`, `install_time`) REFERENCES `installation` (`station`, `instr_id`, `install_time`) ON DELETE RESTRICT ON UPDATE CASCADE,
