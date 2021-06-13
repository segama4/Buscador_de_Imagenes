# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

from distancies import Cosinus, Intersection

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#


class Recuperador ():
    def __init__(self, document, database, t_document, t_distancia):
        self._t_document = t_document
        self._database = database
        self._document = [arxiu for arxiu in self._database if arxiu.file_name == document][0]
        self._distancies = []
        if t_distancia == "cosinus": 
            self._operador = Cosinus()
        else: 
            self._operador = Intersection()

    def processa_recuperacio(self):
        for fitxer in self._database:
                if fitxer.file_name != self._document.file_name:
                    self._distancies.append((fitxer, self._operador.calcula_distancia(self._document, fitxer)))
        self._distancies = sorted(self._distancies, key=lambda x: x[1])
    
    def get_results(self):
        return [x[0] for x in self._distancies]











    
        



    
        
        