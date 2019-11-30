
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


class Country_index(base):
    __tablename__ = 'Country index'

    Country = db.Column(String(48))
    ISO_3 = db.Column(db.String(3)primary_key=True)
    UN_region = db.Column(db.String(40))
    UN_subregion = db.Column(db.String(30))
    Data_Quality = db.Column(String(5))

    def __repr__(self):
        return '<Country index {}>'.format(self.Country)


class Economy_info(base):
    __tablename__ = 'Economy info'

    ISO_3 = db.Column(db.String(3), primary_key=True, ForeignKey('Country_table.ISO_3'))
    Years = db.Column(DateTime(4), primary_key=True)
    GDP = db.Column(Decimal(10,4))
    Population = db.Column(Decimal(15,0))

    def repr(self):
        return '<Economy_info {}>'.format(self.Country) 

class National_Footprint(base):
    __tablename__ = 'National_Footprint'

    ISO_3 = db.Column(db.String(3), primary_key=True, ForeignKey('Country_table.ISO_3'))
    Years = db.Column(DateTime(4), primary_key=True)
    Record = db.Column(String(30), primary_key=True)
    Crop_Land = db.Column(Decimal(20,10))
    Grazing_Land = db.Column(Decimal(20,10))
    Forest_Land = db.Column(Decimal(20,10))
    Fishing_Ground = db.Column(Decimal(20,10))
    Built_up_Land = db.Column(Decimal(20,10))
    Carbon = db.Column(BigInteger(20))
    Total = db.Column(BigInteger(20))

    
    def repr(self):
        return '<National_Footprint {}>'.format(self.Country)

class Bilan_Footprint(base):
    __tablename__ = 'Bilan_Footprint'

    ISO_3 = db.Column(db.String(3), primary_key=True, ForeignKey('Country_table.ISO_3'))
    Years = db.Column(DateTime(4), primary_key=True)
    HDI = db.Column(Decimal(2,2))
    Biocapacity_Deficit_or_Reserve = db.Column(Decimal(10,0))
    Earths_Required = db.Column(Decimal(10,0))
    Countries_Required = db.Column(Decimal(10,0))

    
    def repr(self):
        return '<Bilan_Footprint {}>'.format(self.id_rest)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)