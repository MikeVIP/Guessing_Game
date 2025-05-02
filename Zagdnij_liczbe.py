# Author: Mateusz B.
# Name: Guessing Game
# Version: v0.01


# Polski: Importowanie biblioteki random
# Deutsch: Importieren der random Bibliothek
# English: Importing the random library
#import random as rnd

liczba_1 = 1
liczba_2 = 200

# Polski: Powitanie
# Deutsch: Begrüßung
# English: Greeting
print("Willkommen zum 'Guessing Game'!")

# Polski: Pętla programu
# Deutsch: Programmschleife
# English: Program loop
while True:
    # Polski: Losowanie liczby (int) z zakresu liczba_1 do liczba_2
    # Deutsch: Zufällige Ganzzahl zwischen liczba_1 und liczba_2 ziehen
    # English: Drawing a random integer between liczba_1 and liczba_2
    #losowa_liczba = rnd.randint(liczba_1, liczba_2)
    
    # Polski: Próby
    # Deutsch: Versuche
    # English: Attempts
    proby = 0

    # Polski: Informacja o zakresie liczb
    # Deutsch: Information über den Zahlenbereich
    # English: Information about the number range
    print(f"Ich habe eine Zahl zwischen {liczba_1} und {liczba_2} ausgewählt. Versuche sie zu erraten.")

    # Polski: Liczba użytkownika
    # Deutsch: Benutzereingabezahl
    # English: User's number
    zagdnij = int(input("Gib deine Zahl ein: "))

    # Polski: Pętla gry
    # Deutsch: Spielschleife
    # English: Game loop
    while True:        
        # Polski: Zliczanie prób
        # Deutsch: Zählen der Versuche
        # English: Counting attempts
        proby += 1
    
        # Polski: Logika programu. Sprawdzanie, czy liczba jest za niska, za wysoka czy poprawna
        # Deutsch: Programmlogik. Überprüfung, ob die Zahl zu niedrig, zu hoch oder korrekt ist
        # English: Program logic. Checking if the number is too low, too high, or correct
        #if zagdnij < losowa_liczba:
        #    print("Zu niedrig.")
        #elif zagdnij > losowa_liczba:
        #    print("Zu hoch.")
        #else:
        #    print(f"Richtig = {losowa_liczba}!")
        #    print(f"Du hast {proby} Versuche gebraucht.")
        #    break
        zagdnij_py = (liczba_1 + liczba_2) // 2
        print(f"Czy to {zagdnij_py}?")

        if zagdnij == zagdnij_py:
            print(f"Zgadłem liczbę {zagdnij} w {proby} próbach!")
            break

        czy_trafil = input("Odpowiedź (- / +): ")
        
        if czy_trafil == "+":
            liczba_1 = zagdnij_py + 1
        elif czy_trafil == "-":
            liczba_2 = zagdnij_py - 1
        else:
            print("Odpowiedz: - / +")
            
    # Polski: Pytanie, czy użytkownik chce grać ponownie czy wyjść
    # Deutsch: Frage, ob der Benutzer erneut spielen oder beenden möchte
    # English: Asking if the user wants to play again or exit
    pytanie = input("Möchtest du noch einmal spielen? (ja): ").lower()
    if pytanie != 'ja':
        print("Danke fürs Spielen! Auf Wiedersehen!")
        # exit
        break
