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

def retrieval():
    buscador = Buscador()
    opcio = True
    while opcio:
        opcio = buscador.tria_menu()
                  
# =============================================================================
#     Iniciem la funció
# =============================================================================

retrieval()




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