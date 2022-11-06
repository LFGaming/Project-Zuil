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
    ('Almere', false, true, false, true),
    ('Amersfoort', true, false, true, false),
    ('Almelo', false, true, false, true),
    ('Alkmaar', true, false, true, false),
    ('Apeldoorn', false, true, false, true),
    ('Assen', true, false, true, false),
    ('Amsterdam', false, true, false, true),
    ('Boxtel', true, false, true, false),
    ('Breda', false, true, false, true),
    ('Dordrecht', true, false, true, false),
    ('Delft', false, true, false, true),
    ('Deventer', true, false, true, false),
    ('Enschede', false, true, false, true),
    ('Gouda', true, false, true, false),
    ('Groningen', false, true, false, true),
    ('Den Haag', true, false, true, false),
    ('Hengelo', false, true, false, true),
    ('Haarlem', true, false, true, false),
    ('Helmond', false, true, false, true),
    ('Hoorn', true, false, true, false),
    ('Heerlen', false, true, false, true),
    ('Den Bosch', true, false, true, false),
    ('Hilversum', false, true, false, true),
    ('Leiden', true, false, true, false),
    ('Lelystad', false, true, false, true),
    ('Leeuwarden', true, false, true, false),
    ('Maastricht', false, true, false, true),
    ('Nijmegen', true, false, true, false),
    ('Oss', false, true, false, true),
    ('Roermond', true, false, true, false),
    ('Roosendaal', false, true, false, true),
    ('Sittard', true, false, true, false),
    ('Tilburg', false, true, false, true),
    ('Utrecht', true, false, true, false),
    ('Venlo', false, true, false, true),
    ('Vlissingen', true, false, true, false),
    ('Zaandam', false, true, false, true),
    ('Zwolle', true, false, true, false),
    ('Zutphen', false, true, false, true);