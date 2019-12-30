CREATE INDEX index_Country
ON Country_index (Country);

ALTER TABLE Country_index
DROP INDEX index_Country;

ALTER TABLE Country_index ADD INDEX ( Country );

ALTER TABLE Country_index
DROP INDEX Country;

EXPLAIN
SELECT Country
FROM Country_index AS C
INNER JOIN National_Footprint AS N
ON N.ISO_3 = C.ISO_3
WHERE N.Record = 'EFConsTotGHA'
AND N.Years = 2014 
ORDER BY N.Total DESC;