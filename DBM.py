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

            
    def GetProfilesName(self, Column):
        try:
            with self.connection:
                self.cursor.execute("SELECT * from profiles")
                records = self.cursor.fetchall()
                #log.write("Всего строк:  ", len(records))
                temp = []
                for row in records:
                    temp.append(row[Column])
                return temp
        except Error as er:
            print(er)
        except Exception as ex:
            print(ex)

    def CreateProfile(self, Name, PGF, PSF):
        with self.connection:
            return self.cursor.execute("INSERT INTO `profiles` (`Name`, `PGF`, `PSF`) values(?,?,?)", (Name, PGF, PSF))

    def DeleteProfile(self, Name):
        try:
            with self.connection:
                self.cursor.execute("delete from profiles where Name = ?", (Name,))
        except Error as er:
            print(er)
        except Exception as ex:
            print(ex)
        




    def CreateDBProfiles(self):
        with self.connection:
            self.cursor.execute(
"""CREATE TABLE IF NOT EXISTS profiles (
ID   INTEGER PRIMARY KEY AUTOINCREMENT,
Name STRING UNIQUE ON CONFLICT REPLACE,
PGF  STRING,
PSF  STRING
);
""")
        #self.connection.commit()
        #except Error as er:
        #    print("CreateDBProfiles" + str(er))
        #except Exception as ex:
        #    print("CreateDBProfiles" + str(ex))
            
        

