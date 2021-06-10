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
    def __init__(self):
        super().__init__(vocabulary = [])

    def read(self, vocabulary_file):
        with open(vocabulary_file, "r") as vocabulary_file:
            for paraula in vocabulary_file:
                self._vocabulary.append(self._vocabulary, paraula[:-1])