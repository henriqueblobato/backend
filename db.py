'''
Created on 3 de abr de 2019

@author: ik
'''
import sqlite3

class Db():
    def __init__(self, db_name):
        self.__conn = sqlite3.connect(db_name)
        self.__cursor = self.__conn.cursor()
        
    def create_env(self):
        self.__create_tables()
        self.__popular_tabelas()

    def __create_tables(self):
        self.__cursor.execute("""
            CREATE TABLE IF NOT EXISTS Clientes (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                RG VARCHAR(9) NOT NULL,
                proof_of_address CHAR(1),
                email TEXT,
                phone VARCHAR(12)
            ); """)
        self.__cursor.execute("""
            CREATE TABLE IF NOT EXISTS Animais (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                type CHAR(3) NOT NULL,
                rescue_date DATE,
                adoption_date DATE,
                porte CHAR(1),
                vaccinated CHAR(1),
                approximate_age SMALLINT,
                image TEXT,
                img_path TEXT
            ); """)
    
    def __popular_tabelas(self):
        self.__cursor.execute("""INSERT INTO Clientes (name, last_name, RG, proof_of_address, email, phone)
                                    VALUES ('Henrique', 'Lobato', '1234567897', 'Y', 'h.lobato001@gmail.com', '11987458745')""")
        self.__cursor.execute("""INSERT INTO Clientes (name, last_name, RG, proof_of_address, email, phone)
                                    VALUES ('Rafaela', 'Frare', '1234654897', 'Y', 'rafa@frare.com', '11987888845')""")
        self.__cursor.execute("""INSERT INTO Clientes (name, last_name, RG, proof_of_address, email, phone)
                                    VALUES ('Jimi', 'Hendrix', '1234567222', 'N', 'hendrix@jimi.com', '00933358745')""")
        self.__cursor.execute("""INSERT INTO Animais (name, type, rescue_date, adoption_date, porte, vaccinated, approximate_age, img_path)
                                    VALUES ('Luke', 'DOG', '2019-01-05', 'NULL', 'XG', 'Y', 3, '../imgs/1')""")
        self.__cursor.execute("""INSERT INTO Animais (name, type, rescue_date, adoption_date, porte, vaccinated, approximate_age, img_path)
                                    VALUES ('Thor', 'DOG', '2018-12-15', 'NULL', 'XG', 'Y', 10, '../imgs/2')""")
        self.__cursor.execute("""INSERT INTO Animais (name, type, rescue_date, adoption_date, porte, vaccinated, approximate_age, img_path)
                                    VALUES ('Jess', 'CAT', '2018-09-08', '2019-04-03', 'XG', 'Y', 1, '../imgs/3')""")
        self.__cursor.execute("""INSERT INTO Animais (name, type, rescue_date, adoption_date, porte, vaccinated, approximate_age, img_path)
                                    VALUES ('Matt', 'DOG', '2018-09-08', 'NULL', 'XG', 'Y', 1, '../imgs/4')""")
        self.__conn.commit()
    
    def insert_cliente(self, name, last_name, RG, proof_of_address, email, phone):
        self.__cursor.execute("""INSERT INTO Clientes (name, last_name, RG, proof_of_address, email, phone)
                                 VALUES (?, ?, ?, ?, ?, ?)""",
                                 (name, last_name, RG, proof_of_address, email, phone))
        self.__conn.commit()
        
    def insert_animais(self, name, typeA, rescue_date, adoption_date, porte, vaccinated, approximate_age, img_dir):
        self.__cursor.execute("""INSERT INTO Animais (name, type, rescue_date, adoption_date, porte, vaccinated, approximate_age, img_path)
                                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                                 (name, typeA, rescue_date, adoption_date, porte, vaccinated, approximate_age, img_dir))
        self.__conn.commit()
        
    def select_from_clientes(self):
        self.__cursor.execute( """ SELECT * FROM Clientes; """)
        return str(self.__cursor.fetchall())
    
    def select_from_animais(self):
        self.__cursor.execute( """ SELECT * FROM Animais; """)
        return str(self.__cursor.fetchall())

    def select_from_animais_by_id(self, idA):
        self.__cursor.execute( """ SELECT * FROM Animais WHERE id=?; """, idA)
        return str(self.__cursor.fetchall())
    
    def select_img_dir_from_animais_by_id(self, idA):
        self.__cursor.execute( """ SELECT img_path FROM Animais WHERE id=?; """, idA)
        return str(self.__cursor.fetchall())
    
    def close_connection_db(self):
        self.__conn.close()


if __name__ == '__main__':
    'TESTES'
    db = Db('teste.db')
    db.create_env()
    db.insert_cliente('Name', 'last_name', '987896541', 'N', 'email@email.com', '11898784566', '../img/99.png')
    db.insert_animais('name', 'DOG', '2019-01-01', None, 'S', 'Y', '3')
    db.close_connection_db()
