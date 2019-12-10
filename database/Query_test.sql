SELECT * FROM Country_index;
SELECT * FROM Economy_info;
SELECT * FROM Bilan_Footprint;
SELECT * FROM National_Footprint;

USE footprint;

-- Evolution of World Carbon Footprint: Global Carbon Ecological Footprint of Consumption (in Billion GHA)
SELECT Country,Years, Carbon/1000000000
FROM National_Footprint AS N
INNER JOIN Country_index AS C
ON N.ISO_3 = C.ISO_3
WHERE C.Country = 'World'
AND N.Record = 'EFConsTotGHA';

-- Avoir une fiche bilan pour la France:
-- Carbon Footprint France (select):

-- No Filter
SELECT *
FROM National_Footprint AS N
INNER JOIN Country_index AS C
ON N.ISO_3 = C.ISO_3
WHERE C.Country = 'France';

SELECT *
FROM Bilan_Footprint AS B
INNER JOIN Country_index AS C
ON B.ISO_3 = C.ISO_3
WHERE C.Country = 'France';


-- Country and Total Ecological Footprint (en GHA)
SELECT Country,Years, Carbon
FROM National_Footprint AS N
INNER JOIN Country_index AS C
ON N.ISO_3 = C.ISO_3
WHERE C.Country = 'France'
AND N.Record = 'EFProdTotGHA';

SELECT Country,Years, Carbon
FROM National_Footprint AS N
INNER JOIN Country_index AS C
ON N.ISO_3 = C.ISO_3
WHERE C.Country = 'France'
AND N.Record = 'EFConsTotGHA';


-- Ecological Footprint of consumption per person (en GHA)
SELECT *
FROM National_Footprint AS N
INNER JOIN Country_index AS C
ON N.ISO_3 = C.ISO_3
WHERE C.Country = 'France'
AND N.Record = 'EFConsPerCap';

-- Biocapacity per person (en GHA)
SELECT *
FROM National_Footprint AS N
INNER JOIN Country_index AS C
ON N.ISO_3 = C.ISO_3
WHERE C.Country = 'France'
AND N.Record = 'BiocapPerCap';


-- Have Countries Relative Footprint Changed?
-- World Carbon footprint in 1970 and in 2014

-- France vs World in 1970
SELECT (100 * 
(SELECT  Total
FROM Country_index AS C
INNER JOIN National_Footprint AS N 
ON N.ISO_3 = C.ISO_3
WHERE  N.Record = 'EFConsTotGHA' AND N.Years = '1970' AND C.Country = 'France')
/
(SELECT Total
FROM Country_index AS C
INNER JOIN National_Footprint AS N 
ON N.ISO_3 = C.ISO_3
WHERE  N.Record = 'EFConsTotGHA' AND N.Years = '1970' AND C.Country = 'World') 
)As PercentDiff;

-- France vs World in 2014
SELECT (100 * 
(SELECT  Total
FROM Country_index AS C
INNER JOIN National_Footprint AS N 
ON N.ISO_3 = C.ISO_3
WHERE  N.Record = 'EFConsTotGHA' AND N.Years = '2014' AND C.Country = 'France')
/
(SELECT Total
FROM Country_index AS C
INNER JOIN National_Footprint AS N 
ON N.ISO_3 = C.ISO_3
WHERE  N.Record = 'EFConsTotGHA' AND N.Years = '2014' AND C.Country = 'World') 
)As PercentDiff;

-- Position de la France vis à vis des autres: 
-- Carbon Footprint France (top ten) en 2014 (en GHA):
SELECT Country
FROM Country_index AS C
INNER JOIN National_Footprint AS N
ON N.ISO_3 = C.ISO_3
WHERE N.Record = 'EFConsTotGHA'
AND N.Years = '2014' 
AND C.Country != 'World'
ORDER BY N.Total DESC
;
-- LIMIT 10;

-- Quels pays se classent au premier rang en termes d'empreintes écologiques et de biocapacités totales?
-- Ten Countries with smallest footprints? in 2014
SELECT Country
FROM Country_index AS C
INNER JOIN National_Footprint AS N
ON N.ISO_3 = C.ISO_3
WHERE N.Record = 'EFConsTotGHA'
AND N.Years = '2014' 
AND C.Country != 'World'
ORDER BY N.Total ASC;


-- Votre pays est-il débiteur ou créancier écologique? 
-- Créancier écologique
SELECT Country, Biocapacity_Deficit_or_Reserve
FROM Country_index AS C
INNER JOIN Bilan_Footprint AS B
ON B.ISO_3 = C.ISO_3
ORDER BY B.Biocapacity_Deficit_or_Reserve ASC;

-- Débiteur écologique
SELECT Country, Biocapacity_Deficit_or_Reserve
FROM Country_index AS C
INNER JOIN Bilan_Footprint AS B
ON B.ISO_3 = C.ISO_3
ORDER BY B.Biocapacity_Deficit_or_Reserve DESC;

-- Ordonner Biocapacity_Deficit_or_Reserve
SELECT Country, Biocapacity_Deficit_or_Reserve
FROM Country_index AS C
INNER JOIN Bilan_Footprint AS B
ON B.ISO_3 = C.ISO_3
ORDER BY B.Biocapacity_Deficit_or_Reserve DESC;


-- Quels pays ont les plus grands déficits ou réserves écologiques?
SELECT COUNT(DISTINCT Biocapacity_Deficit_or_Reserve) FROM Bilan_Footprint;

SELECT Biocapacity_Deficit_or_Reserve, COUNT(Biocapacity_Deficit_or_Reserve)
FROM Bilan_Footprint
GROUP BY Biocapacity_Deficit_or_Reserve
ORDER BY Biocapacity_Deficit_or_Reserve DESC;

SELECT Biocapacity_Deficit_or_Reserve, COUNT(Biocapacity_Deficit_or_Reserve)
FROM Bilan_Footprint
WHERE Biocapacity_Deficit_or_Reserve > '-2'
GROUP BY Biocapacity_Deficit_or_Reserve
ORDER BY Biocapacity_Deficit_or_Reserve DESC;
