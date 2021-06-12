# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

from distancies import Cosinus, Intersection
import classes_arxius
import vocabulari
import os
from vocabulari import Img_Vocabulary

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#


class Recuperador ():
    def __init__(self, document, index, t_distancia):
        self._index = index
        self._arxius_analitzar = []
        for i in self._index:
            self._arxius_analitzar.append(self._index[i])
            if self._index[i].file_name == document:
                self._document = self._index[i]
        self._distancies = []
        
        
        
        
        if t_distancia == "cosinus": 
            self._operador = Cosinus()
        else: 
            self._operador = Intersection()

    def processa_recuperacio(self):
        for fitxer in self._arxius_analitzar:
            if fitxer.file_name != self._document.file_name:
                self._distancies.append((fitxer, self._operador.calcula_distancia(self._document, fitxer)))
        self._distancies = sorted(self._distancies, key=lambda x: x[1])
        #No se puede poner self._distancies.sort() y hace lo mismo?
    def get_results(self):
        return [x[0] for x in self._distancies]





#Test
"""train = "cifrar/clustering"
vocabulary = vocabulari.Img_Vocabulary()
vocabulary.read("cifrar/vocabulary/vocabulary.dat")
document = classes_arxius.Imatge("image_1_class_airplane.jpg", "cifrar/clustering/image_1_class_airplane.jpg",vocabulary, "")
document.get_representation()
t_dis = "cosinus"

recuperador = Recuperador(document, train, t_dis)
recuperador.processa_recuperacio()
print(str(recuperador.get_results()))"""




    
        



    
        
        