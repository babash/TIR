#-*- coding: utf-8 -*-
import sys
import pickle
import os

if len(sys.argv) != 2:
    print "Usage : <nom_fichier_a_traduire>"
    exit()

#Chemin vers le dictionnaire
PATH_DICO="dictionnaire/dictionary.ket"
#Chemin vers le fichier test traduit
PATH_TRADUI=sys.argv[1][:-3]+"ket"

#Ouverture ou creation du fichier dictionnaire
dictio=dict()
if os.path.isfile(PATH_DICO):
    with open(PATH_DICO, 'rb') as fichier:
        dictio=pickle.load(fichier)


#Traitement du fichier test
traduction = open(PATH_TRADUI, "w")
with open(sys.argv[1], "r") as cible :
    for line in cible :
        words = line.split()
        if words[0] == ":" :
            #On réécris la ligne si ":"
            traduction.write(line)
        elif len(words) != 4 :
            #On ignore si la ligne n'est pas correct
            pass
        else :
            mots = list();
            for w in words :
                try :
                    m = dictio[w]
                    if m == None :
                        raise KeyError
                    if len(m.split(" ")) != 1 :
                        #si le mot traduit est décomposé, on ignore
                        break
                    mots += [dictio[w]]
                except KeyError:
                    # En cas de non traduction du mot, on ignore la ligne
                    break
            if len(mots) == 4 :
                #On ignore si l'on obtient pas 4 mots.
                for m in mots :
                    traduction.write(m + " ")
                traduction.write("\n")
traduction.close()
