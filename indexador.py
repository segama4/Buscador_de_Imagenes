# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#


#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

class Index():
    
    def __init__(self, tipus, vocabulary):
        self._tipus = tipus
        self._index = {}
        self._mida = int(vocabulary.descriptorSize()) if tipus == 'imatge' else (len(vocabulary)-1)
        for i in range(self._mida):
            self._index[i]=[]

    def afegeix_document(self, document):
        for i in range (self._mida): 
            if float(document.representation[i]) != 0:
                self._index[i].append(document.file_name)

    def recuperar_documents_on_buscar(self, database):
        index = {}
        for arxiu in database: 
            documents_on_buscar = []
            for i in range(self._mida):
                if float(arxiu.representation[i]) != 0:
                    for i in self._index[i]:
                        if i not in documents_on_buscar:
                            documents_on_buscar.append(i)
            documents_on_buscar = list(set(documents_on_buscar))
            index[arxiu.file_name] = documents_on_buscar
        return index