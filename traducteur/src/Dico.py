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
		try:
			self._classes[keyclass]
			s=raw_input("La classe "+keyclass+" existe deja voulez-vous la remplacer?(o/n)")
			if s=="o":
				raise KeyError
			elif s=="n":
				keyclass=raw_input("Nouveau nom : ")
				self.add_class(keyclass, classe)
			else:
				self.add_class(keyclass, classe)
		except KeyError:
			self._classes[keyclass]= classe

	def modif_class(self) :
			choice=[]
			for i,key in enumerate(self._classes.keys()):
				print i,": ",key
				choice.append(key)
			s=input("Selectioner un id de classes :")
			self._classes[choice[int(s)]].modif_couples()

	def get_classe(self, c) :
		try :
			return self._classes[c]
		except KeyError :
			return None

	def get_classes_in_tab(self) :
		tab = []
		for i,c in enumerate(self._classes) :
			tab += [[i, c]]
		return tab

	def add_class_from_file(self, path) :
		current_classe_key = None
		with open(path, "r") as fichier :
			for ligne in fichier :
				if ligne[0] == "!" :
					self._consignes.add(ligne[1:-1])
				elif ligne[0] == ":" :
					current_classe_key = ligne[:-1]
					try :
						self._classes[current_classe_key]
					except KeyError as e:
						self._classes[current_classe_key] = Classe.Classe(current_classe_key)
						print self._classes[current_classe_key]
				else :
					mots = ligne.split(";")
					for i,mot in enumerate(mots):
						tab = mot.split()
						if len(tab)>=2:
							mots[i]='_'.join(tab)
						else:
							mots[i]=tab[0]
					self._classes[current_classe_key].add_couple((Word.Word(mots[0]), Word.Word(mots[1])))

	def add_cons_for_class(self, keycons, keyclass) :
		pass
