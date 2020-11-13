#coding:utf-8

import os
import sys
import time
import keyboard
from colorama import init
from termcolor import colored, cprint
#from event import *
import pickle

keyboard.press_and_release('win + right arrow')
os.system('cls')

init()

def fiche_perso():
    print("\t\t\t\t",colored("FICHE PERSONNAGE",'grey','on_white'),"\n\n\n\n\n")
    print("",colored('CARACTERISTIQUES :','grey','on_white'),"   ",colored("Aventurier",'grey','on_white'),"\n\n")

    n = 0
    while n < len(carac_pero) - 1:
        print(carac_pero[n],":",colored(carac_pero[n+1],'yellow'),"\n")
        n += 2

    print("\n\n",colored("SAC A DOS :",'grey','on_white'),"\n\n")

    if not contenu_sac:
        print("Votre sac est vide.")
    else:
        n = 0
        x = 0
        while x != len(contenu_sac) / 2:
            print(contenu_sac[n],":",colored(contenu_sac[n+1],'yellow'),"\n")
            n += 2
            x += 1

    print("\n\n",colored("QUETES :",'grey','on_white'),"\n\n")

    if not quetes:
        print("Vous n'avez aucune quête.")
    else:
        n = 0
        while n < len(quetes):
            cprint(quetes[n],"yellow")
            print("\n")
            n +=1

print("\t\t\t\t",colored("FICHE PERSONNAGE",'grey','on_white'),"\n\n\n\n\n")

contenu_sac_check = 0
carac_pero_check = 0
quetes_check = 0

while True:
    contenu_sac = pickle.load(open('contenu_sac.p', 'rb'))
    carac_pero = pickle.load(open('carac_pero.p', 'rb'))
    quetes = pickle.load(open('quetes.p', 'rb'))
    time.sleep(1)
    if contenu_sac != contenu_sac_check:
        contenu_sac_check = contenu_sac
        os.system('cls')
        fiche_perso()
    if carac_pero != carac_pero_check:
        carac_pero_check = carac_pero
        os.system('cls')
        fiche_perso()
    if quetes != quetes_check:
        quetes_check = quetes
        os.system('cls')
        fiche_perso()
