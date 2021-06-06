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

import os
import re
from abc import ABC, abstractmethod
import numpy as np
import collections
import time
import cv2
import pickle
import matplotlib.image as image
import matplotlib.pyplot as plt
from buscador import Buscador

#+--------------------------------------------------------------------------+#
#    Definim les funcions                                                    #
#+--------------------------------------------------------------------------+#

def retrieval(t_document, t_representacio, t_distancia, t_model, train):
        try: 
            buscador = Buscador(t_document, t_representacio, t_distancia, t_model, train)
            conjunt_train = buscador.crea_models()
            buscador.visualitza_resultats(conjunt_train)

        except:
            raise AssertionError("ERROR: Ha ocurregut un error durant l'execució!")
        

# =============================================================================
#     Iniciem la funció
# =============================================================================

start_time = time.time()
try:
    print("\nResultats:\n")
    
    """Comentar un o l'altre (imatge o text) depenent del que vulgueu vuscar"""
    
    #retrieval("imatge", "bow", "interseccio", "agrupament", "newsgroups")
    retrieval("text", "tf-idf", "cosinus", "vocabulary.txt", "recuperacio", "cifrar")

except AssertionError as missatge:
    print(missatge)

print("\nTemps =", time.time()-start_time, "segons.")


# =============================================================================
# try: 
#             if tipus == "txt":  
#                 vocabulary_txt = []
#                 with open(vocabulary_file, "r") as file:
#                     for paraula in file:
#                         vocabulary_txt.append(paraula[:-1])
#                         
#                 google = Buscador(vocabulary_txt, None)
#                 google.prepare_test_database(train)
#                 file_list = os.listdir(test)
#                 for file in file_list:
#                     base_file = Document(file, test+"/"+file, vocabulary_txt, None)
#                     base_file.read()
#                     base_file.get_representation()
#                     result = google.make_clasification(base_file, k)
#                     google.view_results(result, tipus)
# 
#             else:
#                 sift = cv2.SIFT_create()
#                 matcher = cv2.FlannBasedMatcher() 
#                 with open(vocabulary_file, 'rb') as fitxer:
#                     vocabulary = pickle.load(fitxer)
#                 bow_extractor = cv2.BOWImgDescriptorExtractor(sift, matcher)
#                 bow_extractor.setVocabulary(vocabulary)
#                 vocabulary_img = bow_extractor
#             
#                 google = Buscador(None, vocabulary_img)
#                 google.prepare_test_database(train)
#                 file_list = os.listdir(test)
#                 for file in file_list:       
#                     base_file = Imatge(file, test+"/"+file, vocabulary_img, None)
#                     base_file.read()
#                     base_file.get_representation()
#                     result = google.make_clasification(base_file, k)
#                     google.view_results(result, tipus)
# =============================================================================
