import sys
import pickle
import os

#Chemin vers le dictionnaire
PATH_DICO="dictionary.ket"
#Chemin vers les mots a traduire
PATH_WORD=sys.argv[1][:-3]+"html"

traduce=False
#Ouverture ou creation du fichier dictionnaire
dictio=dict()
if os.path.isfile(PATH_DICO):
    with open(PATH_DICO, 'rb') as fichier:
        dictio=pickle.load(fichier)

#Traitement du fichier de test
with open(sys.argv[1], "r") as file_read:
    for line in file_read:
        words = line.split()
        for key in words:
            if key!=":":
                try:
                    if (dictio[key]):
                        pass
                except:
                        traduce=True
                        dictio[key]=None


#Ecriture du fichier a traduire
if traduce:
    with open(PATH_WORD, "w") as file:
        for key in dictio.keys():
            if dictio[key]==None:
                file.write(key + " <br>\n")


#Enregistrement du dictionnaire
with open(PATH_DICO, 'wb') as fichier:
    pickle.dump(dictio,fichier)

#Fermeture du fichier des mots a traduire
if traduce==True:
    print "Le fichier de mot a traduire a etait genere"
else:
    print "Le dictionnaire est pret"
