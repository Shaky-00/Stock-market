DROP TABLE IF EXISTS `current_details`;
CREATE TABLE `current_details`(
    `code` CHARACTER(6) NOT NULL,
    `name` varchar(20) NOT NULL,
    `current_price` float,
    `gains` float,
    `increase_price` float,
    `vol` int(32),
    `turn_over` float,
    `PE` float,
    `high` float,
    `low` float,
    `t_open` float,
    `y_close` float,
    `total_market` bigint,
    `current_market` bigint,
    `PBR` float,
    `update_time` DATETIME
)ENGINE=InnoDB DEFAULT CHARACTER SET = utf8;

select * from current_details
    where code REGEXP '^30' and name not REGEXP '^C' and gains>19.9
    or code REGEXP '^00' and gains>9.9
    or code REGEXP '^60' and gains>9.9;