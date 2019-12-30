-- Importation des données CSV sur une table MySQL:

LOAD DATA INFILE 'FLASK/app/file/Bilan_table.csv'
INTO TABLE country 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'FLASK/app/file/Country_info.csv' 
INTO TABLE country 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'FLASK/app/file/Country_table.csv' 
INTO TABLE discounts 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'FLASK/app/file/NFA_all.csv' 
INTO TABLE discounts 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Use mysqlimport to load a table into the database:
-- mysqlimport --ignore-lines=1 \
        --    --fields-terminated-by=, \
        --    --local -u root \
        --    -p Footprint \
        --     Bilan_table.csv