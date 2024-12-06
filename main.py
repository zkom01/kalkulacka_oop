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
                        return a + b
                    case 2:
                        return a - b
                    case 3:
                        return a * b
                    case 4:
                        return a / b if b != 0 else "Nulou nelze dělit!!"
            else:
                print("Zadej číslo 1 - 4")


print("Vítejte v Kalkulačce OOP")
kalc = KalkulackaOOP()

cislo1 = kalc.nacti_cislo("Zadej první číslo:", "Není číslo znovu!")
cislo2 = kalc.nacti_cislo("Zadej druhé číslo:", "Není číslo znovu!")

print(f"Zadali jste čísla {cislo1} a {cislo2} výsledek: {kalc.proved_operaci(cislo1, cislo2)}")

jhdvbdjvbdkjvbdskbvdkvdkvbdkjvbdvkdsn