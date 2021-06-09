# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

import os
import re
import matplotlib.image as image
import matplotlib.pyplot as plt

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
            self._results.append([[self._train[i]], [], []])
        
    def calcula_distancies(self):
        for fitxer in self._train:
            self._distancies[fitxer] = []
            for grup in range(self._k):
                self._distancies[fitxer].append([fitxer.calcula_distancia(
                self._results[grup][0]), self._results[grup][0]])
        error = max([distancia for distancia in [distancia for distancia in [self._distancies[fitxer] for fitxer in self._distancies.keys()]]])
        #return error
        return 0.1 
    
    def calcula_grups(self):
        for fitxer in self._distancies:
            print("ERROR")
        
        
    def calcula_representant(self):
        for group in range(self._k):
            print("ERROR")
        
        
    def get_results(self):
        return self._results