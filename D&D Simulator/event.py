#coding:utf-8

import time
import random
import sys
import winsound
from interface import *
from termcolor import colored, cprint
import pickle

#keyboard.press_and_release('win + left arrow')
#time.sleep(0.5)
#os.system("start cmd C:/Users/Aimé/Desktop/Prog/Jeu Textuel/ /k py fiche_perso.py")

carac_pero = []
pickle.dump(carac_pero,open('carac_pero.p','wb'))

contenu_sac = []
pickle.dump(contenu_sac,open('contenu_sac.p','wb'))

quetes = []
pickle.dump(quetes,open('quetes.p','wb'))

"""bandit = [10,5]
pickle.dump(bandit,open('monstres.p','wb'))"""

pv_max = 10
pickle.dump(pv_max,open('pv_max.p','wb'))

def main_menu():
    os.system('cls')
    print("\t\t\t\t",end="")
    print(colored("DONJON QUEST",'grey','on_white'))
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(colored("\t    'ENTREE' :",'yellow'),colored("JOUER",'grey','on_white'),colored("\t\t\t'ECHAP' :",'yellow'),colored("QUITTER",'grey','on_white'),"\n")
    while True:
        if keyboard.read_key() == "enter":
            intro()

def intro():
    winsound.PlaySound('sounds/warcraft.wav', winsound.SND_ASYNC)
    #winsound.PlaySound(None, winsound.SND_PURGE) #TO STOP SOUND
    clear_main()
    ecrire("Bienvenu Aventurier !\n\nDans ce jeu de rôle vous incarnez un personnage que vous devrez faire avancer au\ntravers d'une histoire.\n\n")
    ecrire("Vous utiliserez les touches du clavier indiquées en ")
    ecrire_color('jaune','yellow'," pour interagir.\n\n")
    ecrire("Cetaines touches sont capricieuses alors n'hésitez pas à appuier une deuxième fois sur la touche souhaitée.\n\n")
    ecrire("Vous rencontrerez des parsonnages au cours du jeu.\nLeurs noms sont affiché en ")
    ecrire_color('bleu','blue',".\n\n")
    ecrire("Les textes d'états sont affichés en ")
    ecrire_color("vert",'green'," si il sont positis.\nEt en ")
    ecrire_color("rouge",'red'," si ils sont négatifs.\n\n\n")
    ecrire("A droite se trouve votre fiche de personnage, elle est actualisée en fonction de\nvos interactions dans le jeu.\n\n\n")
    carac_pero = ["Points de vie",20,"Armure",0,"Force",10,"Chance",6]
    pickle.dump(carac_pero,open('carac_pero.p', 'wb'))
    ecrire("Jettez un oeil à vos caracteristiques dans votre fiche peronnage.\n\n")
    ecrire("Les caractéristiques vous indiquent vos points de vie votre armure et\nvotre competence d'attaque.\n\n")
    ecrire("Vous commencez avec une épée médiocre et une tunique légère. N'ayez\ncrainte, vous trouverez de meilleurs objets au cours du jeu.\n\n")
    ecrire("Vous disposer également d'une petite bourse de cuir remplie de 10 pièces d'or.\n\n")
    ecrire("Vos objets ont été ajoutés à votre sac.\n\n\n")
    contenu_sac = ["Pèces d'or",5,"Tunique légère","+0 armure","Epée médiocre","+0 attaque",]
    pickle.dump(contenu_sac,open('contenu_sac.p', 'wb'))
    ecrire_color("\tC.",'yellow'," Commencer l'aventure.\n\n")
    while True:
        if keyboard.read_key() == "c":
            entree_ville()

def entree_ville():
    clear_main()
    ecrire("Vous êtes en quête d'aventure et décidez de quitter votre village.\n\nAprès plusieurs jours de marche à travers plaines et forêts vous apperceuvez une\nville au loin.\n\n")
    ecrire("De hautes murailles entourent la ville. En arrivant à la porte un garde vous\narrête...\n\n")
    ecrire_color('Garde : ','blue',"Halte ! Que venez-vous faire ici ?\n\n\n") #Question du garde
    ecrire_color("\tT.",'yellow'," Demander le chemin de la taverne.\n\n") #Choix 1
    ecrire_color("\tM.",'yellow'," Demander le chemin du marché.") #Choix 2
    while True:
        if keyboard.read_key() == "t":
            ouvrir_porte_taverne()
        if keyboard.read_key() == "m":
            clear_main()
            marche()

def ville():
    winsound.PlaySound('sounds/warcraft.wav', winsound.SND_ASYNC)
    clear_main()
    ecrire("La ville s'ouvre à vous, où voulez-vous aller ?\n\n\n")
    ecrire_color("\tT.",'yellow'," Taverne.\n\n")
    ecrire_color("\tM.",'yellow'," Marché.\n\n")
    ecrire_color("\tQ.",'yellow'," Quitter la ville.\n\n")
    if keyboard.read_key() == "t":
        ouvrir_porte_taverne()
    if keyboard.read_key() == "m":
        marche()
    if keyboard.read_key() == "q":
        sortie_ville()

def sortie_ville():
    clear_main()
    ecrire("Vous sortez de la ville par la grande porte et arrivez à une patte d'oie.\n\n")
    ecrire_color("\tE.",'yellow'," Vers l'Est.\n\n")
    ecrire_color("\tO.",'yellow'," Vers l'Ouest.\n\n")
    ecrire_color("\tV.",'yellow'," Retourner en ville.\n\n")
    while True:
        if keyboard.read_key() == "e":
            est_premier()
        if keyboard.read_key() == "o":
            ouest()
        if keyboard.read_key() == "v":
            ville()

def est_premier():
    clear_main()
    ecrire("Vous prenez en direction de l'Est.\n\nAprès quelques kilomètres vous aperceuvez, au travers des bois, un château\nvisiblement en ruine.\n\n")
    ecrire_color("\tC.",'yellow'," Aller au château.\n\n")
    ecrire_color("\tE.",'yellow'," Continuer vers l'Est.\n\n")
    ecrire_color("\tF.",'yellow'," Faire demi tour.\n\n")
    while True:
        if keyboard.read_key() == "c":
            chateau_ruine_bandit()
        if keyboard.read_key() == "e":
            est_second()
        if keyboard.read_key() == "f":
            sortie_ville()

def est_second():
    print("NON CODE !")

""" CHATEAU RUINE """

def chateau_ruine_bandit():
    clear_main()
    ecrire("Vous empruntez un petit sentier au travers de la forêt. Plus vous vous rapprochez\ndu château, plus il vous semble imposant. Vous distinguez bientôt de la mousse verdâtre recouvrir les pierres des murailles.\n\n")
    ecrire("Le sentier débouche sur l'entrée principle du château où un homme garde la porte\ndélabrée.\n\nEn vous voyant débouler l'homme dégaine son épée.\n\n")
    ecrire_color("Bandit :",'red'," Que fais-tu ici vermine ? Dégage de là !\n\n")
    ecrire_color("\tA.",'yellow'," Je viens vous faire la peau !\n\n")
    ecrire_color("\tE.",'yellow'," J'aimerai simplement récupérer le mateau que vous avez volé.\n\n")
    while True:
        if keyboard.read_key() == "a":
            combat("bandit",10,5)
        if keyboard.read_key() == "e":
            ecrire("NON CODE !")

""" COMBATS """

def combat(monstre,pv,degats):
    clear_main()
    ecrire("Le combat commence :\n\n")
    ecrire_color("{} :".format(monstre).upper(),'red'," ")
    ecrire_color("{}".format(pv),'yellow'," points de vie - ")
    ecrire_color("{}".format(degats),'yellow'," points d'attaque\n\n\n")
    ecrire_color("\tA.",'yellow'," Attaquer\n")
    ecrire_color("\tF.",'yellow'," Fuir\n\n")
    #Boucle de combat
    while pv > 0:
        if keyboard.read_key() == "a":
            carac_pero = pickle.load(open('carac_pero.p','rb'))
            attaque = random.randrange(0,carac_pero[5])
            if attaque > 0 and attaque < carac_pero[5]:
                clear_main()
                ecrire("Vous frappez le {}.\n\n".format(monstre))
                ecrire_color("Le {} perd {} points de vie.".format(monstre,attaque),'green', "\n\n")
                pv -= attaque
                if pv > 0 :
                    ecrire("Le {} vous attaque !\n\n".format(monstre))
                    cpu_attaque = random.randrange(0,degats)
                    carac_pero[1] = carac_pero[1] - cpu_attaque
                    pickle.dump(carac_pero,open('carac_pero.p','wb'))
                    ecrire_color("Vous perdez {} points de vie.".format(cpu_attaque),"red","\n\n")
                    ecrire_color("{} :".format(monstre).upper(),'red'," ")
                    ecrire_color("{}".format(pv),'yellow'," points de vie - ")
                    ecrire_color("{}".format(degats),'yellow'," points d'attaque\n\n\n")
                    ecrire_color("\tA.",'yellow'," Attaquer\n\n")
                    ecrire_color("\tF.",'yellow'," Fuir\n\n")
                else :
                    ecrire("Le {} s'effondre au sol, mort.".format(monstre))
            if attaque == 0:
                clear_main()
                ecrire_color("Echec critique.",'red'," \n\n")
                ecrire("Le {} vous attaque !\n\n".format(monstre))
                cpu_attaque = random.randrange(0,degats)
                carac_pero[1] = carac_pero[1] - cpu_attaque
                pickle.dump(carac_pero,open('carac_pero.p','wb'))
                ecrire_color("Vous perdez {} points de vie.".format(cpu_attaque),"red","\n\n")
                ecrire_color("{} :".format(monstre).upper(),'red'," ")
                ecrire_color("{}".format(pv),'yellow'," points de vie - ")
                ecrire_color("{}".format(degats),'yellow'," points d'attaque\n\n\n")
                ecrire_color("\tA.",'yellow'," Attaquer\n\n")
                ecrire_color("\tF.",'yellow'," Fuir\n\n")
            if attaque == carac_pero[5]:
                clear_main()
                ecrire_color("Coup critique !",'green',"\n\n")
                ecrire_color("Le {} perd {} pv.".format(monstre,attaque),'green',"\n\n")
                pv -= attaque
                if pv > 0:
                    ecrire("Le {} vous attaque !\n\n".format(monstre))
                    cpu_attaque = random.randrange(0,degats)
                    carac_pero[1] = carac_pero[1] - cpu_attaque
                    pickle.dump(carac_pero,open('carac_pero.p','wb'))
                    ecrire_color("Vous perdez {} points de vie.".format(cpu_attaque),"red","\n\n")
                    ecrire_color("{} :".format(monstre).upper(),'red'," ")
                    ecrire_color("{}".format(pv),'yellow'," points de vie - ")
                    ecrire_color("{}".format(degats),'yellow'," points d'attaque\n\n\n")
                    ecrire_color("\tA.",'yellow'," Attaquer\n\n")
                    ecrire_color("\tF.",'yellow'," Fuir\n\n")
                else :
                    ecrire("Le {} s'effondre au sol, mort.".format(monstre))

        if keyboard.read_key() == "f":
            print("NON CODE !")



""" TAVERNE """

ivresse = 0
pickle.dump(ivresse,open('ivresse.p', 'wb'))

def ouvrir_porte_taverne():
    clear_main()
    ecrire("Vous arrivez devant la potre de la taverne.\n\n\n")
    ecrire_color("\tO.",'yellow'," Ouvrir la porte.\n\n") #Choix 1
    ecrire_color("\tM.",'yellow'," Finalement je vais aller au marché.\n\n") #Choix 2
    while True:
        if keyboard.read_key() == "m":
            marche()
        if keyboard.read_key() == "o":
            winsound.PlaySound('sounds/ouvrir porte.wav', winsound.SND_ASYNC)
            time.sleep(2)
            quetes = pickle.load(open('quetes.p', 'rb'))
            if len(quetes) == 0:
                taverne_quete()
            else:
                taverne()

def taverne():
        clear_main()
        winsound.PlaySound('sounds/Stonefire.wav', winsound.SND_ASYNC)
        ecrire("L'interieur de la taverne est sombre. Une légère fumée flotte dans l'air.\nUn petit groupe de musiciens joue dans un coin. Un feu brûle dans la cheminée.\nQuelques tables sont libres.\n\n")
        ecrire("Que faîtes-vous ?\n\n\n")
        ecrire_color("\tM.",'yellow'," Restaurer ses points de vie avec un bon repas. (3 PO)\n\n")
        ecrire_color("\tB.",'yellow'," Boire une bière.(1 PO)\n\n")
        ecrire_color("\tD.",'yellow'," Jouer aux dés.\n\n")
        ecrire_color("\tQ.",'yellow'," Quitter la taverne.\n\n")
        while True:
            if keyboard.read_key() == "m":
                manger()
            if keyboard.read_key() == "b":
                boire()
            if keyboard.read_key() == "d":
                jeu_des_presentation()
            if keyboard.read_key() == "q":
                winsound.PlaySound('sounds/ouvrir porte.wav', winsound.SND_ASYNC)
                ville()

def taverne_quete():
        clear_main()
        winsound.PlaySound('sounds/Stonefire.wav', winsound.SND_ASYNC)
        ecrire("L'interieur de la taverne est sombre. Une légère fumée flotte dans l'air.\nUn petit groupe de musiciens joue dans un coin. Un feu brûle dans la cheminée.\n\nQuelques tables sont libres.\n\n\n")
        ecrire_color("\tA.",'yellow'," S'asseoir à une table et attendre.\n\n")
        ecrire_color("\tM.",'yellow'," Restaurer ses points de vie avec un bon repas. (3 PO)\n\n")
        while True:
            if keyboard.read_key() == "m":
                manger()
            if keyboard.read_key() == "a":
                clear_main()
                ecrire("Vous vous asseyez et attandez qu'on vienne vous servir.\n\nL'aubergiste arrive un plateau à la main, un chiffon humide sur l'épaule...\n\n")
                ecrire_color("Aubergiste : ",'blue',"Alors qu'es-ce qu'on lui sert au petit nouveau ?\n\n\n") #Aubergiste
                ecrire_color("\tB.",'yellow'," Une pinte de bière et si vous connaissez quelqu'un qui cherche un\n\t   aventurier... (1 PO)") #Pinte + quete
                ecrire_color("\n\n\tT.",'yellow'," Je cherche du travail, vous savez pas ou je peux en trouver ?\n\n") #Juste travail
                while True:
                    if keyboard.read_key() == "b":
                        taverne_aubergiste()
                    if keyboard.read_key() == "t":
                        clear_main()
                        ecrire("L'aubergiste vous regarde d'un air de reproche...\n\n")
                        ecrire_color("Aubergiste : ",'blue',"Si vous voulez des informations va falloir que j'vois des pièces d'or.\n\n")
                        ecrire_color("\tB.",'yellow'," Commander une bière (1 PO)\n\n") #Bière
                        ecrire_color("\tQ.",'yellow'," Quitter la taverne.\n\n") #Marché
                        while True:
                            if keyboard.read_key() == "b":
                                clear_main()
                                taverne_aubergiste()
                            if keyboard.read_key() == "q":
                                winsound.PlaySound('sounds/ouvrir porte.wav', winsound.SND_ASYNC)
                                ville()

def taverne_aubergiste():
    while True:
            clear_main()
            RetireVieOuPo(contenu_sac,1,1,'contenu_sac.p') #RetireObjet(contenu_sac,2,'contenu_sac.p')
            ecrire("L'aubergiste s'en va chercher votre commande.\n\nIl revient et dépose votre pinte sur la table...\n\n")
            ecrire_color("Aubergiste :","blue"," Voila votre bière. Et pour le travail j'ai entendu dire que le\n\t     forgeron avait eu un soucis. Il a surement besoin d'aide.\n\t     Vous le trouverez au marché.\n\n\n\n")
            quetes =["Allez voir le forgeron, il se trouve au marché."]
            with open("quetes.p", "wb") as f:
                pickle.dump(quetes,f)
            ecrire_color("Vous obtenez une nouvelle quête !\n\n\n",'yellow',"\n\n\n")
            ecrire_color("\tB.",'yellow'," Boire une bière. (1 PO)\n\n") #Choix 1
            ecrire_color("\tD.",'yellow'," Jouer aux dés.\n\n") #Choix 2
            ecrire_color("\tQ.",'yellow'," Quitter la taverne.") #Choix 2
            while True :
                if keyboard.read_key() == "d":
                    jeu_des_presentation()
                if keyboard.read_key() == "b":
                    boire()
                if keyboard.read_key() == "q":
                    winsound.PlaySound('sounds/ouvrir porte.wav', winsound.SND_ASYNC)
                    ville()

def boire():
    clear_main()
    ivresse = pickle.load(open('ivresse.p', 'rb'))
    ivresse += 1
    pickle.dump(ivresse,open('ivresse.p', 'wb'))
    RetireVieOuPo(contenu_sac,1,1,'contenu_sac.p')
    winsound.PlaySound('sounds/drinking.wav', winsound.SND_ASYNC)
    ecrire("On vous apporte une bière que vous buvez tranquillement à votre table.\n\n")
    winsound.PlaySound('sounds/Stonefire.wav', winsound.SND_ASYNC)
    if ivresse == 1 :
        ecrire("Vous vous sentez joyeux !\n\n")
    if ivresse == 2 :
        ecrire("On vous apporte une bière de plus. Vous commencez à être serieusement ivre...\nN'oubliez pas que vous êtes un aventurier novice !\n\n")
    if ivresse == 3 :
        ecrire("On vous apporte la bière de trop. La cuite est totale !\n\n")
        ecrire("Vous passez votre soirée à cuver votre bière dans la taverne, trop ivre pour faire autre chose.\nSi bien que vous finissez pas vous endormir...")
        #Musique nocturne
        time.sleep(4)
        clear_main()
        RetireVieOuPo(contenu_sac,1,100,'contenu_sac.p')
        ecrire("Vous vous réveillez allongé sur le comptoir, sans trop vous rappeler de votre nuit. \n\nVous remarquez que votre bourse est completement vide !\nAvez-vous été détroussé pendant votre sommeil ou avez-vous tout dépensé en bière ?\n\nVous n'en avez aucune idée...")
        ecrire("Vous n'avez plus un sous. Que voulez-vous faire ?\n\n\n")
        ecrire_color("\tQ.",'yellow'," Quitter la taverne.\n\n")
        ecrire_color("\tR.",'yellow'," L'aventure ce n'est pas pour moi. (ABANDONNER)\n\n")
        while True:
            if keyboard.read_key() == "q":
                winsound.PlaySound('sounds/ouvrir porte.wav', winsound.SND_ASYNC)
                ville()
            if keyboard.read_key() == "r":
                clear_main()
                ecrire("Vous abandonnez votre destin d'aventurier et rentrez chez vous, sans un sous en poche mais avec une bonne geule de bois...\n\n\n\n\n")
                ecrire_color("\t\t\t\tFIN.",'yellow',"\n\n\n\n\n\n\n\n\n\n\n\n")
                quit()

    ecrire_color("\tM.",'yellow'," Restaurer ses points de vie avec un bon repas. (3 PO)\n\n")
    ecrire_color("\tB.",'yellow'," Boire une bière.(1 PO)\n\n")
    ecrire_color("\tD.",'yellow'," Jouer aux dés.\n\n")
    ecrire_color("\tQ.",'yellow'," Quitter la taverne.\n\n")
    while True:
        if keyboard.read_key() == "m":
            manger()
        if keyboard.read_key() == "b":
            boire()
        if keyboard.read_key() == "d":
            jeu_des_presentation()
        if keyboard.read_key() == "q":
            winsound.PlaySound('sounds/ouvrir porte.wav', winsound.SND_ASYNC)
            ville()

def manger():
    clear_main()
    plats = ["pot au feu","ragout de boeuf","tourte à l'oignon","côtes de sanglier à la bière",]
    plat_random = plats[random.randrange(0,len(plats) - 1)]
    ecrire("On vous sert le plat suivant : ")
    print(plat_random,'\n\n')
    AjouteVieOuPo(carac_pero,1,100,'carac_pero.p')

    ecrire_color("\tB.",'yellow'," Boire une bière.(1 PO)\n\n")
    ecrire_color("\tD.",'yellow'," Jouer aux dés.\n\n")
    ecrire_color("\tQ.",'yellow'," Quitter la taverne.\n\n")
    while True:
        if keyboard.read_key() == "b":
            boire()
        if keyboard.read_key() == "d":
            jeu_des_presentation()
        if keyboard.read_key() == "q":
            winsound.PlaySound('sounds/ouvrir porte.wav', winsound.SND_ASYNC)
            ville()

def jeu_des_presentation():
    clear_main()
    ecrire("Vous rejoignez la table des joueurs de dés.\n\nRègles du jeu :\n\nIl y a deux dès dans une chope de bois. A chaque tour vous retournez la chope sur\nla table.\
    \nLe but est de parier sur l'addition des deux dès (pair ou impair). Si vous gagnez\nvous remportez une fois votre mise (1PO). Sinon vous la perdez.\n\n\n")
    ecrire_color("\tP. ",'yellow',"Le résultat sera pair. (1PO)\n\n")
    ecrire_color("\tI. ",'yellow',"Le résultat sera impair. (1PO)\n\n")
    ecrire_color("\tQ. ",'yellow',"Quitter la table de jeu.\n\n")
    jeu_des()

def jeu_des():
    while True:
        if keyboard.read_key() == "q":
            quetes = pickle.load(open('quetes.p', 'rb'))
            if quetes == 0 :
                taverne_quete()
            else:
                taverne()
        if keyboard.read_key() == "p": #CHoix Pair
            ecrire("Votre mise est pair.\n\n")
            des_result = random.randrange(2,12)
            if des_result%2 == 0:
                winsound.PlaySound('sounds/roll_dice.wav', winsound.SND_ASYNC)
                retourner_chope = [ecrire("Vous retournez la chope sur la table puis regadez le résultat... "),time.sleep(1)]
                retourner_chope
                ecrire_color(des_result,'yellow',"\nVous avez gagné !\n\n")
                AjouteVieOuPo(contenu_sac,1,1,'contenu_sac.p')
                jeu_des_choix()
            else :
                winsound.PlaySound('sounds/roll_dice.wav', winsound.SND_ASYNC)
                retourner_chope = [ecrire("Vous retournez la chope sur la table puis regadez le résultat... "),time.sleep(1)]
                retourner_chope
                ecrire_color(des_result,'yellow',"\nVous avez perdu.\n\n")
                RetireVieOuPo(contenu_sac,1,1,'contenu_sac.p')
                jeu_des_choix()
        if keyboard.read_key() == "i": #Choix Impair
            ecrire("Votre mise est impair.\n\n")
            des_result = random.randrange(2,12)
            if des_result%2 == 0:
                winsound.PlaySound('sounds/roll_dice.wav', winsound.SND_ASYNC)
                retourner_chope = [ecrire("Vous retournez la chope sur la table puis regadez le résultat... "),time.sleep(1)]
                retourner_chope
                ecrire_color(des_result,'yellow',"\nVous avez perdu.\n\n")
                RetireVieOuPo(contenu_sac,1,1,'contenu_sac.p')
                jeu_des_choix()
            else :
                winsound.PlaySound('sounds/roll_dice.wav', winsound.SND_ASYNC)
                retourner_chope = [ecrire("Vous retournez la chope sur la table puis regadez le résultat... "),time.sleep(1)]
                retourner_chope
                ecrire_color(des_result,'yellow',"\nVous avez gagné !\n\n")
                AjouteVieOuPo(contenu_sac,1,1,'contenu_sac.p')
                jeu_des_choix()

def jeu_des_choix():
    print("Nouvelle manche :\n")
    print(colored("\tP.",'yellow'),"Le résultat sera pair. (1PO)\n")
    print(colored("\tI.",'yellow'),"Le résultat sera impair. (1PO)\n")
    print(colored("\tQ.",'yellow'),"Quitter la table de jeu.\n")
    jeu_des()

""" MARCHE """

lettres = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
lettres.split()
lettres_track = []

objets_a_vendre = ["Gants de cuir :","+1 armure","(10 PO)","Côte de maille :","+5 armure","(50 PO)","Bouclier :","+10 armure","(80 PO)"]
pickle.dump(objets_a_vendre,open('objets_a_vendre.p', 'wb'))

def marche():
    clear_main()
    ecrire("Le marché se trouve sur la place centrale de la ville. On y vend toutes sortes de\nproduits.\n\n\n")
    ecrire_color("\tF.",'yellow'," Etal du forgeron.\n\n")
    ecrire_color("\tP.",'yellow'," Vendeur de potions.\n\n")
    ecrire_color("\tQ.",'yellow'," Quitter le marché.\n\n")
    while True:
        if keyboard.read_key() == "f":
            forgeron()
        if keyboard.read_key() == "p":
            vendeur_potion()
        if keyboard.read_key() == "q":
            ville()

def forgeron():
    clear_main()
    ecrire("Vous arrivez devant l'étal du forgeron. C'est un homme petit et bedonnant.\nDes armes et des armures sont a vendre.\n\n")
    ecrire_color("Forgeron :","blue"," Que puis-je faire pour vous ?\n\n\n")
    quetes = pickle.load(open('quetes.p', 'rb'))
    if len(quetes) == 1 and quetes[0] == "Allez voir le forgeron, il se trouve au marché.":
        ecrire_color("\tQ.",'yellow'," Vous avez eu un soucis il me semble ?\n\n")
        ecrire_color("\tA.",'yellow'," Faites voir ce que vous vendez.\n\n")
        ecrire_color("\tV.",'yellow'," J'ai des objets à vendre.\n\n")
        while True:
            if keyboard.read_key() == "q":
                forgeron_quete()
            if keyboard.read_key() == "a":
                acheter_forgeron()
            if keyboard.read_key() == "v":
                vendre_forgeron()
    else:
        ecrire_color("\tA.",'yellow'," Faites voir ce que vous vendez.\n\n")
        ecrire_color("\tV.",'yellow'," J'ai des objets à vendre.\n\n")
        ecrire_color("\tQ.",'yellow'," Quitter l'étal du forgeron.\n\n")
        while True:
            if keyboard.read_key() == "a":
                acheter_forgeron()
            if keyboard.read_key() == "v":
                vendre_forgeron()
            if keyboard.read_key() == "q":
                marche()

def forgeron_quete():
    clear_main()
    ecrire("Le forgeron vous regarde d'un air surpris.\n\n")
    ecrire_color("Forgeron :",'blue'," En effet ! La nuit dernière des brigands se sont introduits chez moi et m'ont volé mon marteau. Je ne peux pas forger sans cet outil... Rapportez le moi etje vous donnerai une récompense.\nLes brigands se cachent sûrement dans le vieux château abandonné à l'Est de la\nville.\n\n")
    QuetesUpdate("Retrouvez le marteau du forgeron à l'Est de la ville.\n\n")
    ecrire_color("\tA.",'yellow'," Faites voir ce que vous vendez.\n\n")
    ecrire_color("\tV.",'yellow'," J'ai des objets à vendre.\n\n")
    ecrire_color("\tQ.",'yellow'," Quitter l'étal du forgeron.\n\n")
    while True:
        while True:
            if keyboard.read_key() == "a":
                acheter_forgeron()
            if keyboard.read_key() == "v":
                vendre_forgeron()
            if keyboard.read_key() == "q":
                marche()

def acheter_forgeron():
    contenu_sac = pickle.load(open('contenu_sac.p', 'rb'))
    clear_main()
    ecrire("Le forgeron vous détail ses ventes...\n\n\n")
    objets_a_vendre = pickle.load(open('objets_a_vendre.p', 'rb'))
    n = 0
    e = 0
    lettres_track = []
    while n != len(objets_a_vendre) / 3:
        lettre_random = random.choice(lettres)
        lettres_track.append(lettre_random)
        print(colored("\t{}.".format(lettres_track[n]),'yellow'),objets_a_vendre[e],objets_a_vendre[e+1],objets_a_vendre[e+2],"\n")
        n += 1
        e += 3
    ecrire_color("\tQ.",'yellow'," Quitter l'étal du forgeron.\n\n")
    while True:
        a = 0
        if keyboard.read_key() == "q":
            marche()
        if len(objets_a_vendre) == 9:
            if keyboard.read_key() == lettres_track[a].lower():
                if contenu_sac[1] < 10:
                    ecrire_color("Vous n'avez pas assez de pièces d'or...",'red',"\n\n")
                else:
                    contenu_sac = pickle.load(open('contenu_sac.p', 'rb'))
                    contenu_sac.append(objets_a_vendre[0])
                    contenu_sac.append(objets_a_vendre[1])
                    pickle.dump(contenu_sac,open('contenu_sac.p', 'wb'))
                    carac_pero = pickle.load(open('carac_pero.p', 'rb'))
                    carac_pero[3] = carac_pero[3] + 1
                    pickle.dump(carac_pero,open('carac_pero.p', 'wb'))
                    RetireVieOuPo(contenu_sac,1,10,'contenu_sac.p')
                    del objets_a_vendre[0]
                    del objets_a_vendre[0]
                    del objets_a_vendre[0]
                    pickle.dump(objets_a_vendre,open('objets_a_vendre.p', 'wb'))
                    time.sleep(4)
                    forgeron()
            if keyboard.read_key() == lettres_track[a+1].lower():
                if contenu_sac[1] < 50:
                    ecrire_color("Vous n'avez pas assez de pièces d'or...",'red',"\n\n")
                else:
                    contenu_sac = pickle.load(open('contenu_sac.p','rb'))
                    contenu_sac.append(objets_a_vendre[3])
                    contenu_sac.append(objets_a_vendre[4])
                    pickle.dump(contenu_sac,open('contenu_sac.p','wb'))
                    carac_pero = pickle.load(open('carac_pero.p','rb'))
                    carac_pero[3] = carac_pero[3] + 5
                    pickle.dump(carac_pero,open('carac_pero.p','wb'))
                    RetireVieOuPo(contenu_sac,1,50,'contenu_sac.p')
                    del objets_a_vendre[3]
                    del objets_a_vendre[3]
                    del objets_a_vendre[3]
                    pickle.dump(objets_a_vendre,open('objets_a_vendre.p','wb'))
                    time.sleep(4)
                    forgeron()
            if keyboard.read_key() == lettres_track[a+2].lower():
                if contenu_sac[1] < 80:
                    ecrire_color("Vous n'avez pas assez de pièces d'or...",'red',"\n\n")
                else:
                    contenu_sac = pickle.load(open('contenu_sac.p', 'rb'))
                    contenu_sac.append(objets_a_vendre[6])
                    contenu_sac.append(objets_a_vendre[7])
                    pickle.dump(contenu_sac,open('contenu_sac.p','wb'))
                    carac_pero = pickle.load(open('carac_pero.p','rb'))
                    carac_pero[3] = carac_pero[3] + 10
                    pickle.dump(carac_pero,open('carac_pero.p','wb'))
                    RetireVieOuPo(contenu_sac,1,80,'contenu_sac.p')
                    del objets_a_vendre[6]
                    del objets_a_vendre[6]
                    del objets_a_vendre[6]
                    pickle.dump(objets_a_vendre,open('objets_a_vendre.p', 'wb'))
                    time.sleep(4)
                    forgeron()
        if len(objets_a_vendre) == 6:
            if keyboard.read_key() == lettres_track[a].lower():
                if contenu_sac[1] < 10:
                    ecrire_color("Vous n'avez pas assez de pièces d'or...",'red',"\n\n")
                else:
                    contenu_sac = pickle.load(open('contenu_sac.p', 'rb'))
                    contenu_sac.append(objets_a_vendre[0])
                    contenu_sac.append(objets_a_vendre[1])
                    pickle.dump(contenu_sac,open('contenu_sac.p', 'wb'))
                    carac_pero = pickle.load(open('carac_pero.p', 'rb'))
                    carac_pero[3] = carac_pero[3] + 1
                    pickle.dump(carac_pero,open('carac_pero.p', 'wb'))
                    RetireVieOuPo(contenu_sac,1,10,'contenu_sac.p')
                    del objets_a_vendre[0]
                    del objets_a_vendre[0]
                    del objets_a_vendre[0]
                    pickle.dump(objets_a_vendre,open('objets_a_vendre.p', 'wb'))
                    time.sleep(4)
                    forgeron()
            if keyboard.read_key() == lettres_track[a+1].lower():
                if contenu_sac[1] < 50:
                    ecrire_color("Vous n'avez pas assez de pièces d'or...",'red',"\n\n")
                else:
                    contenu_sac = pickle.load(open('contenu_sac.p', 'rb'))
                    contenu_sac.append(objets_a_vendre[3])
                    contenu_sac.append(objets_a_vendre[4])
                    pickle.dump(contenu_sac,open('contenu_sac.p', 'wb'))
                    carac_pero = pickle.load(open('carac_pero.p', 'rb'))
                    carac_pero[3] = carac_pero[3] + 5
                    pickle.dump(carac_pero,open('carac_pero.p', 'wb'))
                    RetireVieOuPo(contenu_sac,1,50,'contenu_sac.p')
                    del objets_a_vendre[3]
                    del objets_a_vendre[3]
                    del objets_a_vendre[3]
                    pickle.dump(objets_a_vendre,open('objets_a_vendre.p', 'wb'))
                    time.sleep(4)
                    forgeron()
        if len(objets_a_vendre) == 3:
            if keyboard.read_key() == lettres_track[a].lower():
                if contenu_sac[1] < 10:
                    ecrire_color("Vous n'avez pas assez de pièces d'or...",'red',"\n\n")
                else:
                    contenu_sac = pickle.load(open('contenu_sac.p', 'rb'))
                    contenu_sac.append(objets_a_vendre[0])
                    contenu_sac.append(objets_a_vendre[1])
                    pickle.dump(contenu_sac,open('contenu_sac.p', 'wb'))
                    carac_pero = pickle.load(open('carac_pero.p', 'rb'))
                    carac_pero[3] = carac_pero[3] + 1
                    pickle.dump(carac_pero,open('carac_pero.p', 'wb'))
                    RetireVieOuPo(contenu_sac,1,10,'contenu_sac.p')
                    del objets_a_vendre[0]
                    del objets_a_vendre[0]
                    del objets_a_vendre[0]
                    pickle.dump(objets_a_vendre,open('objets_a_vendre.p', 'wb'))
                    time.sleep(4)
                    forgeron()

def vendre_forgeron():
    lettres_track = []
    contenu_sac = pickle.load(open('contenu_sac.p','rb')) #Ouvrir le pickle sac
    if len(contenu_sac) == 2: #Si il n'y a pas d'objets à vendre
        clear_main()
        ecrire("Vous n'avez rien à vendre...\n\n\n")
        ecrire_color("\tQ.",'yellow'," Quitter l'étal du forgeron.\n\n")
        while True:
            if keyboard.read_key() == "q":
                marche()
    if len(contenu_sac) > 2: #Si il y a des objets à vendre
        clear_main()
        ecrire_color("Forgeron :",'yellow'," Très bien, que voulez-vous vendre ? \n\n\n")
        prix_vente_track = []
        n = 2
        x = 0
        while n < len(contenu_sac) - 1:
            prix_vente = random.randrange(1,5)
            prix_vente_track.append(prix_vente)
            lettre_random = random.choice(lettres)
            lettres_track.append(lettre_random)
            print(colored("\t{}.".format(lettres_track[x]),'yellow'),"{} ({}PO)\n".format(contenu_sac[n],prix_vente))
            n += 2
            x += 1
        ecrire_color("\tQ.",'yellow'," Quitter l'étal du forgeron.\n\n")
        while True:
            a = 0
            if len(lettres_track) == 1:
                if keyboard.read_key() == lettres_track[a].lower():
                    RetireObjet(contenu_sac,2,'contenu_sac.p')
                    AjouteVieOuPo(contenu_sac,1,prix_vente_track[0],'contenu_sac.p')
                    time.sleep(2)
                    vendre_forgeron()
                if keyboard.read_key() == "q":
                    marche()
            if len(lettres_track) == 2:
                if keyboard.read_key() == lettres_track[a].lower():
                    RetireObjet(contenu_sac,2,'contenu_sac.p')
                    AjouteVieOuPo(contenu_sac,1,prix_vente_track[0],'contenu_sac.p')
                    time.sleep(2)
                    vendre_forgeron()
                if keyboard.read_key() == lettres_track[a+1].lower():
                    RetireObjet(contenu_sac,4,'contenu_sac.p')
                    AjouteVieOuPo(contenu_sac,1,prix_vente_track[0+1],'contenu_sac.p')
                    time.sleep(2)
                    vendre_forgeron()
                if keyboard.read_key() == "q":
                    marche()
            if len(lettres_track) == 3:
                if keyboard.read_key() == lettres_track[a].lower():
                    RetireObjet(contenu_sac,2,'contenu_sac.p')
                    AjouteVieOuPo(contenu_sac,1,prix_vente_track[0],'contenu_sac.p')
                    time.sleep(2)
                    vendre_forgeron()
                if keyboard.read_key() == lettres_track[a+1].lower():
                    RetireObjet(contenu_sac,4,'contenu_sac.p')
                    AjouteVieOuPo(contenu_sac,1,prix_vente_track[0+1],'contenu_sac.p')
                    time.sleep(2)
                    vendre_forgeron()
                if keyboard.read_key() == lettres_track[a+2].lower():
                    RetireObjet(contenu_sac,6,'contenu_sac.p')
                    AjouteVieOuPo(contenu_sac,1,prix_vente_track[0+1],'contenu_sac.p')
                    time.sleep(2)
                    vendre_forgeron()
                if keyboard.read_key() == "q":
                    marche()

def vendeur_potion():
    potions = ["Petite Potion :","+2 points de vie","(5 PO)","Potion Moyenne :","+5 points de vie","(10 PO)","Grande Potion :","+10 points de vie","(20 PO)"]
    pickle.dump(potions,open('potions.p', 'wb'))
    clear_main()
    ecrire("Le vendeur de potions vous dévoile son stock...\n\n")
    ecrire_color("Maître des potions :","blue"," Comment allez-vous ?\n\n\n")
    print(colored("\tG.",'yellow'),potions[0],potions[1],potions[2],"\n")
    print(colored("\tC.",'yellow'),potions[3],potions[4],potions[5],"\n")
    print(colored("\tB.",'yellow'),potions[6],potions[7],potions[8],"\n")
    ecrire_color("\tQ.",'yellow'," Quitter l'étal du forgeron.\n\n")
    while True:
        if keyboard.read_key() == "q":
            marche()
        if keyboard.read_key() == "g":
            contenu_sac = pickle.load(open('contenu_sac.p', 'rb'))
            if contenu_sac[1] < 5:
                ecrire_color("Vous n'avez pas assez de pièces d'or...",'red',"\n\n")
            else:
                contenu_sac.append(potions[0])
                contenu_sac.append(potions[1])
                pickle.dump(contenu_sac,open('contenu_sac.p', 'wb'))
                RetireVieOuPo(contenu_sac,1,5,'contenu_sac.p')
                ecrire_color("Vous obtenez une potion.",'green',"\n\n")
                time.sleep(2)
                vendeur_potion()
        if keyboard.read_key() == "c":
            if contenu_sac[1] < 10:
                ecrire_color("Vous n'avez pas assez de pièces d'or...",'red',"\n\n")
            else:
                contenu_sac = pickle.load(open('contenu_sac.p', 'rb'))
                contenu_sac.append(potions[3])
                contenu_sac.append(potions[4])
                pickle.dump(contenu_sac,open('contenu_sac.p', 'wb'))
                RetireVieOuPo(contenu_sac,1,10,'contenu_sac.p')
                ecrire_color("Vous obtenez une potion.",'green',"\n\n")
                time.sleep(2)
                vendeur_potion()
        if keyboard.read_key() == "b":
                if contenu_sac[1] < 20:
                    ecrire_color("Vous n'avez pas assez de pièces d'or...",'red',"\n\n")
                else:
                    contenu_sac = pickle.load(open('contenu_sac.p', 'rb'))
                    contenu_sac.append(potions[6])
                    contenu_sac.append(potions[7])
                    pickle.dump(contenu_sac,open('contenu_sac.p','wb'))
                    RetireVieOuPo(contenu_sac,1,20,'contenu_sac.p')
                    ecrire_color("Vous obtenez une potion.",'green',"\n\n")
                    time.sleep(2)
                    vendeur_potion()
