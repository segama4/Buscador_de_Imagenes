# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

from distancies import Cosinus, Intersection
import vocabulari
import classes_arxius
import representacio
from indexador import Index

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#


class Recuperador ():
    def __init__(self, document, index, t_distancia):
        self._index = index
        self._documents_on_buscar, self._document = self._index.recuperar_documents_on_buscar(document)
        self._distancies = []
        self.__arxius_analitzar = []
        if t_distancia == "cosinus": 
            self._operador = Cosinus()
        else: 
            self._operador = Intersection()

    def processa_recuperacio(self):
        for fitxer in self._documents_on_buscar:
            if fitxer.file_name != self._document.file_name:
                self._distancies.append((fitxer, self._operador.calcula_distancia(self._document, fitxer)))
        self._distancies = sorted(self._distancies, key=lambda x: x[1])
    
    def get_results(self):
        return [x[0] for x in self._distancies]





#Test
train = "cifrar/clustering"
vocabulary1 = vocabulari.Img_Vocabulary()
vocabulary1.read("cifrar/vocabulary/vocabulary.dat")
#vocabulary = vocabulari.Tfidf_Vocabulary(vocabulary1)
#vocabulary.read("im","cifrar/vocabulary/idf.txt")
representdor = representacio.Bow("tfidf", vocabulary1)
document = classes_arxius.Imatge("image_1_class_airplane.jpg", "cifrar/clustering/image_1_class_airplane.jpg",vocabulary1, representdor)
document.read()
document.get_representation()
t_dis = "cosinus"
index = Index("imatge", vocabulary1)

recuperador = Recuperador(document, index, t_dis)

recuperador.processa_recuperacio()
print(str(recuperador.get_results()))





    
        



    
        
        