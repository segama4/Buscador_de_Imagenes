# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

from controlador import Controller

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

class Buscador():
    
    def __init__(self, nom_database):
        self._database = nom_database
        
    def crea_model(self, nom_database, k, document_query):
        self._controlador.prepara_documents()
        
        if self._t_model == "recuperacio":
            self._controlador.realitza_recuperacio(nom_database, document_query)
        else:
            self._controlador.realitza_agrupacio(nom_database, k)
        
    def visualitza_resultats(self, nom_database):
        self._controlador.visualitza_resultats(nom_database)

    def tria_menu(self, vegada):
        buscador = None
        nom_database = "database.pckl"
        
        if vegada == 0:    
            print(""".______    _______ .__   __. ____    ____  __  .__   __.   _______  __    __  .___________. __
|   _  \  |   ____||  \ |  | \   \  /   / |  | |  \ |  |  /  _____||  |  |  | |           ||  |
|  |_)  | |  |__   |   \|  |  \   \/   /  |  | |   \|  | |  |  __  |  |  |  | `---|  |----`|  |
|   _  <  |   __|  |  . `  |   \      /   |  | |  . `  | |  | |_ | |  |  |  |     |  |     |  |
|  |_)  | |  |____ |  |\   |    \    /    |  | |  |\   | |  |__| | |  `--'  |     |  |     |__|
|______/  |_______||__| \__|     \__/     |__| |__| \__|  \______|  \______/      |__|     (__)\n""") 
    
        print("𝚂𝚎𝚕𝚎𝚌𝚌𝚒𝚘𝚗𝚊 𝚚𝚞𝚎 𝚟𝚘𝚕𝚜 𝚏𝚎𝚛!")
        vegada += 1    
        
        try:
            opcio = int(input("1- Crea els models.\n2- Visualitza resultats. (Atenció: Abans has de crear els models!)\n\nAltre número implica sortir.\n\n"))
        except:
            print("ERROR: Opció NO vàlida. Tria una opció correcta!")
            opcio = int(input("1- Crea els models.\n2- Visualitza resultats. (Atenció: Abans has de crear els models!)\n\nAltre número implica sortir.\n\n"))
        
        if opcio == 1:
            try: 
                print("\n𝚂𝚎𝚕𝚎𝚌𝚌𝚒𝚘𝚗𝚊 𝚎𝚕𝚜 𝚙𝚊𝚛𝚊𝚖𝚎𝚝𝚛𝚎𝚜 𝚊𝚖𝚋 𝚎𝚕𝚜 𝚚𝚞𝚎 𝚟𝚘𝚕𝚜 𝚝𝚛𝚎𝚋𝚊𝚕𝚕𝚊𝚛!")
            
                t_document = 0; t_representacio = 0; t_distancia = 0; t_model = 0; k = 0; document_query = None;
                
                while t_document == 0:
                    try:
                        t_document = int(input("Document:\n1- Imatge\n2- Text\n\n"))
                    except:
                        print("ERROR: Opció NO vàlida. Tria una opció correcta!")
                        t_document = int(input("Document:\n1- Imatge\n2- Text\n\n"))
                    if t_document == 1: t_document = "imatge"; train = "cifrar"
                    elif t_document == 2: t_document = "text"; train = "newsgroups"
                    else: t_document = 0; print("\nOpció NO vàlida!\n")
                
                while t_representacio == 0:
                    try:
                        t_representacio = int(input("Representació:\n1- Bow\n2- Tf-idf\n\n"))
                    except:
                        print("ERROR: Opció NO vàlida. Tria una opció correcta!")
                        t_representacio = int(input("Representació:\n1- Bow\n2- Tf-idf\n\n"))
                    if t_representacio == 1: t_representacio = "bow"
                    elif t_representacio == 2: t_representacio = "tf-idf"
                    else: t_representacio = 0; print("\nOpció NO vàlida!\n")
                    
                while t_distancia == 0:
                    try:
                        t_distancia = int(input("Distància:\n1- Imatge\n2- Text\n\n"))
                    except:
                        print("ERROR: Opció NO vàlida. Tria una opció correcta!")
                        t_distancia = int(input("Distància:\n1- Imatge\n2- Text\n\n"))
                    if t_distancia == 1: t_document = "imatge"
                    elif t_distancia == 2: t_distancia = "text"
                    else: t_distancia = 0; print("\nOpció NO vàlida!\n")
                    
                while t_model == 0:
                    try:
                        t_model = int(input("Model:\n1- Recuperació\n2- Agrupament\n\n"))
                    except:
                        print("ERROR: Opció NO vàlida. Tria una opció correcta!")
                        t_model = int(input("Model:\n1- Recuperació\n2- Agrupament\n\n"))
                    if t_model == 1: 
                        t_document = "recuperacio"
                        try:
                            document_query = input("\nIntrodueix el document Query: \n")
                        except:
                            print("ERROR: Opció NO vàlida. Tria una opció correcta!")
                            document_query = input("\nIntrodueix el document Query: \n")
                    elif t_model == 2: 
                        t_model = "agrupament"
                        try:
                            k = int(input("\nIntrodueix el número de grups: \n"))
                        except:
                            print("ERROR: Opció NO vàlida. Tria una opció correcta!")
                            k = int(input("\nIntrodueix el número de grups: \n"))
                    else: t_model = 0; print("\nOpció NO vàlida!\n")
                
                self._controlador = Controller(t_document, t_representacio, t_distancia, train)
                self._t_model = t_model 
                self.crea_model(self._database, k, document_query)
                print("\nFi! \n\n--------------------------------------\n")
                return True
            
            except AssertionError as missatge:
                print("\nERROR: ", missatge)
                return True
                
        elif opcio == 2:
            try:
                buscador.visualitza_resultats(nom_database)
                return True
            except AssertionError as missatge:
                print("\nERROR: ", missatge)
                return True
            except AttributeError:
                self._controlador = Controller(None, None, None, None)
                self.visualitza_resultats(self._database)
                return True
        else:
            print("\n𝙵𝚒𝚗𝚜 𝚊𝚟𝚒𝚊𝚝!")
            return False





























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