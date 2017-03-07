import sets
import Classe
import Word

class Dico :
	"""
		consigne= Set des consignes sous forme de string
		classe =  dictionnaire des classes
	"""
	def __init__(self, consigne=sets.Set(), classe=dict()) :
		self._consignes = consignes
		self._classes = classes

	def add_class(self, keyclass, classe) :
	def add_class(self, path) :
		current_classe_key= None
		current_classe = None
		with open(path, "r") as fichier :
			for ligne in fichier :
				if ligne[0] == "!" :
					self._consignes.add(ligne[1:])
				elif ligne[0] == ":" :
					current_classe_key = ligne[1:]
					try :
						self._classes[current_classe_key]
						current_classe = 
					except KeyError:
						self._classes[current_classe_key] = Classe.Classe(current_classe_key)
				else :
					mots = ligne.split(";")
					.add_couple((Word.Word(mots[0]), Word.Word(mots[1])))
			for classe in validation.classe();

	def add_cons_for_class(self, keycons, keyclass) :
