# -*- coding: utf-8 -*-
# Initialisation des librairies
import tkinter as tk

# Iniatialisation des variables
dictionnaire_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', 
    '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', 
    '7': '--...', '8': "---..", 
    '9': "----."
}

def convertir_vers_morse(texte):    
    texte = texte.upper()
    morse = []
    for caractere in texte:
        if caractere in dictionnaire_morse:
            morse.append(dictionnaire_morse[caractere])
        elif caractere == ' ':
            morse.append(' ')  # Espace entre les mots
        else:
            morse.append('?')  # Caractère inconnu
    return ' '.join(morse)

def saisie_morse():
    pass

if __name__ == "__main__":
  
    # Création de la fenêtre principale
    fenetre = tk.Tk()
    fenetre.title("Convertisseur Texte vers Morse")

    # Création des widgets
    label_texte = tk.Label(fenetre, text="Entrez le texte à convertir:")
    label_texte.pack()

    entree_texte = tk.Entry(fenetre, width=50)
    entree_texte.pack()

    # Label pour afficher le résultat
    label_resultat = tk.Label(fenetre, text="Résultat en Morse:")
    label_resultat.pack()
    resultat_morse = tk.Label(fenetre, text="")
    resultat_morse.pack()
    # Fonction pour mettre à jour le label de résultat
    def mettre_a_jour_resultat():
        texte = entree_texte.get()
        resultat = convertir_vers_morse(texte)
        resultat_morse.config(text=resultat)
    
    # Bouton pour mettre à jour le résultat
    bouton_convertir = tk.Button(fenetre, text="Convertir", command=mettre_a_jour_resultat)
    bouton_convertir.pack()

    # Lancement de la boucle principale
    fenetre.mainloop()