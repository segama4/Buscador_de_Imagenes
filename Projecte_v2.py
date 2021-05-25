# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#                                                                            #
#   Dades del projecte:                                                      #
#                                                                            #
#      - Nom de la práctica: Projecte                                        #
#      - Data d'entrega:     9 / 05 / 2021                                   #
#      - Nom dels alumnes:   Sergi Garriga Mas                               #
#                            Sergio Trigueros                                #
#      - Nom professor:      Ernest Valveny Llobet                           #
#      - Assignatura:        Programació Avançada                            #
#      - Universitat:        Universitat Autònoma de Barcelona               #
#      - Funcionalitat:      Tractar similitud d'imatges i arxius            #
#                                                                            #
#+--------------------------------------------------------------------------+#


#+--------------------------------------------------------------------------+#
#   Definim els imports                                                      #
#+--------------------------------------------------------------------------+#

import os Hola
import re
from abc import ABC, abstractmethod
import numpy as np
import collections
import time
import cv2
import pickle
import matplotlib.image as image
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm, rcParams

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
          
        
    def get_distance(self, training_file):
        dist = np.sum(np.minimum(self._representation, 
                                 training_file.representation))
        den = min(np.sum(self._representation),
                              np.sum(training_file.representation))
        if den != 0:
            return 1 - (dist / den)
        else:
            return 1


class Buscador():
    
    def __init__(self, vocabulary_txt, vocabulary_img):
        self._vocabulary_txt = vocabulary_txt
        self._vocabulary_img = vocabulary_img

    def prepare_test_database(self, train):
        self._database = []
        file_list = os.listdir(train)
        for file in file_list: 
            if ".txt" in file:
                for letter in file: 
                        guio = 0
                        punt = 0
                        etiqueta = ""
                        for lletra in file:
                            if lletra == ".":
                                punt += 1 
                            if guio == 1 and punt == 0:
                                etiqueta += lletra 
                            if lletra == "_":
                                guio += 1
                        etiqueta = re.sub("[^a-zA-Z0-9]", " ", etiqueta)
                self._database.append(Document(file, train+"/"+file, 
                                               self._vocabulary_txt, 
                                               etiqueta))
                self._database[len(self._database)-1].read()
                self._database[len(self._database)-1].get_representation()

            else:
                for letter in file: 
                        guio = 0
                        punt = 0
                        etiqueta = ""
                        for lletra in file:
                            if lletra == ".":
                                punt += 1 
                            if guio == 3 and punt == 0:
                                etiqueta += lletra 
                            if lletra == "_":
                                guio += 1
                self._database.append(Imatge(file, train+"/"+file, 
                                             self._vocabulary_img, 
                                             etiqueta))
                self._database[len(self._database)-1].read()
                self._database[len(self._database)-1].get_representation()
    
    def make_clasification(self, base_file, k):
        try: 
            result = [[x, base_file.get_distance(x)] for x in self._database]
            result = sorted(result, key=lambda file : file[1])
            print("\n",base_file.file_name,": ",[[x[0].file_name, x[1]] for x in result[:k]])
            return(result[:k])
        except:
            raise AssertionError("ERROR: Ha ocurregut un error durant la " + 
                                 "clasificació de l'arxiu.")
            
    def view_results(self, result, tipus):  
        if tipus == "img":
            if len(result) == 1:  
                fig, axs = plt.subplots()
                axs.axis('off')
                axs.imshow(image.imread(result[0][0].location))
            else:    
                fig, axs = plt.subplots(1, len(result))
                for i in range(len(result)): 
                    axs[i].axis('off')
                    axs[i].imshow(image.imread(result[i][0].location))
        else:
            if len(result) == 1: 
                fig, axs = plt.subplots()
                axs.axis('off')
                with open(result[i][0].location, "r") as file:
                    txt = file.read()
                axs.text(0, 1, txt, va = 'top', clip_on = True, 
                         fontsize = 'xx-small')
            else:
                fig, axs = plt.subplots(1, len(result))
                for i in range(len(result)):  
                    axs[i].axis('off')
                    with open(result[i][0].location, "r") as file:
                        txt = file.read()
                    axs[i].text(0, 1, txt, va = 'top', clip_on = True, 
                                fontsize = 'xx-small') 


#+--------------------------------------------------------------------------+#
#    Definim les funcions                                                    #
#+--------------------------------------------------------------------------+#

def retrieval(test, train, tipus, vocabulary_file, k):
        try: 
            if tipus == "txt":  
                vocabulary_txt = []
                with open(vocabulary_file, "r") as file:
                    for paraula in file:
                        vocabulary_txt.append(paraula[:-1])
                        
                google = Buscador(vocabulary_txt, None)
                google.prepare_test_database(train)
                file_list = os.listdir(test)
                for file in file_list:
                    base_file = Document(file, test+"/"+file, vocabulary_txt, None)
                    base_file.read()
                    base_file.get_representation()
                    result = google.make_clasification(base_file, k)
                    google.view_results(result, tipus)

            else:
                sift = cv2.SIFT_create()
                matcher = cv2.FlannBasedMatcher() 
                with open(vocabulary_file, 'rb') as fitxer:
                    vocabulary = pickle.load(fitxer)
                bow_extractor = cv2.BOWImgDescriptorExtractor(sift, matcher)
                bow_extractor.setVocabulary(vocabulary)
                vocabulary_img = bow_extractor
            
                google = Buscador(None, vocabulary_img)
                google.prepare_test_database(train)
                file_list = os.listdir(test)
                for file in file_list:       
                    base_file = Imatge(file, test+"/"+file, vocabulary_img, None)
                    base_file.read()
                    base_file.get_representation()
                    result = google.make_clasification(base_file, k)
                    google.view_results(result, tipus)
                    
            return True
        
        except:
            raise AssertionError("ERROR: Ha ocurregut un error durant l'execució!")
        

# =============================================================================
#     Iniciem la funció
# =============================================================================

start_time = time.time()
try:
    print("\nResultats:\n")
    
    """Comentar un o l'altre (imatge o text) depenent del que vulgueu vuscar"""
    
    #retrieval("cifar/test", "cifar/train", "img", "vocabulary.dat", 5)
    retrieval("newsgroups/test", "newsgroups/train", "txt", "vocabulary.txt", 5)

except AssertionError as missatge:
    print(missatge)

print("\nTemps =", time.time()-start_time, "segons.")