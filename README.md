# django_tutorials



BEGIN;
CREATE TABLE `polls_poll` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `question` varchar(200) NOT NULL,
    `pub_date` datetime NOT NULL
)
;
CREATE TABLE `polls_choice` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `poll_id` integer NOT NULL,
    `choice_text` varchar(200) NOT NULL,
    `votes` integer NOT NULL
)
;
ALTER TABLE `polls_choice` ADD CONSTRAINT `poll_id_refs_id_3aa09835` FOREIGN KEY (`poll_id`) REFERENCES `polls_poll` (`id`);

COMMIT;

####
tutorials 2

user:root
pass:-minepassword


####################

path to find django 
python -c "import sys; sys.path = sys.path[1:]; import django; print(django.__path__)"

