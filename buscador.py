# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

from controlador import Controller

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

class Buscador():
    
    def __init__(self, t_document, t_representacio, t_distancia, t_model, train, k = 0):
        self._t_model = t_model
        self._controlador = Controller(t_document, t_representacio, t_distancia, train, k)
        
    def crea_model(self, nom_database):
        self._controlador.prepara_documents()
        
        if self._t_model == "recuperacio":
            self._controlador.realitza_recuperacio(nom_database)
        else:
            self._controlador.realitza_agrupacio(nom_database)
        
    def visualitza_resultats(self, nom_database):
        self._controlador.visualitza_resultats(nom_database)






















































def prepare_test_database(self, train):
        self._database = []
        file_list = os.listdir(train)
        for file in file_list: 
            if ".txt" in file:
                for letter in file: 
                        guio = 0
                        punt = 0
                        etiqueta = ""
                        for lletra in file:
                            if lletra == ".":
                                punt += 1 
                            if guio == 1 and punt == 0:
                                etiqueta += lletra 
                            if lletra == "_":
                                guio += 1
                        etiqueta = re.sub("[^a-zA-Z0-9]", " ", etiqueta)
                self._database.append(Document(file, train+"/"+file, 
                                               self._vocabulary_txt, 
                                               etiqueta))
                self._database[len(self._database)-1].read()
                self._database[len(self._database)-1].get_representation()

            else:
                for letter in file: 
                        guio = 0
                        punt = 0
                        etiqueta = ""
                        for lletra in file:
                            if lletra == ".":
                                punt += 1 
                            if guio == 3 and punt == 0:
                                etiqueta += lletra 
                            if lletra == "_":
                                guio += 1
                self._database.append(Imatge(file, train+"/"+file, 
                                             self._vocabulary_img, 
                                             etiqueta))
                self._database[len(self._database)-1].read()
                self._database[len(self._database)-1].get_representation()
    
def make_clasification(self, base_file, k):
    try: 
        result = [[x, base_file.get_distance(x)] for x in self._database]
        result = sorted(result, key=lambda file : file[1])
        print("\n",base_file.file_name,": ",[[x[0].file_name, x[1]] for x in result[:k]])
        return(result[:k])
    except:
        raise AssertionError("ERROR: Ha ocurregut un error durant la " + 
                             "clasificació de l'arxiu.")
        
def view_results(self, result, tipus):  
    if tipus == "img":
        if len(result) == 1:  
            fig, axs = plt.subplots()
            axs.axis('off')
            axs.imshow(image.imread(result[0][0].location))
        else:    
            fig, axs = plt.subplots(1, len(result))
            for i in range(len(result)): 
                axs[i].axis('off')
                axs[i].imshow(image.imread(result[i][0].location))
    else:
        if len(result) == 1: 
            fig, axs = plt.subplots()
            axs.axis('off')
            with open(result[i][0].location, "r") as file:
                txt = file.read()
            axs.text(0, 1, txt, va = 'top', clip_on = True, 
                     fontsize = 'xx-small')
        else:
            fig, axs = plt.subplots(1, len(result))
            for i in range(len(result)):  
                axs[i].axis('off')
                with open(result[i][0].location, "r") as file:
                    txt = file.read()
                axs[i].text(0, 1, txt, va = 'top', clip_on = True, 
                            fontsize = 'xx-small') 