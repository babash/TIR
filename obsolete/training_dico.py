import sys
import pickle
import os


def validation(context,key,gtraduc):
    regex_carac = r"^\[(?P<ind>\-?[0-9]*)\] (?P<new>[A-Za-z'\-])"
    regex_range =  r"^\[(?P<indmin>\-?[0-9]*)\:(?P<indmax>\-?[0-9]*)\] (?P<new>[A-Za-z'\-]*)"
    regex_sup_carac =  r"^\-\[(?P<ind>\-?[0-9]*)\]"
    regex_sup_range =  r"^\-\[(?P<indmin>\-?[0-9]*)\:(?P<indmax>\-?[0-9]*)\]"
    regex_norm = r"^[A-Za-z'\-]*"

    validation = False
    while(!validation):
        gtemp=gtraduc
        print "context:"+str(context)
        str_input=raw_input(key + " = " + gtraduc + " ?: "))

        # aide
        if(str_input=="--help"):
            print "Syntax:\n|"+regex_carac+"\n|"+regex_range+"\n|"+regex_sup_carac+"\n|"+regex_sup_range+"\n|"+regex_norm
        # mise en minuscule
        if(str_input=="--low"):
            gtemp.tolower()
        # mise en format capitale
        elif(str_input=="cap"):
            gtemp.captitalize()
        # cas d'une traduction completement differente
        elif re.match(regex_norm, str_input):
            gtemp=str_input
        # cas d'un remplacement d'un caractere
        elif re.match(regex_carac, str_input):
            m=re.search(regex_carac,str_input)
            ind=atoi(m.group("ind"))
            if len(m.group("new"))!=1:
                print "Error: bad syntax (--help)"
            elif ind>len(gtemp) || ind<-len(gtemp):
                print "Error: out of bound (--help)"
            else:
             gtemp[atoi(m.group("ind"))]=m.group("new")

        # cas d'une suppression d'un caractere
        elif  re.match(regex_sup_carac, str_input):
            m=re.search(regex_sup_carac,str_input)
            ind=atoi(m.group("ind"))
            if len(m.group("new"))!=1:
                print "Error: bad syntax (--help)"
            elif ind>len(gtemp) || ind<-len(gtemp):
                print "Error: out of bound (--help)"
            else:
             gtemp=gtemp[:ind] + gtemp[ind+1:]



        annule=raw_input(str_input+"?: "))
        if annule!='a':
            gtraduc=gtemp
            validation=True
        if annule!='k':
            gtraduc=gtemp

    return gtraduc
    
#Chemin vers le dictionnaire
PATH_DICO="dictionary.ket"
#Chemin vers les mots traduit en francais
PATH_ADD_FR=sys.argv[1]
#Chemin vers les mots traduit en anglais
PATH_ADD_EN=sys.argv[2]

#Ouverture ou creation du fichier dictionnaire
dictio=dict()
if os.path.isfile(PATH_DICO):
    with open(PATH_DICO, 'rb') as fichier:
        dictio=pickle.load(fichier)

#Traitement des fichiers contenant la traduction
list_mot=list()
en=[]
fr=[]
with open(PATH_ADD_FR, "r") as file_read_en:
    with open(PATH_ADD_EN, "r") as file_read_fr:
        en = [ligne for ligne in file_read_en]
        fr = [ligne for ligne in file_read_fr]

relation = [[en[i], fr[i]] for i in range(len(en))]
for [line_en,line_fr] in relation :
    word_en = line_en[:-1]
    word_fr = line_fr[:-1]
    list_mot.append([line_en,word_en,word_fr])

#Traduction des mots
for context,key,gtraduc in list_mot:
    dictio[key] = validation(context,key,gtraduc)
#Enregistrement du dictionnaire
with open(PATH_DICO, 'wb') as fichier:
    pickle.dump(dictio,fichier)
