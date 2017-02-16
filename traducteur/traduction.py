from translate import translator

files = []
for i in range(5) :
	files += ["words_english_"]

fichier = open("word2vec/trunk/questions-words.txt")

dico = dict();
#gs = goslate.Goslate(service_urls=['http://translate.google.fr'])

for ligne in fichier :
	if ligne[0] == ":" :
		pass
	else :
		mots_ligne = ligne.split(" ")
		for mot in mots_ligne :
			try :
				if(dico[mot]) :
					pass
			except :
				trad = translator("en", "fr", mot)
				validation = input(mot + " = " + trad + " ? (y/n) : ")
				if(validation == "y") :
					dico[mot] = trad

