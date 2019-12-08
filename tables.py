from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR
from sqlalchemy.schema import ForeignKeyConstraint
from sqlalchemy.orm import sessionmaker
from config import FlaskConfig, MySQLConfig
import migrate.changeset
#from test import start_alter_table


# create an engine
config = FlaskConfig()
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)

# configuration to file db
conf = MySQLConfig()

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
meta = MetaData()


"""Country_index = Table(
   'Country_index', meta, 
   Column('Country', VARCHAR(48)), 
   Column('ISO_3', VARCHAR(3),primary_key=True), 
   Column('UN_region', VARCHAR(40)),
   Column('UN_subregion', VARCHAR(30)),
   Column('Data_Quality', VARCHAR(5))
)"""

Country_index = Table(
   'Country_index', meta, 
   Country = Column(VARCHAR(48)), 
   ISO_3 = Column(VARCHAR(3),primary_key=True), 
   UN_region = Column(VARCHAR(40)),
   UN_subregion = Column(VARCHAR(30)),
   Data_Quality = Column(VARCHAR(5))
)

# Other properties can be modified as well
start_alter_table( Country_index, Table)


Economy_info = Table(
   'Economy_info', meta, 
   Column('ISO_3', VARCHAR(3), primary_key=True), 
   Column('Years', YEAR(4), primary_key=True),
   Column('GDP', DECIMAL(10,4)),
   Column('Population', DECIMAL(15,0)),
   ForeignKeyConstraint(['ISO_3'], ['Country_index.ISO_3'])
)


National_Footprint = Table(
   'National_Footprint', meta, 
   Column('ISO_3', VARCHAR(3), primary_key=True), 
   Column('Years', YEAR(4), primary_key=True),
   Column('Record', VARCHAR(30), primary_key=True),
   Column('Crop_Land', DECIMAL(20,10)), 
   Column('Grazing_Land', DECIMAL(20,10)), 
   Column('Forest_Land', DECIMAL(20,10)), 
   Column('Fishing_Ground', DECIMAL(20,10)), 
   Column('Built_up_Land', DECIMAL(20,10)), 
   Column('Carbon', BIGINT), 
   Column('Total', BIGINT),
   ForeignKeyConstraint(['ISO_3'], ['Country_index.ISO_3'])
)


Bilan_Footprint = Table(
   'Bilan_Footprint', meta, 
   Column('ISO_3', VARCHAR(3), primary_key=True), 
   Column('Years', YEAR(4), primary_key=True),
   Column('HDI', DECIMAL(2,2)),
   Column('Biocapacity_Deficit_or_Reserve', DECIMAL(10,0)), 
   Column('Earths_Required', DECIMAL(10,0)), 
   Column('Countries_Required', DECIMAL(10,0)), 
   ForeignKeyConstraint(['ISO_3'], ['Country_index.ISO_3'])
)

#http://www.mapfish.org/doc/tutorials/sqlalchemy.html
#Session = sessionmaker(engine)
#session = Session()

meta.create_all(engine)


