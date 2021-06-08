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


#+----------------------------------2----------------------------------------+#
#    Definim les funcions                                                    #
#+--------------------------------------------------------------------------+#

def retrieval(mode, nom_database, t_document, t_representacio, t_distancia, t_model, train, k):
    buscador = Buscador(t_document, t_representacio, t_distancia, t_model, train, k)
    if mode == 1: 
        buscador.crea_model(nom_database)
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
            opcio = int(input("1- Crea els models.\n2- Visualitza resultats. (Atenció: Abans has de crear els models!)\n\nAltre número implica sortir.\n\n"))
        except:
            print("ERROR: Opció NO vàlida. Tria una opció correcta!")
            opcio = int(input("1- Crea els models.\n2- Visualitza resultats. (Atenció: Abans has de crear els models!)\n\nAltre número implica sortir.\n\n"))
        
        if opcio == 1 or opcio == 2:
            print("\n𝚂𝚎𝚕𝚎𝚌𝚌𝚒𝚘𝚗𝚊 𝚎𝚕𝚜 𝚙𝚊𝚛𝚊𝚖𝚎𝚝𝚛𝚎𝚜 𝚊𝚖𝚋 𝚎𝚕𝚜 𝚚𝚞𝚎 𝚟𝚘𝚕𝚜 𝚝𝚛𝚎𝚋𝚊𝚕𝚕𝚊𝚛!")
            
            t_document = 0; t_representacio = 0; t_distancia = 0; t_model = 0; k = 0;
            
            database = "database.pckl"
            #database = input("Arxiu del database: ")
            
            while t_document == 0:
                t_document = int(input("Document:\n\n1- Imatge\n2- Text\n\n"))
                if t_document == 1: t_document = "imatge"; train = "cifrar"
                elif t_document == 2: t_document = "text"; train = "newsgroups"
                else: t_document = 0; print("\nOpció NO vàlida!\n")
            
            while t_representacio == 0:
                t_representacio = int(input("Representació:\n\n1- Bow\n2- Tf-idf\n\n"))
                if t_representacio == 1: t_representacio = "bow"
                elif t_representacio == 2: t_representacio = "tf-idf"
                else: t_representacio = 0; print("\nOpció NO vàlida!\n")
                
            while t_distancia == 0:
                t_distancia = int(input("Distància:\n\n1- Imatge\n2- Text\n\n"))
                if t_distancia == 1: t_document = "imatge"
                elif t_distancia == 2: t_distancia = "text"
                else: t_distancia = 0; print("\nOpció NO vàlida!\n")
                
            while t_model == 0:
                t_model = int(input("Distància:\n\n1- Recuperació\n2- Agrupament\n\n"))
                if t_model == 1: t_document = "recuperacio"
                elif t_model == 2: 
                    t_model = "agrupament";
                    k = int(input("\nIntrodueix el número de grups: \n"))
                else: t_model = 0; print("\nOpció NO vàlida!\n")
            
            start_time = time.time()
            retrieval(opcio, database, t_document, t_representacio, t_distancia, t_model, train, k)
            print("\nFi! Temps =", time.time()-start_time, "segons.\n\n--------------------------------------\n\n")
            
        else:
            print("\n𝙵𝚒𝚗𝚜 𝚊𝚟𝚒𝚊𝚝!")

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
