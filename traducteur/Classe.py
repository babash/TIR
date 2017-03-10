#-*- coding: utf-8 -*-
from Word import *

class Classe :
	def __init__(self, nom_classe, couples_mots=list()) :
		self._nom = nom_classe
		self._couples_mots = couples_mots

	def __str__(self) :
		for i in range(len(self._couples_mots)):
			s+= [ligne + "\n" for ligne in [mot1 + mot2 for mot1,mot2 in self._couples_mots]]
		return s

	def modif_couples(self) :
			for i,key in enumerate(self._couples_mots.keys()):
				print i,": ",key
			i=input("Selectioner un id de couples :")
			s=input("Reecriver le couples :")
			#blablalalalaalbalaballalab

	def to_string(self, parametre) :
		string = self._nom + "\n"
		taille = len(self._couples_mots)
		for i in range(taille) :
			j = i + 1
			while j < taille :
				string += self._couples_mots[i][0].get_def(parametre) + " " + self._couples_mots[i][1].get_def(parametre) + " " + self._couples_mots[j][0].get_def(parametre) + " " + self._couples_mots[j][1].get_def(parametre) + "\n"
				j += 1
		return string

	def add_couple(self, couple) :
		self._couples_mots += [couple]

	def validation(self) :
		pass

# a = SlimShady("a")
# b = SlimShady("b")
# c = SlimShady("c")
# d = SlimShady("d")


# v = Vandal(":ma-classe", [[a, b], [a, c], [a, d], [b, c]])
# print v.to_string("castor")
