USE footprint;

-- creation des tables 

ALTER TABLE Country_index
    MODIFY ISO_3 VARCHAR (3),
    MODIFY Country VARCHAR (48),
    MODIFY UN_region VARCHAR (40),
    MODIFY UN_subregion VARCHAR (30),
    MODIFY Data_Quality VARCHAR (5),
    ADD PRIMARY KEY (ISO_3)
;


ALTER TABLE Economy_info 
    MODIFY ISO_3 VARCHAR (3),
    MODIFY Years YEAR (4), 
    MODIFY GDP DECIMAL (10,4), 
    MODIFY Population DECIMAL (15),
    ADD PRIMARY KEY (ISO_3, Years)
;

ALTER TABLE Bilan_Footprint
    MODIFY ISO_3 VARCHAR (3),
    MODIFY Years YEAR (4),
    MODIFY HDI DECIMAL(2,2),
    MODIFY Biocapacity_Deficit_or_Reserve DECIMAL,
    MODIFY Earths_Required DECIMAL,
    MODIFY Countries_Required DECIMAL,
    ADD PRIMARY KEY (ISO_3,Years)
;

ALTER TABLE National_Footprint 
	MODIFY ISO_3 VARCHAR (3),
    MODIFY Years YEAR (4),
    MODIFY Record VARCHAR (30),
    MODIFY Crop_Land DECIMAL(20,10),
    MODIFY Grazing_Land DECIMAL(20,10),
    MODIFY Forest_Land DECIMAL(20,10), 
    MODIFY Fishing_Ground DECIMAL(20,10),
    MODIFY Built_up_Land DECIMAL(20,10),
    MODIFY Carbon BIGINT,
    MODIFY Total BIGINT,
    ADD PRIMARY KEY (ISO_3, Years, Record)
;
