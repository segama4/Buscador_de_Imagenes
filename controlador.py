# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

import os
from agrupador import Agrupador
from visualitzador import Visualitzador
import pickle
from tqdm import tqdm

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

class Controller():
    
    def __init__(self, t_document, t_representacio, t_distancia, t_model, train, k):
        self._t_document = t_document
        self._t_representacio = t_representacio
        self._t_distancia = t_distancia
        self._t_model = t_model
        self._train = train
        self._k = k
        
        
    def prepara_documents(self):
        
        
        
        self._train = resultat
        
    def realitza_recuperacio(self, nom_database):
        
        
        
        self.guardar(nom_database, ["recuperacio", resultat])
        
    def realitza_agrupacio(self, nom_database):
        self._agrupador = Agrupador(self._train_representacions, self.k)
        error = 2 
        while error > 0.3:
            error = self._agrupador.calcula_distancies()
            self._agrupador.recalcula_grups()
            self._agrupador.recalcula_representant()
            
        resultat = self._agrupador.get_results()
        self.guardar(nom_database, ["agrupacio", resultat])
        
    def visualitza_resultats(self, nom_database):
        self._visualitzador = Visualitzador()
        opcio = self._visualitzador.escolleix_opcio()
        while opcio == 1 or opcio == 2:
            if opcio == 1:
                
                
                opcio = self._visualitzador.escolleix_opcio()
            else:
                
        
                opcio = self._visualitzador.escolleix_opcio()
        
        loop = tqdm(total = 5000, position = 0, leave = False)
        for k in range(5000):
            loop.set_description("Tancant visualitzador...".format(k))
            loop.update(1)
        loop.close()
            
    def guardar(self, fitxer, dades):
        fitxer = open(fitxer, 'wb')
        pickle.dump(dades, fitxer)
        fitxer.close()