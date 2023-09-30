import sqlite3
from sqlite3 import Error

class DBM:
    
    def __init__(self, database):
        try:
            self.connection = sqlite3.connect(database)
        except Error as er:
            print(er)
        except Exception as ex:
            print(ex)
        try:
            self.cursor = self.connection.cursor()
        except Error as er:
            print(er)
        except Exception as ex:
            print(ex)
            
    def CheckConnect(self):
        try:
            with self.connection:
                self.cursor.execute("SELECT * from profiles")
            return 1
        except Error as er:
            print(er)
            return 0
        except Exception as ex:
            print(ex)
            return 0

            
    def GetProfilesName(self):
        try:
            with self.connection:
                self.cursor.execute("SELECT * from profiles")
                records = self.cursor.fetchall()
                #log.write("Всего строк:  ", len(records))
                temp = []
                for row in records:
                    temp.append(row[0])
                return temp
        except Error as er:
            print(er)
        except Exception as ex:
            print(ex)

"""    def CreateDBProfiles(self):
        with self.connection:
            self.cursor.execute(
    "CREATE TABLE profiles (
    ID   INTEGER PRIMARY KEY AUTOINCREMENT,
    Name STRING,
    PGF  STRING,
    PSF  STRING
    );
    ")
"""
