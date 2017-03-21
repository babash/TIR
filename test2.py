#!/usr/bin/python
# coding: utf-8

from gensim.models import word2vec
"""from nltk.corpus import brown"""
import logging, re, codecs
from time import time
from gensim.models.word2vec import LineSentence
import multiprocessing

#fichier = open("trate2.txt", "r")
t = time()
print "fichier ouvert :",time()-t,"s"
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


#liste de phrase et chaque phrase est une liste de mot
#brown_vecs = word2vec.Word2Vec(brown.sents())
#sentences = [ "the quick brown fox jumps over the lazy dogs","you go home now to sleep"]
#vocab = [s.encode('utf-8').split() for s in sentences]
#voc_vec = word2vec.Word2Vec(vocab, min_count = 4)
phrase = list()
#lignes  = fichier.readlines()
#regex = re.compile(r'[\n\r\t]')

'''
i = 0
print "go parse :",time()-t,"s"
with open("traiteComplet2.txt","r") as fichier :
	for ligne in fichier:
		#ligne = regex.sub(" ", ligne)
		#ligne = unicode(ligne, "utf-8")
		#ligne = ligne.encode('utf-8')
		phrase.append(ligne.split())
		i+=1
'''
i = 0
print "Debut test :",time()-t,"s"
#vocab = [s.encode('utf-8').split() for s in phrase]

#model = word2vec.Word2Vec(phrase, min_count = 4)
model = word2vec.Word2Vec(LineSentence("traiteComplet2.txt"),min_count = 5, size = 400, window=5, workers = multiprocessing.cpu_count())
model.init_sims(replace=True)

model.save('wikiFR.model')

print "Debut modele :",time()-t,"s"
test = model.doesnt_match("le les est des".split())
print "Dans : ['le', 'les', 'est', 'des'], l'intru est : ", test

test = model.similarity('droite', 'gauche')
print "La similarite entre 'droite' et 'gauche' est de : ", test

test = model.most_similar(['épisode'])
print "Les mot les plus similaires a 'épisode' sont : "
for t in test:
	print " -- '", t[0] , "' avec un score de ", t[1]

more_examples = ["il ils elle", "froid chaud blanc", "a avait est"] 
for example in more_examples:
	a, b, x = example.split()
	predicted = model.most_similar([x, b], [a])[0][0]
	print "'%s' est a '%s' ce que '%s' est a '%s'" % (a, b, x, predicted)

fichierQuestion = open('questions-words.txt', "r")
s=codecs.open('questions-words.txt', 'r','utf-8')


print "Test d'accuracy"
lignes  = s.readlines()
acc = []
ns = -1
nomS = []
flag = True
nbLigne = 0

for ligne in lignes:
	#ligne = str(ligne)
	if ligne.startswith(':'):
		ligne = ligne.split(':')
		if flag != True:
			acc[ns] = acc[ns]/nbLigne
		ns = ns + 1
		nomS.append(ligne[1])
		acc.append(0)
		flag = False	
		nbLigne = 0
	else:
		nbLigne = nbLigne + 1
		a, b, x, y = ligne.split()
		predicted = model.most_similar([x, b], [a])[0][0]
		if predicted.decode('utf-8') == y:
			acc[ns] = acc[ns] + 1
	
acc[ns] = (float(acc[ns])/nbLigne)*100
i = 0
for n in nomS:
	print n, " : ", acc[i], '%'
#accuracy = model.accuracy(s)
#print "resultat : ", accuracy
