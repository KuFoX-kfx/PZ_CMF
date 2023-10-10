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
                self.cursor.execute("SELECT * from settings")
            return 1
        except Error as er:
            print(er)
            return 0
        except Exception as ex:
            print(ex)
            return 0

            
    def GetProfilesName(self, type):
        try:
            with self.connection:
                self.cursor.execute("SELECT * from profiles")
                records = self.cursor.fetchall()
                #log.write("Всего строк:  ", len(records))
                temp = []
                if type == "NP":
                    for row in records:
                        temp.append(row[1])
                    return temp
                if type == "NF":
                    for row in records:
                        temp.append(row[2])
                    return temp
                else:
                    return 400
        except Error as er:
            print(er)
        except Exception as ex:
            print(ex)

    def CreateProfile(self, Name, NF):
        with self.connection:
            return self.cursor.execute("INSERT INTO `profiles` (`NameProfile`, `NameFolder`) values(?,?)", (Name, NF))

    def DeleteProfile(self, Name, type):
        try:
            if type == "NP":
                with self.connection:
                    self.cursor.execute("delete from profiles where NameProfile = ?", (Name,))
            if type == "NF":
                with self.connection:
                    self.cursor.execute("delete from profiles where NameFolder = ?", (Name,))
            else:
                return 400
        except Error as er:
            print(er)
        except Exception as ex:
            print(ex)
        




    def CreateDBProfiles(self):
        with self.connection:
            self.cursor.execute("""
    CREATE TABLE profiles (
    ID          INTEGER PRIMARY KEY AUTOINCREMENT,
    NameProfile STRING  UNIQUE ON CONFLICT REPLACE,
    NameFolder  STRING
);
""")
            self.cursor.execute("""
    CREATE TABLE settings (
    Language STRING,
    GSF      STRING,
    BF       STRING
);
""")
