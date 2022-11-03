drop table if exists moderator CASCADE;
drop table if exists station CASCADE;
drop table if exists voorzieningen CASCADE;
drop table if exists stationvoorz CASCADE;
drop table if exists station CASCADE;

create table moderator(modnummer integer not null primary key,
					  email varchar(255),
					  naam varchar(255),
					  tijd TIME);
					  
create table station(stationnummer integer not null primary key,
					naam varchar(255));

create table voorzieningen(voorznummer integer not null primary key);

create table bericht(Idnummer integer not null primary key,
					naam varchar(255),
					bericht varchar(255),
					tijd time,
					modnummer integer,
					stationnummer integer,
					FOREIGN key(modnummer) REFERENCES moderator(modnummer),
					FOREIGN key(stationnummer) REFERENCES station(stationnummer));
					
create table stationvoorz(antal integer not null,
						 stationnummer integer,
						 voorznummer integer,
						 FOREIGN key(stationnummer) REFERENCES station(stationnummer),
						 foreign key(voorznummer) references voorzieningen(voorznummer));
						 
