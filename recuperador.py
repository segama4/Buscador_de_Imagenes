# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

from vocabulari import Vocabulary, Img_Vocabulary
from indexador import Indexador
from distancies import Cosinus, Intersection
import classes_arxius
import os

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#


class Recuperador ():
    def __init__(self, document, train, t_distancia):
        self._train = train
        self._document = [document for doc in os.listdir(train) if document.file_name == doc][0]
        
        self._distancies = []
        self._offset = 0
        if t_distancia == "cosinus": 
            self._operador = Cosinus(self._train, self._document)
        else: 
            self._operador = Intersection(self._train, self._document)

    def processa_recuperacio(self):
        if self._document.tipus() == "Imatge":
            for fitxer in os.listdir(self._train):
                fitx = classes_arxius.Imatge(fitxer, self._train+"/"+fitxer, self._document.vocabulary, "")
                fitx.get_representation()
                if fitxer != self._document:
                    self._distancies.append(self._operador.calcula_distancia(self._document, fitx))

        self._distancies.sort()
    
    def get_results(self):
        return [self._document, self._distancies]



"""
Funcion por si quieres comprobarlo


train = "cifrar/clustering"
vocabulary = Img_Vocabulary()
vocabulary.read("cifrar/vocabulary/vocabulary.dat")
document = classes_arxius.Imatge("image_1_class_airplane.jpg", "cifrar/clustering/image_1_class_airplane.jpg",vocabulary, "")
document.get_representation()
t_dis = "cosinus"

recuperador = Recuperador(document, train, t_dis)
recuperador.processa_recuperacio()
print(str(recuperador.get_results()))"""




    
        



    
        
        