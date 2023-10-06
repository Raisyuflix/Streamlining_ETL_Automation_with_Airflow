--membuat table segment
create table table_m3
(
	price int,
	area int,
	berdrooms int,
	bathrooms int,
	stories int,
	mainroad VARCHAR(50),
	guestroom VARCHAR(50),
	basement VARCHAR(50),
	hotwaterheating VARCHAR(50),
	airconditioning VARCHAR(50),
	parking int,
	prefarea VARCHAR(50),
	furnishingstatus VARCHAR(50)
);

COPY table_m3(price,area,berdrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnishingstatus)
FROM 'D:\git_practice\Phase 2\Week 2\MS3\P2M3_rais_yufli_data_raw.csv'
DELIMITER ','
CSV HEADER;	

select * from table_m3