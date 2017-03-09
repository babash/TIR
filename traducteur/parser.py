#-*- coding: utf-8 -*-
import sys
import sets

""" Prends en entrée un fichier de test de relation entre mots en anglais, donne en sortie un ou plusieurs nouveaux fichiers
dans lesquels pour chaque classe on a la liste des couples de mots lui appartenant"""

if len(sys.argv) != 3 and len(sys.argv) != 2:
	print "Usage : <name_file> <consigne=default>"
if len(sys.argv) == 2 :
	consigne = "default"
else :
	consigne = sys.argv[2]

nom_fichier = sys.argv[1]
fichier = open(nom_fichier, "r")

dict_classe = dict()
last_classe = None


for ligne in fichier :
	if ligne[0] == ":" :
		dict_classe[ligne[:-1]] = sets.Set()
		last_classe = ligne[:-1]
	else :
		mots = ligne.split(" ")
		dict_classe[last_classe].add(mots[0] + " ; " + mots[1])
		dict_classe[last_classe].add(mots[2] + " ; "  + mots[3][:-1])

fichier.close()

nb_fichier = 1
fichier_out = open(nom_fichier[:-4] + str(nb_fichier) + ".out", "w")
i = 0

fichier_out.write("! " + consigne + "\n")

for classe in dict_classe :
	if i + len(dict_classe[classe]) > 450 :
		fichier_out.close()
		nb_fichier += 1
		fichier_out = open(nom_fichier[:-4] + str(nb_fichier) + ".out", "w")
		fichier_out.write("! " + consigne + "\n")
		i = 0
	fichier_out.write(classe + "\n")
	i += 1
	for elem in dict_classe[classe] :
		fichier_out.write(elem + "\n")
		i += 1

fichier_out.close()
