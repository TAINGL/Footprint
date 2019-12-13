import os
import time
import datetime
from zipfile import ZipFile
from config import MySQLConfig, FlaskConfig


conf = MySQLConfig()

# Connect to the database

DB_HOST = conf.MYSQL_HOST 
DB_USER = conf.MYSQL_USER
DB_USER_PASSWORD = conf.MYSQL_PASSWORD
DB_NAME = conf.MYSQL_DB
BACKUP_DIR_NAME = '/Users/Johanna/Documents/SIMPLON/PROJET_FINAL/FLASK/app/backup/mysql'
FILE_PREFIX = "db_footprint"
FILE_SUFFIX_DATE_FORMAT = "%Y%m%d%H%M%S"


# get today's date and time
TIMESTAMP = datetime.datetime.now().strftime(FILE_SUFFIX_DATE_FORMAT)
BACKUP_FILENAME = BACKUP_DIR_NAME+"/"+FILE_PREFIX+TIMESTAMP+".sql"
BACKUP_PATH = 'backup/mysql'+"/"+FILE_PREFIX+TIMESTAMP+".sql"

dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + DB_NAME + " > " + BACKUP_DIR_NAME + "/" + FILE_PREFIX + "_" + TIMESTAMP + ".sql"
os.system(dumpcmd)

print ("")
print ("Backup script completed")
print ("Your backups have been created in '" + BACKUP_DIR_NAME + "' directory")

DAYS_TO_KEEP_BACKUP = 360
"""
for f in os.listdir(path):
    if os.stat(os.path.join(path,f)).st_mtime < now - 360 * 86400:

# deleting old files

        list_files = os.listdir(BACKUP_DIR_NAME)

back_date = datetime.datetime.now() - datetime.timedelta(days=DAYS_TO_KEEP_BACKUP)
back_date = back_date.strftime(FILE_SUFFIX_DATE_FORMAT)

length = len(FILE_PREFIX)

# deleting files older than DAYS_TO_KEEP_BACKUP days
for f in list_files:
    filename = f.split(".")[0]
    if "zip" == f.split(".")[1]:
        suffix = filename[length:]
        if suffix < back_date:
            print("Deleting file : "+f)
            os.remove(BACKUP_DIR_NAME + "/" + f)

"""