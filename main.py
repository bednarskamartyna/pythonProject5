#dziedziczenie
#tworzenie nowych klas przyjmujących formę i funkcjonalność klas bazowych

class KlasaBazowa:
    pass

class KlasaPochodna(KlasaBazowa):
    pass

class KontoBankowe:
    def __init__(self, nazwa, stan = 0):
        self.nazwa = nazwa
        self.stan = stan

    def info(self):
        print("nazwa:", self.nazwa)
        print("stan:", self.stan)

    def wyplac(self, ilosc):
        self.stan -= ilosc
        print("nazwa:", self.nazwa)
        print("stan:", self.stan)

    def wplac(self, ilosc):
        self.stan += ilosc
        print("nazwa:", self.nazwa)
        print("stan:", self.stan)

class KontoDebetowe(KontoBankowe):
    pass

class KontoDebetowe(KontoBankowe):
    def __init__(self, nazwa, stan=0, limit=0):
        KontoBankowe.__init__(self, nazwa, stan)
        self.limit = limit

    def wyplac(self, ilosc):
        """Jeżeli stan konta po operacji przekroczyłby limit, przerwij."""
        if (self.stan - ilosc) < (-self.limit):
            print("Brak srodkow na koncie")
        else:
            KontoBankowe.wyplac(self, ilosc)

account = KontoDebetowe("Jan Nowak", 0, 1000)
account.info()
account.wplac(500)
account.wyplac(1000)
account.info()
account.wyplac(1000)

#funkcja super
# bylo:
def __init__(self, nazwa, stan=0, limit=0):
    KontoBankowe.__init__(self, nazwa, stan)
    self.limit = limit


# jest:
def __init__(self, nazwa, stan=0, limit=0):
    super().__init__(nazwa, stan)
    self.limit = limit

class A:
    """Rodzic pierwszy"""

    def __init__(self):
        super().__init__()
        self.a = "A"

    def fa(self):
        print("a:", self.a)


class B:
    """Rodzic drugi"""

    def __init__(self):
        super().__init__()
        self.b = "B"

    def fb(self):
        print("b:", self.b)


class Pochodna(B, A):
    """Dziecko"""

    def __init__(self):
        super().__init__()


#__doc__ docstringi nie są dziedziczone

d = Pochodna()
print(d.a)
print(d.b)

import math


class Figura:
    def obwod(self):  # L
        """Obliczanie obwodu."""
        raise NotImplementedError

    def pole(self):  # S/P
        """Obliczanie pola powierzchni."""
        raise NotImplementedError

class Kolo(Figura):
    def __init__(self, r):
        self.r = r
    def pole(self):
        pole = math.pi * self.r**2
        print(pole)
    def obwod(self):
        obwod = 2* math.pi * self.r
        print(obwod)

kolo = Kolo(5)
kolo.pole()
kolo.obwod()

class Prostokat(Figura):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def pole(self):
        pole = self.a * self.b
        print(pole)
    def obwod(self):
        obwod = 2 * self.a + 2 * self.b
        print(obwod)

prostokat = Prostokat(2,6)
prostokat.obwod()
prostokat.pole()

class Kwadrat(Prostokat):
    def __init__(self, a):
        Prostokat.__init__(self, a, a)

kwadrat = Kwadrat(7)
kwadrat.obwod()
kwadrat.pole()

class TrojkatRownoboczny(Figura):
    def __init__(self, a):
        self.a = a
    def pole(self):
        pole = (self.a ** 2) * 3**(0.5) * 0.25
        print(pole)
    def obwod(self):
        obwod = 3 * self.a
        print(obwod)

trojkat_rownoboczny = TrojkatRownoboczny(5)
trojkat_rownoboczny.pole()
trojkat_rownoboczny.obwod()

class Rownoleglobok(Prostokat):
    def __init__(self, a, b, h):
        self.a = a
        self.h = h
        self.b = b
    def pole(self):
        pole = self.a * self.h
        print(pole)

rownoleglobok = Rownoleglobok(6, 4, 2)
rownoleglobok.pole()
rownoleglobok.obwod()

class Trapez(Figura):
    def __init__(self, a, b, d):
        self.a = a
        self.b = b
        self.c = (d**2 + (a-b)**2)**0.5
        self.d = d
    def pole(self):
        pole = 0.25 * (self.a + self.b)  * self.d
        print(pole)
    def obwod(self):
        obwod = self.a + self.b + self.c + self.d
        print(obwod)

trapez = Trapez(3,4,4)
trapez.obwod()
trapez.pole()

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus (Vehicle):
    pass

bus = Bus("Szkolny bus", 180, 12)


# Ćwiczenie
# Utwórz klasę Bus, która dziedziczy po klasie Vehicle.
# Podaj argument pojemności w metodzie Bus.seating_capacity() o domyślnej wartości 50.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Liczba miejsc siedzących w {self.name} to {capacity} pasażerów"

class Bus(Vehicle):
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity)

bus2 = Bus("Szkolny bus", 180, 12)
print(bus2.seating_capacity())

