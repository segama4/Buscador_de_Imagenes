# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

from indexador import Indexador
from distancies import Cosinus, Intersection

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#


class Recuperador ():
    def __init__(self, document, train, t_distancia):
        self._document = [document for document in train if document.nom == document][0]
        self._train = train
        self._distancies = []
        self._offset = 0
        if t_distancia == "cosinus": self._operador = Cosinus()
        else: self._operador = Intersection(train, document)

    def processa_recuperacio(self):
        for fitxer in self._train:
            if fitxer != self._document:
                self._distancies.append(fitxer.calcula_distancia (self._document))

        self._distancies.sort()
    
    def get_results(self):
        return [self._document, self._distancies]
    
        



    
        
        