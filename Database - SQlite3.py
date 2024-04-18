# Importerer SQLite3-modulet, som tillader interaktion med SQLite-databaser.
import sqlite3
# Importerer random-modulet, som giver funktioner til generering af tilfældige tal og valg.
import random
# Importerer re-modulet, som giver funktionalitet til regulære udtryk i Python.
import re
# Opretter forbindelse til SQLite-databasen 'flashcards.db'.
conn = sqlite3.connect('flashcards.db')
c = conn.cursor()
# Eksekverer en SQL-forespørgsel for at oprette en tabel kaldet 'flashcards',
# hvis den ikke allerede eksisterer, med kolonnerne id, question og answer.
c.execute('''CREATE TABLE IF NOT EXISTS flashcards
             (id INTEGER PRIMARY KEY, question TEXT, answer TEXT)''')
# Definerer en liste med flashcard-data, hvor hvert element er et tuple bestående af spørgsmål og svar.
flashcards_data = [
    ("Skriv en funktion, der udskriver teksten 'Hello, world!' til konsollen.", "print('Hello, world!')"),
    ("Lav en variabel kaldet 'navn' og tildel den dit eget navn. Udskriv så værdien af variablen til konsollen.", "navn = 'dit navn'\nprint(navn)"),
    ("Skriv en funktion, der tager to tal som argumenter og returnerer deres sum.", "def sum(x, y):\n    return x + y"),
    ("Lav en variabel, der indeholder en liste af dine favoritfarver. Udskriv derefter denne liste til konsollen.", "favoritfarver = ['farve1', 'farve2', 'farve3']\nprint(favoritfarver)"),
    ("Skriv en for-løkke, der udskriver tallene fra 1 til 10 til konsollen.", "for i in range(1, 11):\n    print(i)"),
    ("Lav en funktion, der tager en streng som input og returnerer længden af strengen.", "def længde_af_streng(streng):\n    return len(streng)"),
    ("Skriv en if-sætning, der tjekker om et tal er større end 10. Udskriv 'Tallet er større end 10' hvis det er tilfældet, ellers udskriv 'Tallet er ikke større end 10'.", "tal = 15\nif tal > 10:\n    print('Tallet er større end 10')\nelse:\n    print('Tallet er ikke større end 10')"),
    ("Lav en variabel kaldet 'alder' og tildel den din egen alder. Skriv derefter en if-sætning, der udskriver 'Du er voksen' hvis din alder er over 18, ellers udskriver 'Du er ikke voksen'.", "alder = 25\nif alder > 18:\n    print('Du er voksen')\nelse:\n    print('Du er ikke voksen')"),
    ("Skriv en funktion, der tager en liste af tal som input og returnerer summen af alle talene i listen.", "def sum_af_liste(tal_liste):\n    return sum(tal_liste)"),
    ("Lav en variabel, der indeholder en liste af dine yndlingsfrugter. Skriv derefter en for-løkke, der udskriver hver frugt i listen til konsollen.", "yndlingsfrugter = ['frugt1', 'frugt2', 'frugt3']\nfor frugt in yndlingsfrugter:\n    print(frugt)")
]
# Indsætter flashcard-dataene i databasen og bekræfter ændringerne i databasen.
# Og lukker forbindelsen til databasen.
c.executemany('INSERT INTO flashcards (question, answer) VALUES (?, ?)', flashcards_data)
conn.commit()
conn.close()
conn = sqlite3.connect('flashcards.db')
c = conn.cursor()

# Laver en funktion, der henter et tilfældigt flashcard fra databasen
def få_tilfældigt_flashcard():
    c.execute('SELECT * FROM flashcards ORDER BY RANDOM() LIMIT 1')
    return c.fetchone()

print("Velkommen til Flashcards-spillet!\n")
# Definerer hovedfunktionen i programmet.
def main():
# Starter en uendelig løkke. Tager et tilfældigt kort fra databasen og udskriver spørgsmålet fra det hentede flashcard.
    while True:
        input("Tryk på Enter for at se næste flashcard...")
        flashcard = få_tilfældigt_flashcard()
        print("\nSpørgsmål: " + flashcard[1])
        bruger_svar = input("Dit svar: ").strip()
        korrekt_svar = flashcard[2]
# Sammenligner brugerens svar med det korrekte svar ved at fjerne specialtegn og sammenligner små bogstaver og mellemrum
        if re.sub(r'\W+', '', bruger_svar.lower()) == re.sub(r'\W+', '', korrekt_svar.lower()):
            print("Korrekt!\n")
        else:
            print(f"Det korrekte svar er: {korrekt_svar}\n")
# Spørger brugeren om de vil fortsætte med spillet.
        spil_igen = input("Vil du fortsætte med at spille? (ja/nej): ").lower()
        if spil_igen != "ja":
            break

    print("Tak fordi du spillede med!")
# Starter programmet ved at kalde 'main()'.
if __name__ == "__main__":
    main()
