CREATE TABLE `default`.`director_to_movie`  (
  `director_id` int UNSIGNED NOT NULL,
  `movie_id` int UNSIGNED NOT NULL,
  PRIMARY KEY (`director_id`, `movie_id`)
);

CREATE TABLE `default`.`directors`  (
  `director_id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `full_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `birth_date` date NULL DEFAULT NULL,
  `death_date` date NULL DEFAULT NULL,
  PRIMARY KEY (`director_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

CREATE TABLE `default`.`genres`  (
  `genre_id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `genre_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `genre_desc` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  PRIMARY KEY (`genre_id`) USING BTREE,
  UNIQUE INDEX `genre_name`(`genre_name` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

CREATE TABLE `default`.`movie_genre`  (
  `movie_id` int UNSIGNED NOT NULL,
  `genre_id` int UNSIGNED NOT NULL,
  PRIMARY KEY (`movie_id`, `genre_id`) USING BTREE,
  INDEX `fk_mg_genre`(`genre_id` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

CREATE TABLE `default`.`movies`  (
  `movie_id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `release_year` smallint NULL DEFAULT NULL,
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  PRIMARY KEY (`movie_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

ALTER TABLE `default`.`director_to_movie` ADD CONSTRAINT `fk_dtm_director` FOREIGN KEY (`director_id`) REFERENCES `default`.`directors` (`director_id`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `default`.`director_to_movie` ADD CONSTRAINT `fk_dtm_movie` FOREIGN KEY (`movie_id`) REFERENCES `default`.`movies` (`movie_id`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `default`.`movie_genre` ADD CONSTRAINT `fk_mg_genre` FOREIGN KEY (`genre_id`) REFERENCES `default`.`genres` (`genre_id`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `default`.`movie_genre` ADD CONSTRAINT `fk_mg_movie` FOREIGN KEY (`movie_id`) REFERENCES `default`.`movies` (`movie_id`) ON DELETE CASCADE ON UPDATE CASCADE;
```
