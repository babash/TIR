#-*- coding: utf-8 -*-
class Word :
	def __init__(self, mot) :
		self._string = mot
		self._dico = dict()
		self._dico["default"] = mot

	def get_def(self, parametre) :
		try :
			r = self._dico[parametre]
		except KeyError :
			r = self._dico["default"]
		return r

	def add_def(self, parametre, definition) :
		self._dico[parametre] = definition

	def remove_space(self):
		self._string.replace(" ","_")

	def __str__(self) :
		return self._string
