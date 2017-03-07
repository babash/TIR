import sys
import pickle
import os
import Dico

if len(sys.argv) != 2 :
	print "Usage : <nom_fichier_dictionnaire>"
	exit(1)

PATH_DICO = sys.argv[1]

if os.path.isfile(PATH_DICO):
    with open(PATH_DICO, 'rb') as fichier:
        dico = pickle.load(fichier)
else :
	dico = Dico()

r = input("Que voulez vous faire:\n 1: Ajouter une classe depuis un fichier.\n 2: Ajouter une classe manuellement.\n 3: Modifier une classe\n 4: Ajouter une interprétation\n 5: Créer un fichier test")

if r == "1" :
	name_file = input("Saisissez le chemin du fichier :")
	dico.add_classe(name_file)
	pass
elif r == "2" :
	pass
elif r == "3" :
	pass
elif r == "4" :
	pass
elif r == "5" :
	pass
else :
	print "Error nombre entré"
	exit(1)

