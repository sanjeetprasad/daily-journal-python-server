CREATE TABLE `Journal_Entries` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`concept`	TEXT NOT NULL,
	`entry`	TEXT NOT NULL,
    `date`	DATE,
    `mood_Id` INTEGER NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `Mood`(`id`)
);

CREATE TABLE `Mood` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `mood`    TEXT NOT NULL
   
);

DROP TABLE Entries;

INSERT INTO `Mood` VALUES (null, "Happy");
INSERT INTO `Mood` VALUES (null, "Sad");
INSERT INTO `Mood` VALUES (null, "Stressed");
INSERT INTO `Mood` VALUES (null, "Ok");

INSERT INTO `Journal_Entries` VALUES (null, "Python", "I am liking it it not that bad.", "01-22-2021", "1");
INSERT INTO `Journal_Entries` VALUES (null, "SQL", "This is fun, i love it", "01-22-2021", "1");
INSERT INTO `Journal_Entries` VALUES (null, "React", "I am was doing some revision", "01-22-2021", "3");



   SELECT
            j.id,
            j.concept,
            j.entry,
            j.DATE,
            j.mood_Id
            
        FROM Journal_entries j



