class Postava: #vytvoření šabloby pro hráče
    def __init__(self, jmeno, pohlavi, vek, barva_oci, barva_vlasu, vaha, vyska):
        self.jmeno = jmeno
        self.pohlavi = pohlavi
        self.vek = vek
        self.barva_oci = barva_oci
        self.barva_vlasu = barva_vlasu
        self.vaha = vaha
        self.vyska = vyska

    def __str__(self): #způsob jak se to vyprintí
        return (f"--- POSTAVA: {self.jmeno} ---\n"
                f"Pohlaví: {self.pohlavi}\n"
                f"Věk: {self.vek} let\n"
                f"Barva očí: {self.barva_oci}\n"
                f"Barva vlasů: {self.barva_vlasu}\n"
                f"Váha: {self.vaha} kg\n"
                f"Výška: {self.vyska} cm\n"
                "-----------------------")

def vytvorit_postavu(): #funkce pro vytvoření postavy 
    print("\n--- TVORBA NOVÉ POSTAVY ---")
    jmeno = input("Zadej jméno: ")
    pohlavi = input("Zadej pohlaví: ")
    vek = input("Zadej věk: ")
    barva_oci = input("Zadej barvu očí: ")
    barva_vlasu = input("Zadej barvu vlasů: ")
    vaha = input("Zadej váhu (kg): ")
    vyska = input("Zadej výšku (cm): ")

    # Vytvoření instance třídy
    nova_postava = Postava(jmeno, pohlavi, vek, barva_oci, barva_vlasu, vaha, vyska)
    return nova_postava

def main_menu(): #main menu 
    seznam_postav = []
    
    while True: #main menu
        print("\n--- EDITOR POSTAV ---")
        print("1. Vytvořit novou postavu")
        print("2. Zobrazit všechny vytvořené postavy")
        print("3. Uložit a ukončit")
        
        volba = input("Vyber akci: ")

        if volba == "1": #zavolá funkci vytvorit_postavu() a přidá do listu
            postava = vytvorit_postavu()
            seznam_postav.append(postava)
            print("\nPostava byla úspěšně vytvořena!")
        
        elif volba == "2": #vyprintí seznam postav
            if not seznam_postav:
                print("\nZatím nebyly vytvořeny žádné postavy.")
            else:
                print("\nSEZNAM VŠECH POSTAV:")
                for p in seznam_postav:
                    print(p)
        
        elif volba == "3": #konec
            print("\nData uložena. Program končí.")
            break
        
        else:
            print("\nNeplatná volba! Program končí.")
            break

main_menu() #spustí program