-- Mise à jour et test d’intégrité
-- http://les.pages.perso.chez.free.fr/mysql-index-et-contraintes-integrite-par-cles-etrangeres.io
-- https://web.maths.unsw.edu.au/~lafaye/CCM/sql/sqlcontr.htm

-- UNIQUE
INSERT INTO  Country_index (Country, ISO_3, UN_region, UN_subregion, Data_Quality) 
VALUES('France', 'FRA', 'Europe','Western Europe', 6);

INSERT INTO  Country_index (Country, ISO, UN_region, UN_subregion, Data_Quality) 
VALUES('TEST', 'TES', 'TEST','TEST', 0);

INSERT INTO  Country_index (Country, ISO_3, UN_region, UN_subregion, Data_Quality) 
VALUES('TEST', 'TES', 'TEST','TEST', 0);

DELETE FROM Country_index
WHERE ISO_3 = 'TES';

-- NOT NULL
INSERT INTO  Country_index (Country, UN_region, UN_subregion, Data_Quality) 
VALUES('TEST', 'TEST','TEST', 0);

-- CHECK & CONTRAINT 
ALTER TABLE Country_index
ADD CONSTRAINT CHK_Country CHECK (Country != '');

ALTER TABLE Country_index
DROP CHECK CHK_Country; 

-- INDEX
CREATE INDEX index_Biocapacity 
ON Bilan_Footprint (Biocapacity_Deficit_or_Reserve);

ALTER TABLE Bilan_Footprint
DROP INDEX index_Biocapacity;

EXPLAIN
SELECT Country, Biocapacity_Deficit_or_Reserve
FROM Country_index AS C
INNER JOIN Bilan_Footprint AS B
ON B.ISO_3 = C.ISO_3
ORDER BY B.Biocapacity_Deficit_or_Reserve DESC;

-- TRIGGER



