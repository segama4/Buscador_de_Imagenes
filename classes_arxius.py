# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

import re
from abc import ABC, abstractmethod
import numpy as np
import collections
import cv2
import matplotlib.image as image

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

class Arxiu(ABC):
    
    def __init__(self, file_name, location, vocabulary, label):
        self._file_name = file_name
        self._location = location
        self._vocabulary = vocabulary
        self._label = label
        self._file = ""
        self._representation = np.array([])
        
    @property
    def file_name(self):
        return self._file_name
    
    @property
    def location(self):
        return self._location
    
    @property
    def vocabulary(self):
        return self._vocabulary
    
    @property
    def label(self):
        return self._label
    
    @property
    def representation(self):
        return self._representation
    
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
    def get_distance(self, training_file):
        raise NotImplementedError()
        
        
class Imatge(Arxiu):
   
    def __init__(self, file_name, location, vocabulary, label):
        super().__init__(file_name, location, vocabulary, label)
        
    def read(self):
        self._file = image.imread(self._location)
            
    def get_representation(self):

        def compute_bow_images(img, bow_extractor):
            sift = cv2.SIFT_create()
            keypoints = sift.detect(img)
            if keypoints != []:
                bow = bow_extractor.compute(img, keypoints)
            else:
                bow = np.zeros((1, bow_extractor.descriptorSize()))
            return bow
        
        img = cv2.imread(self._location)
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        self._representation = compute_bow_images(img_gray, self._vocabulary)
        
    def get_distance(self, training_file):
        dist = np.sum(np.minimum(self._representation, 
                                 training_file.representation))
        den = min(np.sum(self._representation),
                              np.sum(training_file.representation))
        if den != 0:
            return 1 - (dist / den)
        else:
            return 1
    

class Document(Arxiu):
     
    def _init_(self, file_name, location, vocabulary, label):
        super().__init__(file_name, location, vocabulary, label)

    def read(self):
        with open(self._location, "r") as file:
            self._file = file.read()
       
    def get_representation(self):
        
        counter = collections.Counter(np.array(re.sub("[^a-zA-Z0-9]", " ", 
                                            self._file.lower()).split()))
        representation = []
        for word in self._vocabulary:
            if word not in counter.keys(): 
                representation.append(0)
            else:
                representation.append(counter[word])
        self._representation = np.array(representation)