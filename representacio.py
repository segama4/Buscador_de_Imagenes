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
            for word in self._vocabulary.vocabulary:
                if word not in counter.keys(): 
                    representation.append(0)
                else:
                    representation.append(counter[word])
            return np.array(representation)
    
        else: 
            img_gray = cv2.cvtColor(file, cv2.COLOR_BGR2GRAY)
            representacio = compute_bow_images(img_gray, self._vocabulary)
            return representacio
    

class TfIdf(Representacio):
    
    def __init__(self, tipus, vocabulary):
        super().__init__(tipus, vocabulary)
    
    def calcula_representacio(self, arxiu, index):
        if self._tipus == "text":
            representation = []
            locf = index.train
            n_arxius = len(os.listdir(locf))
            counter = collections.Counter(np.array(re.sub("[^a-zA-Z0-9]", " ", arxiu.lower()).split()))
            df = 0
            for i in self._vocabulary:
                if i not in counter.keys(): 
                    tf = 0
                else:
                    tf =counter[i] / len(counter)
                df = len (index[i])
                representation.append(tf * log10(n_arxius/df))

            return np.array(representation)
        else:
            representation_tf = []
            locf = index.train
            n_arxius = len(os.listdir(locf))
            img_gray = cv2.cvtColor(arxiu, cv2.COLOR_BGR2GRAY)
            representacio = compute_bow_images(img_gray, self._vocabulary)
            for i in representacio:
                tf = i / representacio.size
                idf = log10 (n_arxius/(len(index[i]))) #Pendiente de cambio
                representation_tf.append(tf*idf)

            return np.array (representation_tf)


                
            
            


            
            


        
