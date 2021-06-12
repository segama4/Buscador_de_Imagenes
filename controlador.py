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
        self._train_ = train
            
    def prepara_index(self):
        if self._t_document == "text":
            vocabulary = Txt_Vocabulary()
            vocabulary.read("./newsgroups/retrieval/vocabulary.txt")
            if self._t_representacio == "bow":
                representador = Bow(self._t_document, vocabulary.vocabulary)
            else:
                vocabulary_tfidf = Tfidf_Vocabulary(self._t_document, vocabulary.vocabulary) 
                vocabulary_tfidf.read("./newsgroups/vocabulary_idf.txt")
                representador = TfIdf(vocabulary.vocabulary, vocabulary_tfidf)
            self._index = Index(self._t_document, vocabulary.vocabulary)
            train = []   
            index = 0
            file_list = os.listdir(self._train_)
            for file in file_list: 
                print(index)
                index += 1
                train.append(Document(file, self._train_+"/"+file, vocabulary, representador))
                train[len(train)-1].read()
                train[len(train)-1].get_representation()
                self._index.afegeix_document(train[len(train)-1])
        
        else:
            vocabulary = Img_Vocabulary()
            vocabulary.read("./cifrar/retrieval/vocabulary.dat")
            if self._t_representacio == "bow":
                representador = Bow(self._t_document, vocabulary.vocabulary)
            else:
                vocabulary_tfidf = Tfidf_Vocabulary() 
                vocabulary_tfidf.read("./cifrar/vocabulary/idf.txt")
                representador = TfIdf(vocabulary.vocabulary, vocabulary_tfidf)
            self._index = Index(self._t_document, vocabulary.vocabulary)
            train = []   
            index = 0
            file_list = os.listdir(self._train_)
            for file in file_list: 
                print(index)
                index += 1
                train.append(Imatge(file, self._train_+"/"+file, vocabulary, representador))
                train[len(train)-1].read()
                train[len(train)-1].get_representation()
                self._index.afegeix_document(train[len(train)-1])
            self._index.borra_representacions()
        self._train = train
        self.guardar("index.pckl", self._index)
        
        
    def realitza_recuperacio(self, nom_database, document_query):
        try: 
            index = self.recuperar("index.pckl")
            self._recuperador = Recuperador(document_query, index, self._t_distancia)
            self._recuperador.processa_recuperacio()
            resultat = self._recuperador.get_results()
            self.guardar(nom_database, ["recuperacio", resultat])
        except:
            print("\nERROR: No hi ha cap index creat!")
        
  
        
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
        loop = tqdm(total = 3000, position = 0, leave = False)
        for k in range(3000):
            loop.set_description("Tancant visualitzador...".format(k))
            loop.update(1)
        loop.close()
        print("\n--------------------------------------\n")
    
    
    def recuperar(self, nom_database):
        try: 
            fitxer = open(nom_database, 'ab+')
            fitxer.seek(0)
            database = pickle.load(fitxer)
            fitxer.close()
            print("\nS'ha carregat correctament el database de recuperació!", database)
            return database
        except:
            raise AssertionError("\nEl fitxer que necessites no existeix!")
            
    
    def guardar(self, fitxer, dades):
        fitxer = open(fitxer, 'wb')
        pickle.dump(dades, fitxer)
        fitxer.close()