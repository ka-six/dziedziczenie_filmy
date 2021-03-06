from faker import Faker
fake = Faker()

import random

print("Biblioteka filmów")

class Movies:
    def __init__(self, tytul, rok_wydania, gatunek, liczba_odtworzen):
        self.tytul=tytul
        self.rok_wydania=rok_wydania
        self.gatunek=gatunek
        self.liczba_odtworzen=liczba_odtworzen
    def __str__(self):
        return f"{self.tytul} ({self.rok_wydania}): {self.liczba_odtworzen}"
    def play(self, step=1):
        self.liczba_odtworzen += step

lista = []
gatunki = ["komedia", "horror", "Sci-Fi", "akcja", "dramat", "dokumentalny"]

for i in range(10):
    lista.append(Movies(tytul=fake.word(), rok_wydania=random.randrange(1980, 2021), gatunek=fake.word(gatunki), liczba_odtworzen=random.randrange(50, 1000)))


class Series(Movies):
    def __init__(self, numer_odcinka, numer_sezonu, *args,  **kwargs):
        super().__init__(*args,  **kwargs)
        self.numer_odcinka=numer_odcinka
        self.numer_sezonu=numer_sezonu
    def __str__(self):
        return f"{self.tytul} S{self.numer_sezonu:02d}E{self.numer_odcinka:02d}: {self.liczba_odtworzen}"

for i in range(10):
    lista.append(Series(tytul=fake.word(), rok_wydania=random.randrange(1980, 2021), gatunek=fake.word(gatunki), liczba_odtworzen=random.randrange(50, 1000), numer_odcinka=random.randrange(1,20), numer_sezonu=random.randrange(1,10)))

movies_only = []

for x in lista:
    if type(x) == Movies:
        movies_only.append(x)
movies_only_sorted = sorted(movies_only, key=lambda a: a.tytul)

def get_movies():
    print("\nOto filmy znajdujące się w bazie:")
    for y in movies_only_sorted:
        print(y)

series_only = []

for x in lista:
    if isinstance(x, Series):
        series_only.append(x)
series_only_sorted = sorted(series_only, key=lambda a: a.tytul)

def get_series():
    print("\nOto seriale znajdujące się w bazie:")
    for z in series_only_sorted:
        print(z)

get_movies() 
get_series()


def search():
    wyszukaj = input("Podaj tytul filmu/serialu, którego szukasz:")
    for i in lista:
        if wyszukaj == i.tytul:
            print(i)

"""
search()
"""

def generate_views():
    random.choice(lista).liczba_odtworzen += random.randrange(1, 100)

generate_views()


def run_generate_views():
    for q in range(10):
        generate_views()

"""
run_generate_views()
"""

import datetime

def top_titles():
    N = 3
    dzis=datetime.date.today() 
    dzis_format = dzis.strftime("%d/%m/%Y")
    print("\nLista wszystkich pozycji w bibliotece: ")
    for i in lista:
        print(i)
    top = sorted(lista, key = lambda x: x.liczba_odtworzen, reverse = True)[:int(N)]
    print(f"\nNajpopularniejsze filmy i seriale dnia {dzis_format}: ")
    for y in top:
        print(y)

top_titles()

def dodaj_sezon():
    podaj_tytul = input("Podaj tytuł dodawanego serialu:")
    podaj_rok = input("Podaj rok wydania dodawanego serialu:")
    podaj_gatunek = input("Podaj gatunek dodawanego serialu:")
    podaj_sezon = input("Podaj numer sezonu dodawanego serialu:")
    podaj_ile_odcinkow = input("Podaj liczbę odcinków sezonu:")
    kolejny_odcinek = 1
    for p in range(int(podaj_ile_odcinkow)):
        series_only_sorted.append(Series(tytul=podaj_tytul, rok_wydania=podaj_rok, gatunek=podaj_gatunek, liczba_odtworzen=random.randrange(50, 1000), numer_odcinka=int(kolejny_odcinek), numer_sezonu=int(podaj_sezon)))
        kolejny_odcinek += 1

"""
dodaj_sezon()
get_series()
"""
