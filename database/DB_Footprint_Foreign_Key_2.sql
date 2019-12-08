USE footprint;

-- creation des contraintes: clé étrangère 
ALTER TABLE Economy_info
ADD CONSTRAINT Economy_info_index
  FOREIGN KEY (ISO_3)
  REFERENCES Country_index (ISO_3);
  -- ON DELETE CASCADE
  -- ON UPDATE CASCADE ;

ALTER TABLE Bilan_Footprint
ADD CONSTRAINT fk_Bilan_Footprint_index
  FOREIGN KEY (ISO_3)
  REFERENCES Country_index (ISO_3);
  -- ON DELETE CASCADE
  -- ON UPDATE CASCADE ;  

ALTER TABLE National_Footprint
ADD CONSTRAINT fk_National_Footprint_index
  FOREIGN KEY (ISO_3)
  REFERENCES Country_index (ISO_3);
  -- ON DELETE CASCADE
  -- ON UPDATE CASCADE ;
  

-- ALTER TABLE Country_index ADD INDEX Country_index (ISO_3);
-- ALTER TABLE Economy_info ADD INDEX Economy_info (ISO_3);
-- ALTER TABLE National_Footprint ADD INDEX National_Footprint (ISO_3);