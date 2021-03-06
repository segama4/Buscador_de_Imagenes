# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

from abc import ABC, abstractmethod
import numpy as np
import cv2
import pickle

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

class Vocabulary(ABC):
    def __init__(self, vocabulary):
        self._vocabulary = vocabulary
    
    @abstractmethod
    def read(self, vocabulary_file):
        raise NotImplementedError
        
    @property
    def vocabulary(self):
        try:
            return self._vocabulary
        except:
            raise AssertionError("ERROR: Vocabulary no llegit!")
        
class Txt_Vocabulary(Vocabulary):
    def __init__(self):
        super().__init__(vocabulary = np.array([]))

    def read(self, vocabulary_file):
        with open(vocabulary_file, "r") as vocabulary_file:
            for paraula in vocabulary_file:
                self._vocabulary = np.append(self._vocabulary, paraula[:-1])
        
class Img_Vocabulary(Vocabulary):
    def __init__(self):
        super().__init__(vocabulary = None)

    def read(self, vocabulary_file):
        sift = cv2.SIFT_create()
        matcher = cv2.FlannBasedMatcher() 
        with open(vocabulary_file, 'rb') as fitxer:
            vocabulary = pickle.load(fitxer)
        bow_extractor = cv2.BOWImgDescriptorExtractor(sift, matcher)
        bow_extractor.setVocabulary(vocabulary)
        self._vocabulary = bow_extractor
        
        
class Tfidf_Vocabulary(Vocabulary):
    def __init__(self, vocabulary_normal):
       super().__init__(vocabulary = np.array([]))
       self._vocabulary_normal = vocabulary_normal
       self._vocabulary_dict = {}

    def read(self, tipus, vocabulary_file):
        if tipus == "text": 
            with open(vocabulary_file, "r") as vocabulary_file:   
                for i in vocabulary_file:
                    try:
                        self._vocabulary_dict[(i.split()[0])] = float(i.split()[1])
                        self._vocabulary = np.append(self._vocabulary, float(i.split()[1]))
                    except ValueError:
                        continue
                    
            

        else:
            with open(vocabulary_file, "r") as vocabulary_file:
                for paraula in vocabulary_file:
                    self._vocabulary = np.append(self._vocabulary,float(paraula))
                    
    @property 
    def vocabulary_normal(self):
        return self._vocabulary_normal

    @property
    def vocabulary_dict(self):
        return self._vocabulary_dict