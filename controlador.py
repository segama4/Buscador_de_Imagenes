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
from distancies import Cosinus, Intersection
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
            
    def prepara_database(self, arxiu = None):
        index = self.recuperar("index.pckl")
        try: 
            database = index[arxiu]
        except:
            raise AssertionError("Index no indicat. Intenta actualitzar-lo.")
        
        if self._t_document == "text":
            vocabulary = Txt_Vocabulary()
            vocabulary.read("./newsgroups/retrieval/vocabulary.txt")
            if self._t_representacio == "bow":
                representador = Bow(self._t_document, vocabulary.vocabulary)
            else:
                vocabulary_tfidf = Tfidf_Vocabulary(vocabulary.vocabulary) 
                vocabulary_tfidf.read(self._t_document, "./newsgroups/vocabulary_idf.txt")
                representador = TfIdf(self._t_document, vocabulary_tfidf)
            train = []   
            #index = 0
            for file in database: 
                #print(index)
                #index += 1
                train.append(Document(file, self._train_+"/"+file, vocabulary, representador))
                train[len(train)-1].read()
                train[len(train)-1].get_representation()
        else:
            vocabulary = Img_Vocabulary()
            vocabulary.read("./cifrar/retrieval/vocabulary.dat")
            if self._t_representacio == "bow":
                representador = Bow(self._t_document, vocabulary.vocabulary)
            else:
                vocabulary_tfidf = Tfidf_Vocabulary(vocabulary.vocabulary) 
                vocabulary_tfidf.read(self._t_document, "./cifrar/vocabulary/idf.txt")
                representador = TfIdf(self._t_document, vocabulary_tfidf)
            train = []   
            #index = 0
            for file in database: 
                #print(index)
                #index += 1
                train.append(Imatge(file, self._train_+"/"+file, vocabulary, representador))
                train[len(train)-1].read()
                train[len(train)-1].get_representation()
        self._train = train
    
    
    def crea_index(self):
        if self._t_document == "text":
            vocabulary = Txt_Vocabulary()
            vocabulary.read("./newsgroups/retrieval/vocabulary.txt")
            if self._t_representacio == "bow":
                representador = Bow(self._t_document, vocabulary.vocabulary)
            else:
                vocabulary_tfidf = Tfidf_Vocabulary(vocabulary.vocabulary) 
                vocabulary_tfidf.read(self._t_document, "./newsgroups/vocabulary_idf.txt")
                representador = TfIdf(self._t_document, vocabulary_tfidf)
            self._index = Index(self._t_document, vocabulary.vocabulary)
            train = []   
            index = 0
            file_list = os.listdir(self._train_)
            for file in file_list: 
                #print(index)
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
                vocabulary_tfidf = Tfidf_Vocabulary(vocabulary.vocabulary) 
                vocabulary_tfidf.read(self._t_document, "./cifrar/vocabulary/idf.txt")
                representador = TfIdf(vocabulary.vocabulary, vocabulary_tfidf)
            self._index = Index(self._t_document, vocabulary.vocabulary)
            train = []   
            index = 0
            file_list = os.listdir(self._train_)
            for file in file_list: 
                #print(index)
                index += 1
                train.append(Imatge(file, self._train_+"/"+file, vocabulary, representador))
                train[len(train)-1].read()
                train[len(train)-1].get_representation()
                self._index.afegeix_document(train[len(train)-1])
        self._train = train
        self.guardar("index.pckl", self._index.recuperar_documents_on_buscar(self._train))
    
    
    def realitza_recuperacio(self, document_query, t_document):
        self.prepara_database(document_query)
        self._recuperador = Recuperador(document_query, self._train, t_document, self._t_distancia)
        self._recuperador.processa_recuperacio()
        self._resultat = ["recuperacio", self._recuperador.get_results()]
        
  
    def realitza_agrupacio(self, k):
        try: 
            self.prepara_database()
            if self._t_distancia == "cosinus": 
                operador = Cosinus()
            else: 
                operador = Intersection()
            self._agrupador = Agrupador(self._train, k, operador)
            final = False
            self._agrupador.calcula_distancies()
            self._agrupador.calcula_grups()
            for i in range(20):
                final = self._agrupador.calcula_representant()
                self._agrupador.calcula_distancies()
                self._agrupador.calcula_grups()
                
            resultat = self._agrupador.get_results()
            self._resultat = ["agrupacio", resultat]
        except:
            raise AssertionError("Index incorrecte!")
        
        
    def visualitza_resultats(self):
        if self._resultat[0] == "recuperacio": 
            self._visualitzador = Visualitzador_Recuperacio(self._resultat)
        elif self._resultat[0] == "agrupacio": 
            self._visualitzador = Visualitzador_Agrupacio(self._resultat)
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
            print("\nS'ha carregat correctament l'índex!")
            return database
        except:
            raise AssertionError("\nL'índex no existeix!")
            
    
    def guardar(self, fitxer, dades):
        fitxer = open(fitxer, 'wb')
        pickle.dump(dades, fitxer)
        fitxer.close()