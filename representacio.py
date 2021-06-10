# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

from abc import ABC, abstractmethod
import cv2
import numpy as np

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

class Representacio(ABC):
    @abstractmethod
    def calcula_representacio(self, arxiu):
        raise NotImplementedError
        
class Bow(Representacio):
    def calcula_representacio(self, bow_extractor, location):
        def compute_bow_images(img, bow_extractor):
            sift = cv2.SIFT_create()
            keypoints = sift.detect(img)
            if keypoints != []:
                bow = bow_extractor.compute(img, keypoints)
            else:
                bow = np.zeros((1, bow_extractor.descriptorSize()))
            return bow
        
        img = cv2.imread(location)
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        representacio = compute_bow_images(img_gray, bow_extractor)
        return representacio
    

class TfIdf(Representacio):
     def calcula_representacio(self, arxiu):
        print("ERROR")
        
        # Falta expressar la fòrmula
