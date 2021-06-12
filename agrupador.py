# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

import random
import numpy as np

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

class Agrupador():
    
    def __init__(self, train, k, operador):
        self._train = train
        self._k = k
        self._operador = operador
        self._results = []
        self._distancies = {}
        for i in range(k):
            self._results.append([self._train[random.randint(0, len(self._train)-1)], []])
        
    def calcula_distancies(self):
        for fitxer in self._train:
            self._distancies[fitxer] = []
            for grup in range(self._k):
                self._distancies[fitxer].append(self._operador.calcula_distancia(fitxer, self._results[grup][0]))
        error = max([distancia for distancia in [distancia for distancia in [self._distancies[fitxer] for fitxer in self._distancies.keys()]]])
        return error
    
    def calcula_grups(self):
        for fitxer in self._distancies:
            self._results[self._distancies[fitxer].index(min(self._distancies[fitxer]))][1].append(fitxer)
        
    def calcula_representant(self):
        for group in range(self._k):
            vegada = 0 
            for arxiu in self._results[group][1]:
                if vegada == 0:
                    mitjana = arxiu.representation 
                    vegada += 1
                else:
                    mitjana += np.sum(arxiu.representation)
            mitjana = mitjana/len(self._results[group][1])
            llista_distancies = []
            for arxiu in self._results[group][1]:
                llista_distancies.append((arxiu, self._operador.calcula_distancia(arxiu, mitjana, True)))
            new = sorted(llista_distancies, key=lambda x: x[1])[0][0]
            if self._results[group][0] == new: acaba = True
            else: acaba = False
            self._results[group][1] = []
            return acaba 
        
    def get_results(self):
        return self._results