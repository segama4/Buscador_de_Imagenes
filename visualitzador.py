# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

import os
import re
import matplotlib.image as image
import matplotlib.pyplot as plt
import pickle
from abc import ABC, abstractmethod

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

class Visualitzador():
    
    def __init__(self, nom_database):
        fitxer = open(nom_database, 'ab+')
        fitxer.seek(0)
        try:
            self._database = pickle.load(fitxer)
        except:
            print("El fitxer està buit")
        finally:
            fitxer.close()
            print("\nS'ha carregat correctament el database de recuperació!")
        if self._database[0] == "recuperacio":
            self._visualitzador_basic = Visualitzador_Basic_Recuperacio()
            #self._visualitzador_dinamic = Visualitzador_Dinamic_Recuperacio()
        #else:
            #self._visualitzador_basic = Visualitzador_Basic_Agrupacio()
            #self._visualitzador_dinamic = Visualitzador_Dinamic_Agrupacio()
            
    def escull_opcio(self):
        print("\n| 𝙱𝚎𝚗𝚟𝚒𝚗𝚐𝚞𝚝𝚜 𝚊𝚕 𝚅𝚒𝚜𝚞𝚊𝚕𝚒𝚝𝚣𝚊𝚍𝚘𝚛! (𝚟𝚎𝚛𝚜𝚒𝚘 𝟸.𝟸.𝟹) |\n")
        print("𝗘𝘀𝗰𝗼𝗹𝗹𝗶𝘂 𝗾𝘂𝗶𝗻𝗮 𝗼𝗽𝗰𝗶𝗼 𝘃𝗼𝗹𝗲𝘂 𝗿𝗲𝗮𝗹𝗶𝘁𝘇𝗮𝗿:\n\
    1 - Visualitza 5 documents més pròxims.\n\
    2 - Entrar al visualitzador dinàmic.")
        opcio = int(input("Opció: "))
        while opcio != 1 and opcio != 2:
            print("ERROR: Opció Incorrecta! Torna a escollir.")
            opcio = int(input("Opció: "))
        return opcio
    
    def visualitzador_basic(self):
        self._visualitzador_basic.visualitza(self._database)
        
    def visualitzador_dinamic(self):
        self._visualitzador_dinamic.visualitza(self._database)
        

class Visualitzador_Basic(ABC):
    
    @abstractmethod
    def visualitza(self, database):
        raise NotImplementedError
        
        
class Visualitzador_Basic_Recuperacio(Visualitzador_Basic):
    
    def visualitza(self, database):
        print("ERROR")
# =============================================================================
#         if self._database[0] == "recuperacio":
#             for recuperacio in self._database[1]:
#                 
#             if tipus == "img":
#             if len(result) == 1:  
#                 fig, axs = plt.subplots()
#                 axs.axis('off')
#                 axs.imshow(image.imread(result[0][0].location))
#             else:    
#                 fig, axs = plt.subplots(1, len(result))
#                 for i in range(len(result)): 
#                     axs[i].axis('off')
#                     axs[i].imshow(image.imread(result[i][0].location))
#         else:
#             if len(result) == 1: 
#                 fig, axs = plt.subplots()
#                 axs.axis('off')
#                 with open(result[i][0].location, "r") as file:
#                     txt = file.read()
#                 axs.text(0, 1, txt, va = 'top', clip_on = True, 
#                          fontsize = 'xx-small')
#             else:
#                 fig, axs = plt.subplots(1, len(result))
#                 for i in range(len(result)):  
#                     axs[i].axis('off')
#                     with open(result[i][0].location, "r") as file:
#                         txt = file.read()
#                     axs[i].text(0, 1, txt, va = 'top', clip_on = True, 
#                                 fontsize = 'xx-small') 
# =============================================================================
        

class Visualitzador_Basic_Agrupacio(Visualitzador_Basic):
    
    def visualitza(self, database):
        print("ERROR")
