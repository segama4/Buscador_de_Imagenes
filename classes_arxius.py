# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

import re
from abc import ABC, abstractmethod
import cv2
import matplotlib.image as image

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

class Arxiu(ABC):
    
    def __init__(self, file_name, location, vocabulary, representador):
        self._file_name = file_name
        self._location = location
        self._vocabulary = vocabulary
        self._label = None
        self._file = ""
        self._representador = representador
        
    @property
    def file_name(self):
        return self._file_name
    
    @property
    def location(self):
        return self._location
    
    @property
    def vocabulary(self):
        return self._vocabulary
    @vocabulary.setter
    def vocabulary(self, rep):
        self._representation =  rep
    
    @property
    def label(self):
        if self._label == None:
            self.get_label()
        return self._label
    
    @property
    def representation(self):
        return self._representation
    
    @representation.setter
    def representation(self, rep):
        self._representation =  rep
    
    @property
    def file(self):
        if self._file != "":
            return self._file 
        else:
            raise AssertionError("ERROR: No file read!")
    
    @abstractmethod            
    def read(self, ):
        raise NotImplementedError()
        
    @abstractmethod        
    def get_representation(self):
        raise NotImplementedError()
    
    @abstractmethod        
    def visualitza(self, training_file):
        raise NotImplementedError()
    
    
class Imatge(Arxiu):
   
    def __init__(self, file_name, location, vocabulary, representador):
        super().__init__(file_name, location, vocabulary, representador)
        
    def read(self):
        self._file = image.imread(self._location)
        self._file_representacio = cv2.imread(self._location)
            
    def get_representation(self):
        self._representation = self._representador.calcula_representacio(self._file_representacio)
        

    def visualitza(self, axs):
            axs.axis('off')
            axs.imshow(self.file)
     
    def get_label(self):
        for letter in self._file_name: 
            guio = 0
            punt = 0
            etiqueta = ""
            for lletra in self._file_name:
                if lletra == ".":
                    punt += 1 
                if guio == 1 and punt == 0:
                    etiqueta += lletra 
                if lletra == "_":
                    guio += 1
            self._label = re.sub("[^a-zA-Z0-9]", " ", etiqueta)


class Document(Arxiu):
     
    def _init_(self, file_name, location, vocabulary, representador):
        super().__init__(file_name, location, vocabulary, representador)

    def read(self):
        with open(self._location, "r") as file:
            self._file = file.read()
       
    def get_representation(self):
        self._representation = self._representador.calcula_representacio(self._file)
        
    def visualitza(self, axs):
        axs.axis('off')
        axs.text(0, 1, self._file, va = 'top', clip_on = True, fontsize = 'xx-small') 
        
    def get_label(self):
        for letter in self._file_name: 
            guio = 0
            punt = 0
            etiqueta = ""
            for lletra in self._file_name:
                if lletra == ".":
                    punt += 1 
                if guio == 1 and punt == 0:
                    etiqueta += lletra 
                if lletra == "_":
                    guio += 1
            etiqueta = re.sub("[^a-zA-Z0-9]", " ", etiqueta)