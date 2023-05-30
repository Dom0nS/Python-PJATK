import sqlite3
import ssl
import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import LeaveOneOut, cross_val_score

ssl._create_default_https_context = ssl._create_unverified_context

#Wczytaj dane z adresu podanego w pliku tekstowym: pliktextowy.txt
# do ramki danych.
#Użyj reszty wierszy jako nagłówków ramki danych.
#Uwaga! Zobacz która zmienna jest zmienną objaśnianą, będzie to potrzebne do dalszych zadań.
with open('pliktextowy.txt') as f:
    url = f.readline().strip("\n")
    headers = [line.rstrip() for line in f]
df = pd.read_csv(url,names=headers) # tutaj podmień df. Ma zawierać wczytane dane.
#Zadanie1 przypisz nazwy kolumn z df w jednej linii:   (2pkt)

wynik1 = df.columns.values.tolist()
print(wynik1)

#Zadanie 2: Wypisz liczbę wierszy oraz kolumn ramki danych w jednej linii.  (2pkt)
wynik2 = "Liczba wierszy: "+str(df.shape[0])+", kolumn: "+str(df.shape[1])
print(wynik2)


#Zadanie Utwórz klasę Wine na podstawie wczytanego zbioru:
#wszystkie zmienne objaśniające powinny być w liscie.
#Zmienna objaśniana jako odrębne pole.
# metoda __init__ powinna posiadać 2 parametry:
#listę (zmienne objaśniające) oraz liczbę(zmienna objaśniana).
#nazwy mogą być dowolne.

# Klasa powinna umożliwiać stworzenie nowego obiektu na podstawie
# już istniejącego obiektu jak w pdf z lekcji lab6.
# podpowiedź: metoda magiczna __repr__
#Nie pisz metody __str__.

class Wine:
    def __init__(self, objasniajace, objasniana):
        self.objasniajace = objasniajace
        self.objasniana = objasniana
    def __repr__(self) -> str:
        return f"Wine(objasniana='{self.objasniana}', objasniajace='{self.objasniajace}')"

#Zadanie 3 Utwórz przykładowy obiekt:   (3pkt)
TypeOf = df.iat[0,0]
skipFirst = True
list = []
for x in range(1, df.shape[1]):
    list.append(df.iat[0,x])
wynik3 = Wine(list,TypeOf) #do podmiany. Pamiętaj - ilość elementów, jak w zbiorze danych.
#Uwaga! Pamiętaj, która zmienna jest zmienną objaśnianą
print(wynik3)

#Zadanie 4.                             (3pkt)
#Zapisz wszystkie dane z ramki danych do listy obiektów typu Wine.
#Nie podmieniaj listy, dodawaj elementy.
#Uwaga! zobacz w jakiej kolejności podawane są zmienne objaśniane i objąśniająca.
# Podpowiedź zobacz w pliktextowy.txt
wineList = []
for i in range(df.shape[0]):
    lista = []
    TypeOf = df.iat[i,0]
    for j in range(1,df.shape[1]):
        lista.append(df.iat[i,j])
    wineList.append(Wine(lista,TypeOf))
wynik4 = len(wineList)
print(wynik4)

#Zadanie5 - Weź ostatni element z listy i na podstawie         (3pkt)
#wyniku funkcji repr utwórz nowy obiekt - eval(repr(obiekt))
#do wyniku przypisz zmienną objaśnianą z tego obiektu:
ostatniElement = wineList[-1]
wynik5 = eval(repr(ostatniElement))
print(wynik5)


#Zadanie 6:                                                          (3pkt)
#Zapisz ramkę danych  do bazy SQLite nazwa bazy(dopisz swoje imię i nazwisko):
# wines_imie_nazwisko, nazwa tabeli: wines.
#Następnie wczytaj dane z tabeli wybierając z bazy danych tylko wiersze z typem wina nr 3
# i zapisz je do nowego data frame:
conn = sqlite3.connect('wines_Dominik_Dziura')
c=conn.cursor()

c.execute("DROP TABLE IF EXISTS wines;")

sql = "CREATE TABLE IF NOT EXISTS wines ("

for element in headers:
    sql+=element+" REAL, "
sql = sql[:-2]
sql+=")"
c.execute(sql)
conn.commit()

for i in range(df.shape[0]):
    sql = "INSERT INTO wines ("
    for element in headers:
        sql+=element+","
    sql = sql[:-1]
    sql+=") VALUES ("
    lista = []
    for j in range(df.shape[1]):
        sql+=str(df.iat[i,j])+","
    sql=sql[:-1]
    sql+=");"
    c.execute(sql)
    conn.commit()

wynik6 = "W następnej linijce podmień na nowy  data frame z winami tylko klasy trzeciej:"
wynik6 = pd.read_sql_query("SELECT * FROM wines WHERE TypeOf = 3.0",conn) #tutaj do podmiany

c.close()
conn.close()

print(wynik6.shape)


#Zadanie 7                                                          (1pkt)
#Utwórz model regresji Logistycznej z domyślnymi ustawieniami:

model = LogisticRegression()


wynik7 = model.__class__.__name__
print(wynik7)

# Zadanie 8:                                                        (3pkt)
#Dokonaj podziału ramki danych na dane objaśniające i  do klasyfikacji.
#Znormalizuj dane objaśniające za pomocą:
#preprocessing.normalize(X)
#cos przypisujemy do x jeszcze raz
# Wytenuj model na wszystkich danych bez podziału na zbiór treningowy i testowy.
# Wykonaj sprawdzian krzyżowy, używając LeaveOneOut() zamiast KFold (Parametr cv)
#  Podaj średnią dokładność (accuracy)
x = df.iloc[:,1:].values.tolist()
y = df.iloc[:,0].values.tolist()
x_normalized = preprocessing.normalize(x)
model.fit(x_normalized,y)

loo = LeaveOneOut()

acc = cross_val_score(model,x_normalized, y, cv=loo, scoring="accuracy")

wynik8 = acc.mean()
print(wynik8)