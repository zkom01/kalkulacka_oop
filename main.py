class KalkulackaOOP:

    def nacti_cislo(self,text_zadani,text_chyba):
        while True:
            try:
                cislo = int(input(text_zadani).strip())
                return cislo
            except ValueError:
                print(text_chyba)

    def proved_operaci(self, a, b):
        operace = 0
        while operace not in [1,2,3,4]:
            print("1 - sčítání")
            print("2 - odčítání")
            print("3 - násobení")
            print("4 - dělení")

            operace = kalc.nacti_cislo("Volba:","Zadej číslo 1 - 4")

            if 1 <= operace <= 4:
                match operace:
                    case 1:
                        return f"Součet: {a + b}"
                    case 2:
                        return f"Rozdíl: {a - b}"
                    case 3:
                        return f"Součin: {a * b}"
                    case 4:
                        return f"Podíl: {a / b}" if b != 0 else "Chyba: Nulou nelze dělit!"
            else:
                print("Zadej číslo 1 - 4")

    def znovu_nebo_ukoncit(self):
        while True:
            volba = input("Chcete pokračovat? (ano/ne): ").strip().lower()
            if volba in ["ano", "a"]:
                return True
            elif volba in ["ne", "n"]:
                return False
            else:
                print("Zadejte 'ano' nebo 'ne'.")


print("Vítejte v Kalkulačce OOP")
kalc = KalkulackaOOP()

while True:
    cislo1 = kalc.nacti_cislo("Zadej první číslo: ", "Není číslo, zkuste znovu!")
    cislo2 = kalc.nacti_cislo("Zadej druhé číslo: ", "Není číslo, zkuste znovu!")

    print(f"Zadali jste čísla {cislo1} a {cislo2}. Výsledek: {kalc.proved_operaci(cislo1, cislo2)}")

    if not kalc.znovu_nebo_ukoncit():
        print("Děkujeme za použití kalkulačky!")
        break