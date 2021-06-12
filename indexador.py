# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#


#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

class Index():
    
    def __init__(self, tipus, vocabulary):
        self._vocabulary = vocabulary
        self._tipus = tipus
        self._index = {}
        self._mida = vocabulary.descriptorSize() if tipus == 'imatge' else len(vocabulary)
        for i in range(self._mida):
            self._index[i]=[]
        self._vocabulary = None

    def afegeix_document(self, document):
        for i in range (self._mida): 
            print(document.representation)
            if float(document.representation[0][i]) != 0:
                self._index[i].append(document)

    def recuperar_documents_on_buscar(self, document):
        documents_on_buscar = []
        for i in range(self._mida):
            if float(document.representation[i]) != 0:
                documents_on_buscar.extend(self._index[i])
        documents_on_buscar = list(set(documents_on_buscar))
        return documents_on_buscar