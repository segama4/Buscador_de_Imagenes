# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

from abc import ABC, abstractmethod
import cv2
import numpy as np
import collections
import re
import os
from math import log10

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

def compute_bow_images(img, bow_extractor):
            sift = cv2.SIFT_create()
            keypoints = sift.detect(img)
            if keypoints != []:
                bow = bow_extractor.compute(img, keypoints)
            else:
                bow = np.zeros((1, bow_extractor.descriptorSize()))
            return bow

class Representacio(ABC):
    def __init__(self, tipus, vocabulary):
        self._tipus = tipus
        self._vocabulary = vocabulary
        
    @abstractmethod
    def calcula_representacio(self, arxiu):
        raise NotImplementedError
        
        
class Bow(Representacio):
    
    def __init__(self, tipus, vocabulary):
        super().__init__(tipus, vocabulary)
        
    def calcula_representacio(self, file):
        
        

        if self._tipus == "text": 
            counter = collections.Counter(np.array(re.sub("[^a-zA-Z0-9]", " ", file.lower()).split()))
            representation = []
            for word in self._vocabulary:
                if word not in counter.keys(): 
                    representation.append(0)
                else:
                    representation.append(counter[word])
            return np.array(representation)
    
        else: 
            img_gray = cv2.cvtColor(file, cv2.COLOR_BGR2GRAY)
            representacio = compute_bow_images(img_gray, self._vocabulary)
            return representacio[0]
    

class TfIdf(Representacio):
    
    def __init__(self, tipus, vocabulary):
        super().__init__(tipus, vocabulary)
    
    def calcula_representacio(self, file):
        if self._tipus == "text":
            representation = []
            counter = collections.Counter(np.array(re.sub("[^a-zA-Z0-9]", " ", file.lower()).split()))
            cont = 0
            for i in self._vocabulary.vocabulary:
                representation.append((counter[cont]/len(counter))*i)
                cont += 1
            return np.array(representation)

        else:
            representation = []
            img_gray = cv2.cvtColor(file, cv2.COLOR_BGR2GRAY)
            representacio = compute_bow_images(img_gray, self._vocabulary.vocabulary_normal)
            cont = 0
            for i in self._vocabulary.vocabulary:
                representation.append((representacio[cont]/len(representacio))*i)
                cont += 1
            return np.array (representation)


                
            
            


            
            


        
