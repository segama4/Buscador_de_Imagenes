# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

from agrupador import Agrupador
from visualitzador import Visualitzador_Recuperacio, Visualitzador_Agrupacio
from recuperador import Recuperador
from representacio import Bow, TfIdf
from indexador import Index
from vocabulari import Txt_Vocabulary, Img_Vocabulary, Tfidf_Vocabulary
from classes_arxius import Document, Imatge
import pickle
from tqdm import tqdm
import os

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

class Controller():
    
    def __init__(self, t_document, t_representacio, t_distancia, train):
        self._t_document = t_document
        self._t_representacio = t_representacio
        self._t_distancia = t_distancia
        self._train = train
            
    def prepara_index(self):
        train = []              
        if self._t_document == "text":
            vocabulary = Txt_Vocabulary()
            vocabulary.read("./newsgroup/retrieval/train/vocabulary.txt")
            if self._t_representacio == "bow":
                representador = Bow(self._t_document, vocabulary)
            else:
                vocabulary_tfidf = Tfidf_Vocabulary(self._t_document, vocabulary) 
                vocabulary_tfidf.read("./newsgroup/vocabulary_idf.txt")
                representador = TfIdf(vocabulary, vocabulary_tfidf)
            file_list = os.listdir(self._train)
            for file in file_list: 
                train.append(Document(file, train+"/"+file, vocabulary, representador))
                train[len(train)-1].read()
                train[len(train)-1].get_representation()
        
        else:
            vocabulary = Img_Vocabulary()
            vocabulary.read("./cifrar/retrieval/train/vocabulary.dat")
            if self._t_representacio == "bow":
                representador = Bow(self._t_document, vocabulary)
            else:
                vocabulary_tfidf = Tfidf_Vocabulary() 
                vocabulary_tfidf.read("./cifrar/vocabulary/idf.txt")
                representador = TfIdf(vocabulary, vocabulary_tfidf)
            file_list = os.listdir(self._train)
            for file in file_list: 
                train.append(Imatge(file, train+"/"+file, vocabulary, representador))
                train[len(train)-1].read()
                train[len(train)-1].get_representation()
        self._train = train
        self.crea_index(self._train, vocabulary)
        
    def crea_index(self, train):
        indexador = Index(train)
        index = indexador.crea_index()
        self.guardar("index.pckl", index)
        
    def realitza_recuperacio(self, nom_database, document_query):
        try: 
            index = self.recupera("index.pckl")
            self._recuperador = Recuperador(document_query, index)
            self._recuperador.processa_recuperacio()
            resultat = self._recuperador.get_results()
            self.guardar(nom_database, ["recuperacio", resultat])
        except AssertionError as missatge:
            print("ERROR: ", missatge)
        
    def realitza_agrupacio(self, nom_database, k):
        self._agrupador = Agrupador(self._train, k)
        error = 2 
        while error > 0.2:
            error = self._agrupador.calcula_distancies()
            self._agrupador.calcula_grups()
            self._agrupador.calcula_representant()
            
        resultat = self._agrupador.get_results()
        self.guardar(nom_database, ["agrupacio", resultat])
        
        
    def visualitza_resultats(self, nom_database):
        database = self.recuperar(nom_database) 
        if database[0] == "recuperacio": 
            self._visualitzador = Visualitzador_Recuperacio(database)
        elif database[0] == "agrupacio": 
            self._visualitzador = Visualitzador_Agrupacio(database)
        else:
            print("El fitxer està dañat!")
        self._visualitzador.visualitza()        
        loop = tqdm(total = 4000, position = 0, leave = False)
        for k in range(4000):
            loop.set_description("Tancant visualitzador...".format(k))
            loop.update(1)
        loop.close()
        print("\n--------------------------------------\n")
    
    
    def recuperar(self, nom_database):
        try: 
            fitxer = open(nom_database, 'ab+')
            fitxer.seek(0)
            try:
                database = pickle.load(fitxer)
            except:
                print("El fitxer està buit")
            finally:
                fitxer.close()
                print("\nS'ha carregat correctament el database de recuperació!", database)
            return database
        except:
            raise AssertionError("El fitxer no existeix!")
            
    
    def guardar(self, fitxer, dades):
        fitxer = open(fitxer, 'wb')
        pickle.dump(dades, fitxer)
        fitxer.close()