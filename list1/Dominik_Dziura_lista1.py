#Lista1

'''
UWAGA! Nie należy zmieniać nazw funkcji, oraz wartości zmiennych podanych w pliku
poza wartościami ze stringiem "PODAJ WYNIK" - w tych zmiennych należy przechowywać wynik
dotyczący poszczególnych zadań w_1, w_2 ... w_6.

Ciało funkcji wpisujemy w kodzie zamiast "pass".

Wyniki z każdego zadania powinny wyświetlać się w jednej linijce.
Nie należy wyświetlań nic poza wynikiem działania kodu z poszczególnych zadań
w kolejności tak jak w pliku.
Plik należy zapisać w postaci: imie_nazwisko_lista1.py
'''

#1. Ile unikatowych elementów znajduje się w liście:
#1 pkt
lista_1 = [0,7,8,3,3,0,7,0,3]

w_1 = "4"
print(w_1)

#2. Napisz kod, który podmieni losowy znak ze stringa
s_2 = "ala ma kota"
#na '0':
#2 pkt
import random
index = random.randint(0, len(s_2))
s_2 = s_2[:index] + '0' + s_2[index+1:]
w_2 = s_2
print(w_2)


#3. Napisz kod który podmieni z lista_3 język programowania R na JS, następnie wyświetl podmieniony JS.
# Przed JS nadal musi znajdować się python w strukturze takiego samego typu jak w przykladowej lista_3.
# 2pkt
lista_3 = [[{1: 'java', 0: ('python', 'R')},'c++'],['word', 'excel']]
lista_3[0][0][0] = lista_3[0][0][0][:1] + ('JS',)
w_3 = lista_3
print(w_3)


#4. Jakiego typu dane z poniższych nie mogą być kluczami słownika?
#boolean,float,int,string,tuple,list,set. Odpowiedź umieśc w stringu w_4
#1 pkt

w_4 = "list, set"
print(w_4)

#5. Dla stringa wypisz
#ile razy pojawił się dany znak, w kolejności alfabetycznej.
#Użyj słownika - wynik również ma być słownikiem.
#Sprawdzamy tylko te znaki, które występują w podanym stringu.
#2 pkt

s_5 = "ala ma kota imie ma macko"
answer = {}
for c in s_5:
    if c not in answer:
        answer[c] = 1
    else:
        answer[c] += 1
answer = dict(sorted(answer.items()))
w_5 = answer
print(w_5)

#6. Napisz kod który sprawdzi, czy w poprzednim stringu s_5,
#jakikolwiek znak wystąpił dokładnie 3 razy. Wyświetl Tak jeżeli wystąpił,
#Nie jeżeli nie wystąpił.
#1 pkt
bylo = "Nie"
counter = {}
for c in s_5:
    if c not in counter:
        counter[c] = 1
    else:
        counter[c] += 1
for c in counter:
    if counter[c] == 3:
        bylo = "Tak"

w_6= bylo
print(w_6)

#7. Napisz funkcję sprawdzającą czy podane słowa/zdania są palindromem
#i zwróci True lub False ( jest/ nie jest).
#Pomiń znaki nie będące literami, wielkość liter nie ma znaczenia
#3pkt

def palindrom(s):
    s = ''.join(c for c in s if c.isalpha()).lower()
    return s == s[::-1]

s_7_1 ="Nowy Targ, góry, Zakopane – na pokazy róg, graty won"
print(palindrom(s_7_1))


#8. Napisz funkcję, która zwróci
#wszystkie liczby od 1 do n w jednym stringu rozdzielone przecinkami,
#jednak jeżeli liczba jest podzielna przez:
#trzy – zamiast liczby mamy „Fizz”,
#pięć – zamiast liczby mamy „Buzz”,
#trzy i pięć zamiast liczby mamy „FizzBuzz”.
#wszystkie liczby/słowa mają zostać zwróćone w jednej linii, oraz być rozdzielone przecinkiem
#BEZ spacji
#2 pkt

def fizzbuzz(n):
    result = ""
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            result += "FizzBuzz,"
        elif i % 3 == 0:
            result += "Fizz,"
        elif i % 5 == 0:
            result += "Buzz,"
        else:
            result += str(i) + ","
    result = result[:-1]
    return result

n_8 = 16
print(fizzbuzz(n_8))

#9. Napisz funkcję zwracającą n-ty element ciągu Fibonacciego
# przy F(0)= 0 i F(1) = 1.
#bez rekurencji:
#3 pkt

n_9 = 6
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b
print(fibonacci(n_9))

#10. Napisz funkcję, która dla podanej posortowanej listy
#zwróci index wyszukiwanego elementu za pomocą wyszkukiwania binarnego,
#lub zwróci None gdy nie ma elementu w liscie:
#3 pkt


def binary_search(lista, e):
    lewy = 0
    prawy = len(lista) - 1

    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        if lista[srodek] == e:
            return srodek
        elif lista[srodek] < e:
            lewy = srodek + 1
        else:
            prawy = srodek - 1
    return None

l_10 = [0,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768]
print(binary_search(l_10, 2))


