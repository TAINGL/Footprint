# import the mysql client for python
import pymysql.cursors
from config import MySQLConfig, FlaskConfig
import csv
import pymysql
import pandas as pd
#import tables

# https://pynative.com/python-mysql-database-connection/
conf = MySQLConfig()

try:
    connection = pymysql.connect(host= conf.MYSQL_HOST,
                                 user= conf.MYSQL_USER,
                                 password= conf.MYSQL_PASSWORD,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    if connection.open:
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()

        # Create a connection object
        dbname = "Footprint"
        # SQL Statement to create a database
        cursor.execute('DROP DATABASE IF EXISTS footprint')
        cursor.execute('CREATE DATABASE footprint;')
        cursor.execute('SHOW DATABASES;')
        cursor.execute('USE footprint;')
        
        # Execute the sqlQuery
        cursor.execute("select DATABASE();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

        # Create cursor and execute Load SQL
        import pandas as pd
        from sqlalchemy import create_engine

        # read CSV file
        path = '/Users/Johanna/Documents/SIMPLON/PROJET_FINAL/FLASK/app/files/'

        # Country_index
        Country_table = pd.read_csv(path + 'Country_table.csv', header = 0, index_col=0)
        print(Country_table)

        engine = create_engine(FlaskConfig.SQLALCHEMY_DATABASE_URI)
        with engine.connect() as conn, conn.begin():
            Country_table.to_sql('Country_index', conn, if_exists='append', index=False)

        # Economy_info
        Economy_info = pd.read_csv(path + 'Country_info.csv', header = 0, index_col=0)
        print(Economy_info)

        engine = create_engine(FlaskConfig.SQLALCHEMY_DATABASE_URI)
        with engine.connect() as conn, conn.begin():
            Economy_info.to_sql('Economy_info', conn, if_exists='append', index=False)

        # National_Footprint
        National_Footprint = pd.read_csv(path + 'NFA_all.csv', header = 0, index_col=0)
        print(National_Footprint)

        engine = create_engine(FlaskConfig.SQLALCHEMY_DATABASE_URI)
        with engine.connect() as conn, conn.begin():
            National_Footprint.to_sql('National_Footprint', conn, if_exists='append', index=False)

        # Bilan_Footprint
        Bilan_Footprint = pd.read_csv(path + 'Bilan_table.csv', header = 0, index_col=0)
        print(Bilan_Footprint)

        engine = create_engine(FlaskConfig.SQLALCHEMY_DATABASE_URI)
        with engine.connect() as conn, conn.begin():
            Bilan_Footprint.to_sql('Bilan_Footprint', conn, if_exists='append', index=False)

        #Fetch all the rows
        databaseList = cursor.fetchall()
        
        for database in databaseList:
            print(database)    

except pymysql.Error as e: # Exception
    print("Error while connecting to MySQL", e)

"""finally:
    try:
        cursor.close()
        connexion.close()
        print("MySQL connection is closed")

    except:
        pass"""


