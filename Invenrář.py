class Predmet:      #Šablona pro předmět
    def __init__(self, nazev, vaha):
        self.nazev = nazev
        self.vaha = vaha

class Inventar: #Class pro Inventář
    def __init__(self, max_nosnost): 
        self.veci = [] #Tady budou uložené věci 
        self.max_nosnost = max_nosnost #max nosnost

    def spocitej_vahu(self): #spočítá se celá váha pro zjištění jestli se tam vejdou ještě další věci
        return sum(v.vaha for v in self.veci)

    def pridat(self, nazev, vaha): #přidání do inventáře
        if self.spocitej_vahu() + vaha <= self.max_nosnost: #kontrola jestli se tam vejde 
            nova_vec = Predmet(nazev, vaha) #vytvoří se nová věc podle class Predmět
            self.veci.append(nova_vec) #přidání do listu
            print(f"'{nazev}' přidán.")
        else:
            print(f"'{nazev}' je moc těžký, už se nevejde!") 

    def odebrat(self, vec_k_odebrani): #odebrání věci
        for vec in self.veci: #projde celej inventář a hledá název který sme zadali (vše v lowercase)
            if vec.nazev.lower() == vec_k_odebrani.lower():
                self.veci.remove(vec) #odstranení z inventáře
                print(f"'{vec.nazev}' byl vyhozen.")
            else:
                print("Tuhle věc v batohu nemáš.")

    def ukaz_batoh(self):  #ukáže aktualní obsah batohu
        print("\n--- AKTUÁLNÍ OBSAH BATOHU ---")
        if not self.veci: #pokud v nem nic neni
            print(" (Batoh je prázdný)")
        else:
            for vec in self.veci:
                print(f"- {vec.nazev} ({vec.vaha} kg)")
        print(f"Váha: {self.spocitej_vahu()} / {self.max_nosnost} kg") #ukáže aktualní stav váhy batohu (zabraná váha/maximalní váha)
        print("-----------------------------\n")

# ----------------------------------------------------------------------------------------------

max_nosnost = 20 #max nosnost
muj_batoh = Inventar(max_nosnost=max_nosnost) #vyvoveří inventáře o nosnosti max_nosnost

while True: #hlavní smyčka
    print("1. Přidat | 2. Odebrat | 3. Ukázat | 4. Konec") #hlavní výběr
    volba = input("Vyber číslo: ")

    if volba == "1":
        jmeno = input("Název věci: ")
        try:
            vaha = float(input("Váha věci (kg): "))  #float pro necelé čísla např. 0.5kg
            muj_batoh.pridat(jmeno, vaha)
        except ValueError:
            print("Chyba: Váha musí být číslo!") #při zadání něčeho jiného než čísla 

    elif volba == "2":
        if not muj_batoh.veci: #pokud v inventáři nic není
            print("\nNemáš co vyhazovat, batoh je prázdný!")
        else:
            muj_batoh.ukaz_batoh() #první ukáže obsah batohu pro vybrání
            odebirana_vec = input("Napiš název věci, kterou chceš vyhodit: ")
            muj_batoh.odebrat(odebirana_vec)

    elif volba == "3": #vypíše obsah
        muj_batoh.ukaz_batoh() 

    elif volba == "4": #rozbije hlavní smyčku
        break 