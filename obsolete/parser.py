import sys
import pickle
import os


#Chemin vers les mots a traduire
PATH_WORD=sys.argv[1][:-4]+"_en"
EXTENTION=sys.argv[1][-4:]
classe=[]
i=-1
#Traitement du fichier de test
with open(sys.argv[1], "r") as file_read:
    for line in file_read:
        words = line.split()
            if words[0]!=":":
                i+=1
                classe.append([word[1],{}])
            else

#Ecriture du fichier a traduire
numero_fichier=1
file=open(PATH_WORD+str(numero_fichier)+EXTENTION, "w")
if traduce:
    for i,key in enumerate(dictio.keys()):
        if i==500:
            file.close()
            numero_fichier+=1
            file=open(PATH_WORD+str(numero_fichier)+EXTENTION, "w")
        if dictio[key]==None:
            file.write(key +"\n")


#Enregistrement du dictionnaire
with open(PATH_DICO, 'wb') as fichier:
    pickle.dump(dictio,fichier)

#Fermeture du fichier des mots a traduire
if traduce==True:
    print "Le fichier de mot a traduire a etait genere"
else:
    print "Le dictionnaire est pret"
