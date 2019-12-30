USE footprint;

-- Evolution de l'empreinte CO2 de consommation dans le monde (in Billion GHA)
CREATE VIEW EFConsTotGHA_w AS
SELECT Country,Years, Carbon/1000000000
FROM National_Footprint AS N
INNER JOIN Country_index AS C
ON N.ISO_3 = C.ISO_3
WHERE C.Country = 'World'
AND N.Record = 'EFConsTotGHA';

SELECT * FROM EFConsTotGHA_w;

-- En France
-- Country and Total Ecological Footprint (en GHA)
CREATE VIEW EFProdTotGHA_fr AS
SELECT Country,Years, Carbon
FROM National_Footprint AS N
INNER JOIN Country_index AS C
ON N.ISO_3 = C.ISO_3
WHERE C.Country = 'France'
AND N.Record = 'EFProdTotGHA';

CREATE VIEW EFConsTotGHA_fr AS
SELECT Country,Years, Carbon
FROM National_Footprint AS N
INNER JOIN Country_index AS C
ON N.ISO_3 = C.ISO_3
WHERE C.Country = 'France'
AND N.Record = 'EFConsTotGHA';

-- Ecological Footprint of consumption per person (en GHA)
CREATE VIEW EFConsPerCap_fr AS
SELECT Country,Years, Carbon
FROM National_Footprint AS N
INNER JOIN Country_index AS C
ON N.ISO_3 = C.ISO_3
WHERE C.Country = 'France'
AND N.Record = 'EFConsPerCap';

-- Biocapacity per person (en GHA)
CREATE VIEW BiocapPerCap_fr AS
SELECT Country,Years, Total
FROM National_Footprint AS N
INNER JOIN Country_index AS C
ON N.ISO_3 = C.ISO_3
WHERE C.Country = 'France'
AND N.Record = 'BiocapPerCap';


-- Have Countries Relative Footprint Changed?
-- World Carbon footprint in 1970 and in 2014

-- France vs World in 1970
CREATE VIEW Diff1970_fr AS
SELECT (100 * 
(SELECT  Total
FROM Country_index AS C
INNER JOIN National_Footprint AS N 
ON N.ISO_3 = C.ISO_3
WHERE  N.Record = 'EFConsTotGHA' AND N.Years = 1970 AND C.Country = 'France')
/
(SELECT Total
FROM Country_index AS C
INNER JOIN National_Footprint AS N 
ON N.ISO_3 = C.ISO_3
WHERE  N.Record = 'EFConsTotGHA' AND N.Years = 1970 AND C.Country = 'World') 
)As PercentDiff;

-- France vs World in 2014
CREATE VIEW Diff2014_fr AS
SELECT (100 * 
(SELECT  Total
FROM Country_index AS C
INNER JOIN National_Footprint AS N 
ON N.ISO_3 = C.ISO_3
WHERE  N.Record = 'EFConsTotGHA' AND N.Years = 2014 AND C.Country = 'France')
/
(SELECT Total
FROM Country_index AS C
INNER JOIN National_Footprint AS N 
ON N.ISO_3 = C.ISO_3
WHERE  N.Record = 'EFConsTotGHA' AND N.Years = 2014 AND C.Country = 'World') 
)As PercentDiff;


-- Position de la France vis à vis des autres: 
-- Quels pays se classent au premier rang en termes d'empreintes écologiques et de biocapacités totales?
-- Carbon Footprint France (top ten) en 2014 (en GHA):
CREATE VIEW Carbon_top10up AS
SELECT Country
FROM Country_index AS C
INNER JOIN National_Footprint AS N
ON N.ISO_3 = C.ISO_3
WHERE N.Record = 'EFConsTotGHA'
AND N.Years = 2014 
ORDER BY N.Total DESC;
-- LIMIT 10;

-- Ten Countries with smallest footprints? in 2014
CREATE VIEW Carbon_top10down AS
SELECT Country
FROM Country_index AS C
INNER JOIN National_Footprint AS N
ON N.ISO_3 = C.ISO_3
WHERE N.Record = 'EFConsTotGHA'
AND N.Years = 2014 
ORDER BY N.Total ASC;


-- Votre pays est-il débiteur ou créancier écologique? 
-- Créancier écologique
CREATE VIEW Biocapacity_down AS
SELECT Country, Biocapacity_Deficit_or_Reserve
FROM Country_index AS C
INNER JOIN Bilan_Footprint AS B
ON B.ISO_3 = C.ISO_3
ORDER BY B.Biocapacity_Deficit_or_Reserve ASC;

-- Débiteur écologique
CREATE VIEW Biocapacity_up AS
SELECT Country, Biocapacity_Deficit_or_Reserve
FROM Country_index AS C
INNER JOIN Bilan_Footprint AS B
ON B.ISO_3 = C.ISO_3
ORDER BY B.Biocapacity_Deficit_or_Reserve DESC;


-- Quels pays ont les plus grands déficits ou réserves écologiques?
SELECT COUNT(DISTINCT Biocapacity_Deficit_or_Reserve) FROM Bilan_Footprint;

CREATE VIEW Categorie_Biocapacity AS
SELECT Biocapacity_Deficit_or_Reserve, COUNT(Biocapacity_Deficit_or_Reserve)
FROM Bilan_Footprint
GROUP BY Biocapacity_Deficit_or_Reserve
ORDER BY Biocapacity_Deficit_or_Reserve DESC;

CREATE VIEW Biocapacity_fr AS
SELECT Biocapacity_Deficit_or_Reserve, COUNT(Biocapacity_Deficit_or_Reserve)
FROM Bilan_Footprint
WHERE Biocapacity_Deficit_or_Reserve > -2
GROUP BY Biocapacity_Deficit_or_Reserve
ORDER BY Biocapacity_Deficit_or_Reserve DESC;
