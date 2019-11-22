
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, String, Integer
from sqlalchemy.types import DateTime, Numeric
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import MySQLConfig, FlaskConfig

# create an engine
conf = FlaskConfig()
db = create_engine(conf.SQLALCHEMY_DATABASE_URI)
base = declarative_base()

# configuration to file db
conf = Config(config)
x = CustomerExtractor(conf.clients)


class Country_table(base):
    __tablename__ = 'Country table'

    Country = db.Column(String(48), primary_key=True, index=True, autoincrement=True)
    ISO_3 = db.Column(db.String(5))
    UN_region = db.Column(db.String(40))
    UN_subregion = db.Column(db.String(30))

    def __repr__(self):
        return '<Country table {}>'.format(self.Country)


class Country_info(base):
    __tablename__ = 'Country info'

    Country = db.Column(String(48), primary_key=True, ForeignKey('Country_table.Country'))
    Years = db.Column(DateTime(4), primary_key=True)
    GDP = db.Column(Decimal(10,4))
    Population = db.Column(BigInteger)

    def repr(self):
        return '<Country_info {}>'.format(self.Country) 

class NFA(base):
    __tablename__ = 'NFA'

    Country = db.Column(String(48), primary_key=True, ForeignKey('Country_table.Country'))
    Years = db.Column(DateTime(4), primary_key=True)
    Record = db.Column(String(30), primary_key=True)
    Crop_Land = db.Column(Decimal(20,10))
    Grazing_Land = db.Column(Decimal(20,10))
    Forest_Land = db.Column(Decimal(20,10))
    Fishing_Ground = db.Column(Decimal(20,10))
    Built_up_Land = db.Column(Decimal(20,10))
    Carbon = db.Column(BigInteger)
    Total = db.Column(BigInteger)

    
    def repr(self):
        return '<NFA {}>'.format(self.Country)

class GEF(base):
    __tablename__ = 'GEF'

    Country = db.Column(String(48), primary_key=True, ForeignKey('Country_table.id'))
    Population_M = db.Column(Decimal(10,2))
    HDI = db.Column(Decimal(2,2))
    PIB = db.Column(Decimal(10,2))
    Biocapacity_Deficit_or_Reserve = db.Column(Decimal(4,2))
    Earths_Required = db.Column(Decimal(2,2))
    Countries_Required = db.Column(Decimal(4,2))
    Data_Quality = db.Column(String(5))

    
    def repr(self):
        return '<GEF {}>'.format(self.id_rest)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)