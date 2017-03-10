#-*- coding: utf-8 -*-
import sets
import Classe
import Word
import unicodedata

class Dico :
	"""
		consignes = Set des consignes sous forme de string
		classes =  Dictionnaire des classes
	"""

	def __init__(self, consignes=sets.Set(), classes=dict()) :
		self._consignes = consignes
		self._classes = classes

	def add_class(self, keyclass, classe) :
		pass

	def add_class(self, path) :
		current_classe_key = None
		current_classe = None
		with open(path, "r") as fichier :
			for ligne in fichier :
				if ligne[0] == "!" :
					self._consignes.add(ligne[1:])
				elif ligne[0] == ":" :
					current_classe_key = ligne[1:]
					try :
						current_classe = self._classes[current_classe_key]
					except KeyError:
						self._classes[current_classe_key] = Classe.Classe(current_classe_key)
						current_classe = self._classes[current_classe_key]
				else :
					mots = ligne.split(";")
					#permet de supprimer les accents
					ligne=unicodedata.normalize('NFD',unicode(ligne,'utf-8')).encode('ascii', 'ignore')
					for i,mot in enumerate(mots):
						tab = mot.split()
						if len(tab)>=2:
							mots[i]='_'.join(tab)
						else:
							mots[i]=tab[0]
					current_classe.add_couple((Word.Word(mots[0]), Word.Word(mots[1])))

	def add_cons_for_class(self, keycons, keyclass) :
		pass
