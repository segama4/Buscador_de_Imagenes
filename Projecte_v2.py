# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#                                                                            #
#   Dades del projecte:                                                      #
#                                                                            #
#      - Nom de la práctica: Projecte Versió 2                               #
#      - Data d'entrega:     13 / 06 / 2021                                   #
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

