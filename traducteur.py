import sys
import pickle
import os

#Chemin vers le dictionnaire
PATH_DICO="dictionary.ket"
#Chemin vers le fichier test traduit
PATH_TRADUI=sys.argv[1][:-3]+"ket"

#Ouverture ou creation du fichier dictionnaire
dictio=dict()
if os.path.isfile(PATH_DICO):
    with open(PATH_DICO, 'rb') as fichier:
        dictio=pickle.load(fichier)


tradui=open(PATH_TRADUI, "r")
#Traitement du fichier de test
with open(sys.argv[1], "r") as atraduire:
    for line in atraduire:
        words = line.split()
        for key in words:
            if key!="<br>":
                tradui.write(dictio[key]+" ")
            else if key==":":
                tradui.write(":")
        tradui.write("\n")
tradui.close()
