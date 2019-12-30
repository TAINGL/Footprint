-- MySQL Export Table to CSV
SELECT ISO_3, Country, UN_region, UN_subregion, Data_Quality FROM Country_index
INTO OUTFILE '/Users/Johanna/Documents/SIMPLON/CHEF DOEUVRE/BASE DE DONNÉE/DB_Footprint_2/DB_Country_index.csv' 
FIELDS ENCLOSED BY '"' 
TERMINATED BY ';' 
ESCAPED BY '"' 
LINES TERMINATED BY '\r\n';

SELECT * FROM Economy_info
INTO OUTFILE '/Users/Johanna/Documents/SIMPLON/CHEF DOEUVRE/BASE DE DONNÉE/DB_Footprint_2/DB_Economy_info.csv' 
FIELDS ENCLOSED BY '"' 
TERMINATED BY ';' 
ESCAPED BY '"' 
LINES TERMINATED BY '\r\n';

SELECT * FROM Bilan_Footprint
INTO OUTFILE '/Users/Johanna/Documents/SIMPLON/CHEF DOEUVRE/BASE DE DONNÉE/DB_Footprint_2/DB_Bilan_Footprint.csv' 
FIELDS ENCLOSED BY '"' 
TERMINATED BY ';' 
ESCAPED BY '"' 
LINES TERMINATED BY '\r\n';

SELECT * FROM National_Footprint
INTO OUTFILE '/Users/Johanna/Documents/SIMPLON/CHEF DOEUVRE/BASE DE DONNÉE/DB_Footprint_2/DB_National_Footprint.csv' 
FIELDS ENCLOSED BY '"' 
TERMINATED BY ';' 
ESCAPED BY '"' 
LINES TERMINATED BY '\r\n';
