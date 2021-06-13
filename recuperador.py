# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

from distancies import Cosinus, Intersection

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#


class Recuperador ():
    def __init__(self, document, database, t_document, t_distancia):
        self._t_document = t_document
        self._database = database
        self._document = [arxiu for arxiu in self._database if arxiu.file_name == document][0]
        self._distancies = []
        if t_distancia == "cosinus": 
            self._operador = Cosinus()
        else: 
            self._operador = Intersection()

    def processa_recuperacio(self):
        for fitxer in self._database:
                if fitxer.file_name != self._document.file_name:
                    self._distancies.append((fitxer, self._operador.calcula_distancia(self._document, fitxer)))
        self._distancies = sorted(self._distancies, key=lambda x: x[1])
    
    def get_results(self):
        return [x[0] for x in self._distancies]





# =============================================================================
# #Test
# train = "cifrar/clustering"
# vocabulary1 = vocabulari.Img_Vocabulary()
# vocabulary1.read("cifrar/vocabulary/vocabulary.dat")
# #vocabulary = vocabulari.Tfidf_Vocabulary(vocabulary1)
# #vocabulary.read("im","cifrar/vocabulary/idf.txt")
# representdor = representacio.Bow("tfidf", vocabulary1)
# document = classes_arxius.Imatge("image_1_class_airplane.jpg", "cifrar/clustering/image_1_class_airplane.jpg",vocabulary1, representdor)
# document.read()
# document.get_representation()
# t_dis = "cosinus"
# index = Index("imatge", vocabulary1)
# 
# recuperador = Recuperador(document, index, t_dis)
# 
# recuperador.processa_recuperacio()
# print(str(recuperador.get_results()))
# =============================================================================





    
        



    
        
        