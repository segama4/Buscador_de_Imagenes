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
import time
import cv2
import pickle
from agrupador import Agrupador
from buscador import Buscador 
from classes_arxius import Arxiu, Imatge, Document
from controlador import Controller
from visualitzador import Visualitzador
from vocabulari import Vocabulary, Txt_Vocabulary, Img_Vocabulary

#+--------------------------------------------------------------------------+#
#    Definim les funcions                                                    #
#+--------------------------------------------------------------------------+#

def retrieval(document_type, representation_type, distance_type, model_type, train):
        try: 
            google = Buscador()
            google.iniciar_controlador(document_type, representation_type, distance_type, train)
            google.preparar_test()
            if model_type == "recuperacio":
                
                
                
                
            else:
                
            
            
            
            
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