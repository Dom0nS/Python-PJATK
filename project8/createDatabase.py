import sqlite3

db = sqlite3.connect("studenci.db")
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE Przedmiot (
        IdPrzedmiot INTEGER NOT NULL CONSTRAINT Przedmiot_pk PRIMARY KEY AUTOINCREMENT,
        Nazwa varchar(30) NOT NULL
    );
''')
cursor.execute('''
    CREATE TABLE Student (
        IdStudent INTEGER NOT NULL CONSTRAINT Student_pk PRIMARY KEY AUTOINCREMENT,
        Imie varchar(30) NOT NULL,
        Nazwisko varchar(30) NOT NULL
    );
''')
cursor.execute('''
    CREATE TABLE Ocena (
        IdOcena INTEGER NOT NULL CONSTRAINT Ocena_pk PRIMARY KEY AUTOINCREMENT, 
        IdStudent int NOT NULL,
        IdPrzedmiot int NOT NULL,
        Ocena varchar(3) NOT NULL,
        CONSTRAINT Ocena_Student FOREIGN KEY (IdStudent)
        REFERENCES Student (IdStudent),
        CONSTRAINT Ocena_Przedmiot FOREIGN KEY (IdPrzedmiot)
        REFERENCES Przedmiot (IdPrzedmiot)
    );
''')
cursor.execute('''
    INSERT INTO Przedmiot VALUES (1,"PPY")
''')
cursor.execute('''
    INSERT INTO Student VALUES (1,"Dominik", "Dziura")
''')
cursor.execute('''
    INSERT INTO OCENA VALUES (1,1, 1, 4)
''')
db.commit()
db.close()