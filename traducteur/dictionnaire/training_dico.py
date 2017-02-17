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
en=[]
fr=[]
with open(PATH_ADD_FR, "r") as file_read_en:
    with open(PATH_ADD_EN, "r") as file_read_fr:
        en = [ligne for ligne in file_read_en]
        fr = [ligne for ligne in file_read_fr]

relation = [[en[i], fr[i]] for i in range(len(en))]
for [line_en,line_fr] in relation :
    word_en = line_en[:-1]
    word_fr = line_fr[:-1]
    list_mot.append([word_en,word_fr])

#Traduction des mots
for key,gtraduc in list_mot:
    validation = raw_input(key + " = " + gtraduc + " ? (y/n) : ")
    if(validation == "n"):
        gtraduc=raw_input("Entrez le mot traduit :")
    print "test\n"
    dictio[key] = gtraduc

#Enregistrement du dictionnaire
with open(PATH_DICO, 'wb') as fichier:
    pickle.dump(dictio,fichier)
