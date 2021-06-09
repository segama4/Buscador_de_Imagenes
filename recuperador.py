import os
import re
import matplotlib.image as image
import matplotlib.pyplot as plt


class Recuperador ():
    def __init__(self, document, train):
        self._document = document
        self._train = train
        self._distancies = []
        self._offset = 0

    def calcula_distancies (self):
        for fitxer in self._train:
            self._distancies.append(fitxer.calcula_distancia (self._document))

        self._distancies.sort()

    def mostrar_documents (self):
        if len(self._distancies) == 0:
            return None
        else:
            return self._distancies[self._offset*5:(self._offset*5)+4]

    def avançar_5 (self):
        self._offset += 1

    def retornar_5 (self):
        if self._offset != 0:
            self._offset -= 1
        else:
            raise IndexError
        



    
        
        