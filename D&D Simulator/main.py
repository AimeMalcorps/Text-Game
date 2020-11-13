#coding:utf-8

import time
import random
import sys
from termcolor import colored, cprint
from interface import *
from event import *
from interface import *
import pickle

keyboard.press_and_release('win + left arrow')
time.sleep(0.1)
os.system("start cmd C:/Users/Aimé/Desktop/Prog/Jeu Textuel/ /k py fiche_perso.py")

carac_pero = ["Points de vie",20,"Endurance",3,"Force",8,"Chance",6,]
pickle.dump(carac_pero,open('carac_pero.p','wb'))
contenu_sac = ["Pèces d'or",5,"Tunique légère"," ","Epée médiocre"," ",]
pickle.dump(contenu_sac,open('contenu_sac.p','wb'))
quetes =["Allez voir le forgeron, il se trouve au marché."]
pickle.dump(quetes,open('quetes.p','wb'))
QuetesUpdate("Retrouvez le marteau du forgeron à l'Est de la ville.\n\n")


combat("bandit",10,5)
