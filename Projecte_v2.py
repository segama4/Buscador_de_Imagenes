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

import time
from buscador import Buscador


#+--------------------------------------------------------------------------+#
#    Definim les funcions                                                    #
#+--------------------------------------------------------------------------+#

def retrieval(mode, nom_database, t_document, t_representacio, t_distancia, t_model, train):
        buscador = Buscador(t_document, t_representacio, t_distancia, t_model, train)
        if mode == 1: 
            buscador.crea_models(nom_database)
        else: 
            buscador.visualitza_resultats(nom_database)
            

# =============================================================================
#     Iniciem la funció
# =============================================================================

start_time = time.time()
try:
    opcio = 1
    while opcio == 1 or opcio == 2:
        
        print(""".______    _______ .__   __. ____    ____  __  .__   __.   _______  __    __  .___________. __
                |   _  \  |   ____||  \ |  | \   \  /   / |  | |  \ |  |  /  _____||  |  |  | |           ||  |
                |  |_)  | |  |__   |   \|  |  \   \/   /  |  | |   \|  | |  |  __  |  |  |  | `---|  |----`|  |
                |   _  <  |   __|  |  . `  |   \      /   |  | |  . `  | |  | |_ | |  |  |  |     |  |     |  |
                |  |_)  | |  |____ |  |\   |    \    /    |  | |  |\   | |  |__| | |  `--'  |     |  |     |__|
                |______/  |_______||__| \__|     \__/     |__| |__| \__|  \______|  \______/      |__|     (__) 

                𝚂𝚎𝚕𝚎𝚌𝚌𝚒𝚘𝚗𝚊 𝚚𝚞𝚎 𝚟𝚘𝚕𝚜 𝚏𝚎𝚛!\n""")
        
        try:
            opcio = int(input("1- Crea els models.\n2- Visualitza resultats. (Atenció: Abans has de crear els models!)\n"))
        except:
            print("ERROR: Opció NO vàlida. Tria una opció correcta!")
            opcio = int(input("1- Crea els models.\n2- Visualitza resultats. (Atenció: Abans has de crear els models!)\nAltre número implica sortir.\n"))
        
        if opcio == 1:
            print("\n𝚂𝚎𝚕𝚎𝚌𝚌𝚒𝚘𝚗𝚊 𝚎𝚕𝚜 𝚙𝚊𝚛𝚊𝚖𝚎𝚝𝚛𝚎𝚜 𝚊𝚖𝚋 𝚎𝚕𝚜 𝚚𝚞𝚎 𝚟𝚘𝚕𝚜 𝚝𝚛𝚎𝚋𝚊𝚕𝚕𝚊𝚛!")
            
            start_time = time.time()
            retrieval(1, "database.txt", "text", "tf-idf", "cosinus", "vocabulary.txt", "recuperacio", "cifrar")
            print("\nFet! Temps =", time.time()-start_time, "segons.")
            
        elif opcio == 2:
            retrieval(2, "database.txt","imatge", "bow", "interseccio", "agrupament", "newsgroups")
        
        else:
            print("𝙵𝚒𝚗𝚜 𝚊𝚟𝚒𝚊𝚝!")

except AssertionError as missatge:
    print(missatge)






# =============================================================================
# import os
# import re
# from abc import ABC, abstractmethod
# import numpy as np
# import collections
# import time
# import cv2
# import pickle
# import matplotlib.image as image
# import matplotlib.pyplot as plt
# from buscador import Buscador
# =============================================================================
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
