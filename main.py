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
