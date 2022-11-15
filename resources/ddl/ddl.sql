
CREATE DATABASE `project_tr`; /* DEFAULT CHARACTER SET utf8*/


CREATE TABLE `t_user`
(
    user_id int NOT NULL AUTO_INCREMENT,
    id    varchar(32),
    level int,
    name  varchar(32),
    score int,
    PRIMARY KEY (`user_id` )
)
COMMENT '사용자 정보';

CREATE TABLE `t_user_squad` (
    user_id int,
    hero_id int comment '',
    pos_x int comment '',
    pos_y int comment '',
    PRIMARY KEY (`user_id`, `hero_id`)
)
COMMENT 'squad 정보';


CREATE TABLE `t_user_hero`
(
    user_id int,
    hero_id int,
    PRIMARY KEY (`user_id`, `hero_id`)
)
COMMENT 'heroes 정보';


CREATE TABLE `t_match`(
    match_id int NOT NULL AUTO_INCREMENT,
    host_user_id int,
    guest_user_id int,
    channel_id int,
    PRIMARY KEY (`match_id` )
)
COMMENT 'match 정보';