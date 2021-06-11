# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

from abc import ABC, abstractmethod
from indexador import Indexador
import numpy as np

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

class Distancia(ABC):
    def __init__(self, train, document):
        raise NotImplementedError
    
    @abstractmethod
    def calcula_representacio(self, arxiu):
        raise NotImplementedError
        
class Cosinus(Distancia):
    def __init__(self, train, document):
        print("ERROR")
        
        
        
    def calcula_distancia(self, arxiu_query, arxiu_2):
        dist = np.sum(np.minimum(arxiu_query.representation, 
                                 arxiu_2.representation))
        den = min(np.sum(arxiu_query.representation),
                              np.sum(arxiu_2.representation))
        if den != 0:
            return 1 - (dist / den)
        else:
            return 1
    def calcula_representacio(self, arxiu):
        return
        
        
        
class Intersection(Distancia):
    def __init__(self, train, document):
        self._indexador = Indexador(train, document)
        
        
        
    def calcula_distancia(self, arxiu_query, arxiu_2):
        print("ERROR")
    
        