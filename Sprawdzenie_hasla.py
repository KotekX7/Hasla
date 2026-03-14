import string
import random
import time
import math
haslo = input("Podaj hasło: ")
def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words
if __name__ == '__main__':
    english_words = load_words()
Listy = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
  list(string.punctuation),[1,2,3,4,5,6,7,8,9,0]]
sh = 0
dlugosc = len(haslo)
print("długość hasła to:", dlugosc)
print("przy aktualnej długości hasła spodziewany czas na zdobycie go atakiem brute-forse to: ",(96 * math.factorial(dlugosc)) / 122000 / 60 / 60/ 24, "dni")
blok_lista =[]
flaga = False
if dlugosc >= 4:
    for n in range(4, dlugosc + 1):
        for i in range(dlugosc - n + 1):
            blok = haslo[i : i + n]
            blok = [s.casefold() for s in blok]
            blok = "".join(blok)
            if n >= 6:    
                if blok not in blok_lista:
                    blok_lista.append(blok)
                    sh = sh + 1
                else:
                    sh = sh - 15
            if blok in english_words:
                sh = sh - 15
                if flaga == False:
                    print("część hasła znajduje się w słowniku")
                    flaga = True
b = 0
for i in range(len(haslo)-2):
    x = haslo[i]
    y = haslo[i+1]
    z = haslo[i+2]
    a = 0
    for test in Listy:
        if x in test and y in test and z in test:
            if b == 10:
                break
            sh = sh - 3
            b = b + 1
        else:
            a = a + 1
        if a == 4:
            sh = sh + 7
if b > 3:
    print("hasło jest mało zróżnicowane")
flaga = False
for i in range(len(haslo)-2):
    x = haslo[i]
    y = haslo[i+1]
    z = haslo[i+2]
    if x == y == z:
        sh = sh - 10
        print("hasło zawiera powtażajace się znaki")
        flaga = True
    else:
        sh = sh + 1
male = 0
duze = 0
liczby = 0
specjalne = 0

for znak in haslo:
    if znak.islower():       
        male += 1
    elif znak.isupper():     
        duze += 1
    elif znak.isdigit():      
        liczby += 1
    else:                     
        specjalne += 1
maxl = max(male, duze, liczby, specjalne)
minl = min(male, duze, liczby, specjalne)
if minl == 0:
    sh = sh - 30
    if male == 0:
        print("w haśle brakuje małych liter ")
    if duze == 0:
        print("w haśle brakuje dużych liter ")
    if liczby == 0:
        print("w haśle brakuje liczby")
    if specjalne == 0:
        print("w haśle brakuje znaków specjalnych")
else:
    sh = sh + 7
if maxl - minl >= 3:
    sh = sh - 20
else: 
    sh = sh + 4
c = 0
sh = sh + (2*len(haslo))
if sh < 0:
    sh = 0
print("siła hasła to:", sh)
if sh <= 64:
    print("hasło jest bardzo słabe")
elif sh >64 and sh <= 98:
    print("hasło jest słabe")
elif sh > 98 and sh <= 144:
    print("hasło jest spoko")
elif sh > 144 and sh <= 180:
    print("hasło jest silne")
else:
    print("hasło jest bardzo silne")
pytanie =input("Czy chcesz wzmocnić swoje hasło?(Tak/Nie)")
if pytanie == "tak" or pytanie == "Tak" or pytanie == "TAK" or pytanie == "t" or pytanie == "T":
    print("1) Użyj zastępników aby wzmocnić hasło")
    print("2) Dodaj x losowych znaków do końca hasła")
    print("3) Ponownie sprawdź siłę hasła")
    print("0) Zakończ edycje hasła")
    wybur=int(input("Co chcesz wykonać?: "))
    while wybur != 0:
        match wybur:
            case 1:
                def wzmocnij_haslo(haslo):
                    zamienniki = {
                    'a': '@', 'A': '4',
                    'e': '3', 'E': '3',
                    'i': '1', 'I': '!',
                    'o': '0', 'O': '0',
                    's': '$', 'S': '5',
                    't': '7', 'T': '7'
                    }
                    haslo = "".join(zamienniki.get(znak, znak) for znak in haslo)
                    return(haslo)
                haslo = wzmocnij_haslo(haslo)
                print("nowe hasło: ")
                print(haslo)
            case 2:
                e = int(input("ile dodać znaków?: "))
                dodatki = string.ascii_letters + string.digits + string.punctuation
                haslo += "".join(random.choice(dodatki) for _ in range(e))
                print("nowe hasło: ")
                print(haslo)
            case 3:
                sh = 0
                dlugosc = len(haslo)
                print("długość hasła to:", dlugosc)
                print("przy aktualnej długości hasła spodziewany czas na zdobycie go atakiem brute-forse to: ",(96 * math.factorial(dlugosc)) / 122000 / 60 / 60/ 24, "dni")
                blok_lista =[]
                flaga = False
                if dlugosc >= 4:
                    for n in range(4, dlugosc + 1):
                        for i in range(dlugosc - n + 1):
                            blok = haslo[i : i + n]
                            blok = [s.casefold() for s in blok]
                            blok = "".join(blok)
                            if n >= 6:    
                                if blok not in blok_lista:
                                    blok_lista.append(blok)
                                    sh = sh + 1
                                else:
                                    sh = sh - 15
                            if blok in english_words:
                                sh = sh - 15
                                if flaga == False:
                                    print("część hasła znajduje się w słowniku")
                                    flaga = True
                b = 0
                for i in range(len(haslo)-2):
                    x = haslo[i]
                    y = haslo[i+1]
                    z = haslo[i+2]
                    a = 0
                    for test in Listy:
                        if x in test and y in test and z in test:
                            if b == 10:
                                break
                            sh = sh - 3
                            b = b + 1
                        else:
                            a = a + 1
                        if a == 4:
                            sh = sh + 7
                if b > 3:
                    print("hasło jest mało zróżnicowane")
                flaga = False
                for i in range(len(haslo)-2):
                    x = haslo[i]
                    y = haslo[i+1]
                    z = haslo[i+2]
                    if x == y == z:
                        sh = sh - 10
                        print("hasło zawiera powtażajace się znaki")
                        flaga = True
                    else:
                        sh = sh + 1
                male = 0
                duze = 0
                liczby = 0
                specjalne = 0

                for znak in haslo:
                    if znak.islower():       
                        male += 1
                    elif znak.isupper():     
                        duze += 1
                    elif znak.isdigit():      
                        liczby += 1
                    else:                     
                        specjalne += 1
                maxl = max(male, duze, liczby, specjalne)
                minl = min(male, duze, liczby, specjalne)
                if minl == 0:
                    sh = sh - 30
                    if male == 0:
                        print("w haśle brakuje małych liter ")
                    if duze == 0:
                        print("w haśle brakuje dużych liter ")
                    if liczby == 0:
                        print("w haśle brakuje liczby")
                    if specjalne == 0:
                        print("w haśle brakuje znaków specjalnych")
                else:
                    sh = sh + 7
                if maxl - minl >= 3:
                    sh = sh - 20
                else: 
                    sh = sh + 4
                c = 0
                sh = sh + (2*len(haslo))
                if sh < 0:
                    sh = 0
                print("siła hasła to:", sh)
                if sh <= 64:
                    print("hasło jest bardzo słabe")
                elif sh >64 and sh <= 98:
                    print("hasło jest słabe")
                elif sh > 98 and sh <= 144:
                    print("hasło jest spoko")
                elif sh > 144 and sh <= 180:
                    print("hasło jest silne")
                else:
                    print("hasło jest bardzo silne")
            case _:
                break
        print("1) Użyj zastępników aby wzmocnić hasło")
        print("2) Dodaj x losowych znaków do końca hasła")
        print("3) Ponownie sprawdź siłę hasła")
        print("0) Zakończ edycje hasła")
        wybur=int(input("Co chcesz wykonać?:"))
    koniec = input()