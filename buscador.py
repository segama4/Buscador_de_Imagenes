# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mÃ²duls                                                          #
#+--------------------------------------------------------------------------+#

from controlador import Controller
import os

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

class Buscador():
    
    def __init__(self, nom_database = "database.pckl"):
        self._database = nom_database
        self._controlador = None
        self._carpeta_train_img = "./cifrar/retrieval/train"
        self._carpeta_train_txt = "./newsgroups/retrieval/train"
        
    def crea_model(self, t_document, t_model, k, document_query):
        if t_model == "recuperacio": 
            self._controlador.realitza_recuperacio(document_query, t_document)
        else:
            self._controlador.realitza_agrupacio(k)
        
        
    def visualitza_resultats(self):
        self._controlador.visualitza_resultats()

    def tria_menu(self, vegada):
        if vegada == 0:    
            print(""".______    _______ .__   __. ____    ____  __  .__   __.   _______  __    __  .___________. __
|   _  \  |   ____||  \ |  | \   \  /   / |  | |  \ |  |  /  _____||  |  |  | |           ||  |
|  |_)  | |  |__   |   \|  |  \   \/   /  |  | |   \|  | |  |  __  |  |  |  | `---|  |----`|  |
|   _  <  |   __|  |  . `  |   \      /   |  | |  . `  | |  | |_ | |  |  |  |     |  |     |  |
|  |_)  | |  |____ |  |\   |    \    /    |  | |  |\   | |  |__| | |  `--'  |     |  |     |__|
|______/  |_______||__| \__|     \__/     |__| |__| \__|  \______|  \______/      |__|     (__)\n""") 
    
        print("\nðððððððððð ððð ðððð ððð!")
        vegada += 1    
        
        try:
            opcio = int(input("1- Crea index.\n2- Visualitza elements. (AtenciÃ³: Abans has de crear els models!)\n\nAltre nÃºmero implica sortir.\n\n"))
        except:
            print("ERROR: OpciÃ³ NO vÃ lida. Tria una opciÃ³ correcta!")
            opcio = int(input("1- Crea els models.\n2- Visualitza resultats. (AtenciÃ³: Abans has de crear els models!)\n\nAltre nÃºmero implica sortir.\n\n"))
        
        if opcio == 1:
            try: 
                print("\n\nðððððððððð ððð ðððððððððð ððð ððð ððð ðððð ððððððððð!")
            
                t_document = 0; t_representacio = 0; t_distancia = 0; t_model = 0; k = 0; document_query = None;
                
                while t_document == 0:
                    try:
                        t_document = int(input("Document:\n1- Imatge\n2- Text\n\n"))
                    except:
                        print("ERROR: OpciÃ³ NO vÃ lida. Tria una opciÃ³ correcta!")
                        t_document = int(input("Document:\n1- Imatge\n2- Text\n\n"))
                    if t_document == 1: t_document = "imatge"; train = self._carpeta_train_img
                    elif t_document == 2: t_document = "text"; train = self._carpeta_train_txt
                    else: t_document = 0; print("\nOpciÃ³ NO vÃ lida!\n")
                
                while t_representacio == 0:
                    try:
                        t_representacio = int(input("RepresentaciÃ³:\n1- Bow\n2- Tf-idf\n\n"))
                    except:
                        print("ERROR: OpciÃ³ NO vÃ lida. Tria una opciÃ³ correcta!")
                        t_representacio = int(input("RepresentaciÃ³:\n1- Bow\n2- Tf-idf\n\n"))
                    if t_representacio == 1: t_representacio = "bow"
                    elif t_representacio == 2: t_representacio = "tf-idf"
                    else: t_representacio = 0; print("\nOpciÃ³ NO vÃ lida!\n")
                    
                while t_distancia == 0:
                    try:
                        t_distancia = int(input("DistÃ ncia:\n1- Cosinus\n2- Interseccio\n\n"))
                    except:
                        print("ERROR: OpciÃ³ NO vÃ lida. Tria una opciÃ³ correcta!")
                        t_distancia = int(input("DistÃ ncia:\n1- Cosinus\n2- Interseccio\n\n"))
                    if t_distancia == 1: t_distancia = "cosinus"
                    elif t_distancia == 2: t_distancia = "interseccio"
                    else: t_distancia = 0; print("\nOpciÃ³ NO vÃ lida!\n")
                    
                self._controlador = Controller(t_document, t_representacio, t_distancia, train)
                self._controlador.crea_index()
                return True
            except:
                print("ERROR: Alguna cosa no ha anat com desitjavem!")
                    
        elif opcio == 2:      
            try: 
                print("\n\nðððððððððð ððð ðððððððððð ððð ððð ððð ðððð ððððððððð!")
            
                t_document = 0; t_representacio = 0; t_distancia = 0; t_model = 0; k = 0; document_query = None;
                
                while t_document == 0:
                    try:
                        t_document = int(input("Document:\n1- Imatge\n2- Text\n\n"))
                    except:
                        print("ERROR: OpciÃ³ NO vÃ lida. Tria una opciÃ³ correcta!")
                        t_document = int(input("Document:\n1- Imatge\n2- Text\n\n"))
                    if t_document == 1: t_document = "imatge"; train = self._carpeta_train_img
                    elif t_document == 2: t_document = "text"; train = self._carpeta_train_txt
                    else: t_document = 0; print("\nOpciÃ³ NO vÃ lida!\n")
                
                while t_representacio == 0:
                    try:
                        t_representacio = int(input("RepresentaciÃ³:\n1- Bow\n2- Tf-idf\n\n"))
                    except:
                        print("ERROR: OpciÃ³ NO vÃ lida. Tria una opciÃ³ correcta!")
                        t_representacio = int(input("RepresentaciÃ³:\n1- Bow\n2- Tf-idf\n\n"))
                    if t_representacio == 1: t_representacio = "bow"
                    elif t_representacio == 2: t_representacio = "tf-idf"
                    else: t_representacio = 0; print("\nOpciÃ³ NO vÃ lida!\n")
                    
                while t_distancia == 0:
                    try:
                        t_distancia = int(input("DistÃ ncia:\n1- Cosinus\n2- Interseccio\n\n"))
                    except:
                        print("ERROR: OpciÃ³ NO vÃ lida. Tria una opciÃ³ correcta!")
                        t_distancia = int(input("DistÃ ncia:\n1- Cosinus\n2- Interseccio\n\n"))
                    if t_distancia == 1: t_distancia = "cosinus"
                    elif t_distancia == 2: t_distancia = "interseccio"
                    else: t_distancia = 0; print("\nOpciÃ³ NO vÃ lida!\n")
                    
                while t_model == 0:
                    try:
                        t_model = int(input("Model:\n1- RecuperaciÃ³\n2- Agrupament\n\n"))
                    except:
                        print("ERROR: OpciÃ³ NO vÃ lida. Tria una opciÃ³ correcta!")
                        t_model = int(input("Model:\n1- RecuperaciÃ³\n2- Agrupament\n\n"))
                    if t_model == 1: 
                        t_model = "recuperacio"
                        while document_query == None:
                            document_query = input("Introdueix el document Query: ")
                            if t_document == "imatge":
                                if document_query not in os.listdir(self._carpeta_train_img):
                                    document_query = None
                                    print("\nERROR: L'arxiu especificat no existeix a la nostra base de dades. Tria una opciÃ³ correcta!")
                                else:
                                    print("\nArxiu correcte!")
                            else: 
                                if document_query not in os.listdir(self._carpeta_train_txt):
                                    document_query = None
                                    print("\nERROR: L'arxiu especificat no existeix a la nostra base de dades. Tria una opciÃ³ correcta!")
                                else:
                                    print("\nArxiu correcte!")
                    elif t_model == 2: 
                        t_model = "agrupament"
                        try:
                            k = int(input("Introdueix el nÃºmero de grups: "))
                        except:
                            print("ERROR: OpciÃ³ NO vÃ lida. Tria una opciÃ³ correcta!")
                            k = int(input("Introdueix el nÃºmero de grups: "))
                    else: t_model = 0; print("\nOpciÃ³ NO vÃ lida!\n")
                
                self._controlador = Controller(t_document, t_representacio, t_distancia, train)
                self.crea_model(t_document, t_model, k, document_query)
                self.visualitza_resultats()
                return True
            
            except AssertionError as missatge:
                print("\nERROR: ", missatge)
                return True

        else:
            print("\nðµððð ððððð!")
            return False