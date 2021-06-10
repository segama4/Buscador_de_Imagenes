# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#                                                                            #
#   Dades del projecte:                                                      #
#                                                                            #
#      - Nom de la práctica: Projecte Versió 2                               #
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

from buscador import Buscador

#+--------------------------------------------------------------------------+#
#    Definim les funcions                                                    #
#+--------------------------------------------------------------------------+#

def retrieval(nom_database):
    buscador = Buscador(nom_database)
    opcio = True
    vegada = 0
    while opcio:
        opcio = buscador.tria_menu(vegada)
        vegada += 1
                  
# =============================================================================
#     Iniciem la funció
# =============================================================================

retrieval("database.pckl")




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