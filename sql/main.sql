drop table if exists moderator CASCADE;
drop table if exists station CASCADE;
drop table if exists bericht CASCADE;

create table moderator(modnummer serial primary key,
					  naam varchar(255),
					  email varchar(255));
					  
create table station(stationnummer serial primary key,
					 naam varchar(255),
					 pr BOOLEAN NOT NULL,
					 wc BOOLEAN NOT NULL,
					 lift BOOLEAN NOT NULL,
					 ovfiets BOOLEAN NOT NULL);
					 

create table bericht(Idnummer serial primary key,
					naam varchar(255),
					bericht varchar(255),
				 	beoordeling varchar(10),
					beoordeling_tijd time,
					tijd time,
					modnummer integer,
					stationnummer integer,
					FOREIGN key(modnummer) REFERENCES moderator(modnummer),
					FOREIGN key(stationnummer) REFERENCES station(stationnummer));
					
insert into moderator (naam, email) VALUES('luke', 'luke@mod.nl');
insert into moderator (naam, email) VALUES('tim', 'tim@mod.nl');

INSERT INTO station (
    naam, ovfiets, lift, wc, pr)
VALUES
    ('Arnhem', true, false, true, false),
    ('Amsterdam', false, true, false, true),
    ('Utrecht', true, false, true, false);