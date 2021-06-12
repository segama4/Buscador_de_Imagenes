# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#


import os
import classes_arxius


#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

class Index():
    
    def __init__(self, train, vocabulary):
        self._vocabulary = vocabulary
        self._train = train
        self._index = {}
        
    def crea_index(self):

        #NO FUNCIONA
        """for i in self._vocabulary.vocabulary:
            self._index[i] = [fitxer for fitxer in self._train if i in fitxer.representation]
        if self._document.tipus() == "Imatge":
            for fitxer in os.listdir(self._train):
                fitx = classes_arxius.Imatge(fitxer, self._train+"/"+fitxer, self._document.vocabulary, "")
                fitx.get_representation()
                if fitx.file_name != self._document.file_name:
                    if fitx._representation in self._document.vocabulary.vocabulary:
                        self._index[fitxer] = True


        
        
        if self._document.tipus() == "Imatge":
            for fitxer in os.listdir(self._train):
                fitx = classes_arxius.Imatge(fitxer, self._train+"/"+fitxer, self._document.vocabulary, "")
                fitx.get_representation()
                if fitx.file_name != self._document.file_name:
                    if fitx._representation in self._document.vocabulary.vocabulary:
                        self._index[fitxer] = True"""


        
        
        
    @property
    def index(self):
        return self._index