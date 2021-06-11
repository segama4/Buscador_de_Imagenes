# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

import random

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

class Agrupador():
    
    def __init__(self, train, k):
        self._train = train
        self._k = k
        self._results = []
        self._distancies = {}
        for i in range(k):
            self._results.append([[self._train[random.randint[0, len(self._train)-1]]], [], []])
        
    def calcula_distancies(self):
        for fitxer in self._train:
            self._distancies[fitxer] = []
            for grup in range(self._k):
                self._distancies[fitxer].append(fitxer.calcula_distancia(self._results[grup][0]))
        error = max([distancia for distancia in [distancia for distancia in [self._distancies[fitxer] for fitxer in self._distancies.keys()]]])
        return error
    
    def calcula_grups(self):
        for fitxer in self._distancies:
            self._results[self._distancies[fitxer].index(min(self._distancies[fitxer]))][2].append(fitxer)
        
    def calcula_representant(self):
        for group in range(self._k):
            mitjana
            self._results[group][1].append(mitjana)
            
        
    
    def get_results(self):
        return self._results