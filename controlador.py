# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

from agrupador import Agrupador
from visualitzador import Visualitzador
import pickle
from tqdm import tqdm

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

class Controller():
    
    def __init__(self, t_document, t_representacio, t_distancia, train, k):
        self._t_document = t_document
        self._t_representacio = t_representacio
        self._t_distancia = t_distancia
        self._train = train
        self._k = k
        
        
    def prepara_documents(self):
# =============================================================================
#         if tipus == "txt":  
#                 vocabulary_txt = []
#                 with open(vocabulary_file, "r") as file:
#                     for paraula in file:
#                         vocabulary_txt.append(paraula[:-1])
#                         
#                 google = Buscador(vocabulary_txt, None)
#                 google.prepare_test_database(train)
#                 file_list = os.listdir(test)
#                 for file in file_list:
#                     base_file = Document(file, test+"/"+file, vocabulary_txt, None)
#                     base_file.read()
#                     base_file.get_representation()
#                     result = google.make_clasification(base_file, k)
#                     google.view_results(result, tipus)
# 
#         else:
#             sift = cv2.SIFT_create()
#             matcher = cv2.FlannBasedMatcher() 
#             with open(vocabulary_file, 'rb') as fitxer:
#                 vocabulary = pickle.load(fitxer)
#             bow_extractor = cv2.BOWImgDescriptorExtractor(sift, matcher)
#             bow_extractor.setVocabulary(vocabulary)
#             vocabulary_img = bow_extractor
#         
#             google = Buscador(None, vocabulary_img)
#             google.prepare_test_database(train)
#             file_list = os.listdir(test)
#             for file in file_list:       
#                 base_file = Imatge(file, test+"/"+file, vocabulary_img, None)
#                 base_file.read()
#                 base_file.get_representation()
#                 result = google.make_clasification(base_file, k)
#                 google.view_results(result, tipus)
# =============================================================================
        
        print("ERROR")
        #self._train = resultat
        
    def realitza_recuperacio(self, nom_database):
        print("ERROR")
        
        
        self.guardar(nom_database, ["recuperacio", self._t_document, resultat])
        
    def realitza_agrupacio(self, nom_database):
        self._agrupador = Agrupador(self._train, self._k)
        error = 2 
        while error > 0.3:
            error = self._agrupador.calcula_distancies()
            self._agrupador.calcula_grups()
            self._agrupador.calcula_representant()
            
        resultat = self._agrupador.get_results()
        self.guardar(nom_database, ["agrupacio", self._t_document, resultat])
        
    def visualitza_resultats(self, nom_database):
        self._visualitzador = Visualitzador(nom_database)
        opcio = self._visualitzador.escull_opcio()
        while opcio == 1 or opcio == 2:
            if opcio == 1:
                self._visualitzador.visualitzador_basic()                
                opcio = self._visualitzador.escolleix_opcio()
            else:
                self._visualitzador.visualitzador_dinamic()
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