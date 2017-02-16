import sys
import pickle
import os

#Chemin vers le dictionnaire
PATH_DICO="dictionary.ket"
#Chemin vers les mots traduit en francais
PATH_ADD_FR=sys.argv[1]
#Chemin vers les mots traduit en anglais
PATH_ADD_EN=sys.argv[2]

#Ouverture ou creation du fichier dictionnaire
dictio=dict()
if os.path.isfile(PATH_DICO):
    with open(PATH_DICO, 'rb') as fichier:
        dictio=pickle.load(fichier)

#Traitement des fichiers contenant la traduction
list_mot=list()
with open(PATH_ADD_FR, "r") as file_read_en:
    with open(PATH_ADD_EN, "r") as file_read_fr:
        for line_en,line_fr in [file_read_en,file_read_fr]:
            words_en = line_en.split()[0]#permet d'ignorer les <br>
            words_fr = line_fr.split()[0]
            for key,gtraduc in [words_en,words_fr]:
                list_mot.append([key,gtraduc])

#Traduction des mots
for key,gtraduc in list_mot:
    validation = input(key + " = " + gtraduc + " ? (y/n) : ")
    if(validation == "n"):
        gtraduc=input("Entrez le mot traduit :")
    dico[key] = gtraduc

#Enregistrement du dictionnaire
with open(PATH_DICO, 'wb') as fichier:
    pickle.dump(dictio,fichier)
