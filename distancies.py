# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

from abc import ABC, abstractmethod
import numpy as np
np.seterr(divide='ignore', invalid='ignore')
from math import sqrt

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

class Distancia(ABC):
    @abstractmethod
    def calcula_distancia(self, arxiu_query, arxiu_2):
        raise NotImplementedError
     
        
class Intersection(Distancia):
    def calcula_distancia(self, arxiu_query, arxiu_2, agrupa = None):
        if agrupa == None:
            dist = np.sum(np.minimum(arxiu_query.representation, arxiu_2.representation))
            den = min(np.sum(arxiu_query.representation), np.sum(arxiu_2.representation))
            if den != 0: return 1 - (dist / den)
            else: return 1
        else:
            dist = np.sum(np.minimum(arxiu_query.representation, arxiu_2))
            den = min(np.sum(arxiu_query.representation), np.sum(arxiu_2))
            if den != 0: return 1 - (dist / den)
            else: return 1


class Cosinus(Distancia):
    def calcula_distancia(self, arxiu_query, arxiu_2, agrupa = None):
        if agrupa == None:
            dist = np.sum(arxiu_query.representation * arxiu_2.representation,dtype=np.uint64)
            den1 = sqrt(np.sum(arxiu_query.representation**2,dtype=np.uint64))
            den2 = sqrt(np.sum(arxiu_2.representation**2,dtype=np.uint64))
            return 1 - ((dist)/(den1*den2))
        else:
            dist = np.sum(arxiu_query.representation * arxiu_2, dtype=np.uint64)
            den1 = sqrt(np.sum(arxiu_query.representation**2, dtype=np.uint64))
            den2 = sqrt(np.sum(arxiu_2**2,dtype=np.uint64))
            return 1 - ((dist)/(den1*den2))

    