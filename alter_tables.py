from sqlalchemy import create_engine, MetaData, Table, Column
from config import FlaskConfig, MySQLConfig
from models import connection, cursor


# create an engine
config = FlaskConfig()
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)

# configuration to file db
conf = MySQLConfig()

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
meta = MetaData()


# creation des tables
sql_command = "USE footprint;"


sql_table_1 ="""ALTER TABLE Country_index
    MODIFY ISO_3 VARCHAR (3),
    MODIFY Country VARCHAR (48),
    MODIFY UN_region VARCHAR (40),
    MODIFY UN_subregion VARCHAR (30),
    MODIFY Data_Quality VARCHAR (5),
    ADD PRIMARY KEY (ISO_3)
;"""


sql_table_2 = """ALTER TABLE Economy_info 
    MODIFY ISO_3 VARCHAR (3),
    MODIFY Years YEAR (4), 
    MODIFY GDP DECIMAL (10,4), 
    MODIFY Population DECIMAL (15),
    ADD PRIMARY KEY (ISO_3, Years)
;"""

sql_table_3 = """ALTER TABLE Bilan_Footprint
    MODIFY ISO_3 VARCHAR (3),
    MODIFY Years YEAR (4),
    MODIFY HDI DECIMAL(2,2),
    MODIFY Biocapacity_Deficit_or_Reserve DECIMAL,
    MODIFY Earths_Required DECIMAL,
    MODIFY Countries_Required DECIMAL,
    ADD PRIMARY KEY (ISO_3,Years)
;"""

sql_table_4 = """ALTER TABLE National_Footprint 
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
;"""

cursor.execute(sql_command)
cursor.execute(sql_table_1)
cursor.execute(sql_table_2)
cursor.execute(sql_table_3)
cursor.execute(sql_table_4)

# add constraint foreign key 

sql_constraint_1 = """ALTER TABLE Economy_info
ADD CONSTRAINT Economy_info_index
  FOREIGN KEY (ISO_3)
  REFERENCES Country_index (ISO_3);"""


sql_constraint_2 = """ALTER TABLE Bilan_Footprint
ADD CONSTRAINT fk_Bilan_Footprint_index
  FOREIGN KEY (ISO_3)
  REFERENCES Country_index (ISO_3);"""
 

sql_constraint_3 = """ALTER TABLE National_Footprint
ADD CONSTRAINT fk_National_Footprint_index
  FOREIGN KEY (ISO_3)
  REFERENCES Country_index (ISO_3);"""

cursor.execute(sql_constraint_1)
cursor.execute(sql_constraint_2)
cursor.execute(sql_constraint_3)

# never forget this, if you want the changes to be saved:
connection.commit()
connection.close()