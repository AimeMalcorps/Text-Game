#coding:utf-8

import os
import sys
import time
import random
import keyboard
from termcolor import colored, cprint
import pickle


"""def chargement():
    os.system('cls')
    i = 0
    while i < 3:
        charge = "LOADING..."
        sys.stdout.write('\r')
        for lettre in charge:
            sys.stdout.write(lettre)
            sys.stdout.flush()
            time.sleep(0.2)
        charge = "          "
        sys.stdout.write('\r')
        for lettre in charge:
            sys.stdout.write(lettre)
            sys.stdout.flush()
            time.sleep(0.1)
        i+=1"""

def clear_main():
    os.system('cls')
    print("\t\t\t\t",colored("DONJON QUEST",'grey','on_white'),"\n\n")

def ecrire(ecris):
    for lettre in ecris:
        sys.stdout.write(lettre)
        sys.stdout.flush()
        attente = 0
        attente += random.randint(1, 2) / 100
        time.sleep(attente)

def ecrire_color(nom,color,ecris):
    nom = colored(nom,color)
    for lettre in nom:
        sys.stdout.write(lettre)
        sys.stdout.flush()
        attente = 0
        attente += random.randint(1, 2) / 100
        time.sleep(attente)
    for lettre in ecris:
        sys.stdout.write(lettre)
        sys.stdout.flush()
        attente = 0
        attente += random.randint(1, 2) / 100
        time.sleep(attente)


def RetireVieOuPo(list,key,value,folder):        #Retirer Vie ou Po selon la liste et la key
    list = pickle.load(open(folder, 'rb'))
    if value == 100:                            #Mettre 100 en value pour enlever la totalité (ex: 0 PO)
        cible_perte = list[key-1]
        old_value = list[key]
        list[key] = 0
        pickle.dump(list,open(folder, 'wb'))
        cprint("Vous perdez {} {}.\n".format(old_value,cible_perte),'red')
    else:
        cible_perte = list[key-1] #Désigne pièce d'or
        old_value = list[key] #Nb PO ou PV dispo
        list[key] = old_value - value
        pickle.dump(list,open(folder, 'wb'))
        cprint("Vous perdez {} {}.\n".format(value,cible_perte),'red')

def AjouteVieOuPo(list,key,value,folder):        #Retirer Vie ou Po selon la liste et la key
    list = pickle.load(open(folder, 'rb'))
    if value == 100:
        pv_max = pickle.load(open('pv_max.p', 'rb'))               #Mettre 100 en value pour enlever la totalité (ex: 0 PO)
        list[key] = pv_max
        pickle.dump(list,open(folder, 'wb'))
        cprint("Vous récupérez tous vos points de vie.\n",'green')
    else:
        cible_gain = list[key-1] #Désigne pièce d'or
        old_value = list[key] #Nb PO dispo ou PV dispo
        list[key] = old_value + value
        pickle.dump(list,open(folder, 'wb'))
        cprint("Vous gagnez {} {}.\n".format(value,cible_gain),'green')


def RetireObjet(list,key,folder):                   #Retire Objet
    list = pickle.load(open(folder,'rb'))
    cprint("Vous perdez {}.\n".format(list[key]),'red')
    del list[key]
    del list[key]
    pickle.dump(list,open(folder, 'wb'))

def QuetesUpdate(update):
    quetes = pickle.load(open('quetes.p','rb'))
    quetes[0] = update
    pickle.dump(quetes,open('quetes.p','wb'))
    ecrire_color("Journal de quêtes mis à jour !",'yellow',"\n\n")

def PvMaxUpdate(new_value):
    pv_max = pickle.load(open('pv_max.p','rb'))
    pv_max = new_value
    pickle.dump(pv_max,open('pv_max.p','wb'))
