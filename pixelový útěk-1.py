def menu_obtiznost(): #funkce pro menu pro výběr obtížnosti
    print("\n--- VOLBA OBTÍŽNOSTI ---")
    print("1. Jednoduchá")
    print("2. Střední")
    print("3. Těžká")
    
    volba = int(input("Vyber obtížnost: ")) 
    print("")
    obtiznosti = ["Jednoduchá", "Střední", "Těžká"]
    
    if volba > 0 or volba < 4:
        print(f"Spouštím hru s obtížností: {obtiznosti[volba - 1]}")
        print("**HRA PROBÍHÁ**")
    else:
        print("Neplatná volba.")
        


def menu_nastaveni(): #funkce pro menu nastavení
    while True:
        print("\n--- NASTAVENÍ ---")
        print("1. Zvuk")
        print("2. Grafika")
        print("3. Jazyk")
        print("4. Ovládání")
        print("5. ULOŽIT A ZPĚT")
        
        volba = input("Vyber kategorii: ")
        print("")
        
        if volba == "1":
            print("Nastavení: Hlasitost efektů / hudby / hlasu")
        elif volba == "2":
            print("Nastavení: Rozlišení / Režim zobrazení / Kvalita textur / V-Sync")
        elif volba == "3":
            print("Nastavení: Čeština / Angličtina / Němčina")
        elif volba == "4":
            print("Nastavení: Mapování kláves / Citlivost myši / Invertovat osu Y")
        elif volba == "5":
            print("Nastavení uloženo")
            break
        else:
            print("Neplatná volba!")

        input() #počkání na jakýkoliv input pro pokračování 

def start_free_play(): #fuknce pro free play
    print("\n--- START FREE PLAY ---")
    print("Inicializace hry...")
    body = 0 #vytvoření bodů
    
    while True:
        print("Pohyb hráče...")
        kolize = input("Nastala kolize s glitchem? (ano/ne): ") 
        print("")
        
        if kolize == "ano":
            print(f"Body: {body}")
            print("KONEC")
            break
        else:
            print("Pokračuješ v pohybu...")
            body = body + 1
            

#----------------------------------------------------        
print("\n--- HLAVNÍ NABÍDKA ---")
print("1. Hrát")
print("2. Nastavení")
print("3. Start (Free Play)")
print("0. Konec")

volba = input("Vyber akci: ")

if volba == "1":
    menu_obtiznost()
elif volba == "2":
    menu_nastaveni()
elif volba == "3":
    start_free_play()
elif volba == "0":
    print("Ukončuji program...")
    
else:
    print("Neplatná volba!")