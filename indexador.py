# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#


#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

from pickle import NONE


class Index():
    
    def __init__(self, tipus, vocabulary):
        self._tipus = tipus
        self._index = {}
        self._mida = int(vocabulary.vocabulary.descriptorSize()) if tipus == 'imatge' else len(vocabulary)
        for i in range(self._mida):
            self._index[i]=[]
        self._representacions = "si"
        self._pos = 0

    def afegeix_document(self, document):
        for i in range (self._mida): 
            if float(document.representation[i]) != 0:
                self._index[i].append(document)

    def recuperar_documents_on_buscar(self, nom_document):
        document = None
        for i in self._index.keys():
            for j in self._index[i]:
                if j.file_name == nom_document:
                    document = j
        documents_on_buscar = []
        self._pos += 1
        for i in range(self._mida):
            if float(document.representation[i]) != 0:
                documents_on_buscar.extend(self._index[i])
        documents_on_buscar = list(set(documents_on_buscar))
        return documents_on_buscar, document
    
    def borra_representacions(self):
        for index in self._index.keys():
            for arxiu in self._index[index]:
                arxiu.representation = None
                arxiu.vocabulary = None
        self._representacions = "no"
                
    def calcula_representacions(self):
        for index in self._index.keys():
            for arxiu in self._index[index]:
                arxiu.get_representation()
        self._representacions = "si"
        
    @property
    def representations(self):
        return self._representacions