# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#


#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

class Index():
    
    def __init__(self, train, vocabulary):
        self._vocabulary = vocabulary
        self._train = train
        self._index = {}
        
    def crea_index(self):
        for i in self._vocabulary.vocabulary:
            self._index[i] = [fitxer for fitxer in self._train if i in fitxer.representation]
        return self._index