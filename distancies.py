# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

from abc import ABC, abstractmethod
import numpy as np
from math import sqrt
from indexador import Index
#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

class Distancia(ABC):
    def __init__(self, train, document):
        raise NotImplementedError
    
"""    @abstractmethod
    def calcula_representacio(self, arxiu):
        raise NotImplementedError"""
        
class Intersection(Distancia):
    def __init__(self, train, document):
        self._train = train
        self._document = document
        
        
        
    def calcula_distancia(self, arxiu_query, arxiu_2):
        dist = np.sum(np.minimum(arxiu_query.representation, 
                                 arxiu_2.representation))
        den = min(np.sum(arxiu_query.representation),
                              np.sum(arxiu_2.representation))
        if den != 0:
            return 1 - (dist / den)
        else:
            return 1

        
        
        
class Cosinus(Distancia):
    def __init__(self, train, document):
        self._indexador = Index(train, document)
        self._indexador.crea_index()
        
        
        
    def calcula_distancia(self, arxiu_query, arxiu_2):
        #if self._indexador.index[arxiu_2.file_name] == True:
        dist = np.sum(arxiu_query.representation * arxiu_2.representation)
        den1 = sqrt(np.sum(arxiu_query.representation**2))
        den2 = sqrt(np.sum(arxiu_2.representation**2))
        return 1 - ((dist)/(den1*den2))
        #else:
        #    return 1

        