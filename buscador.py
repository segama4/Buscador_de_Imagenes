# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
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
        self._carpeta_train_txt = "./newsgroup/retrieval/train"
        
    def crea_model(self, nom_database, k, document_query):
        try: 
            opcio = input("Vols actualitzar l'index? (S/N) ")
            if opcio not in "SsNn":
                raise AssertionError("Opció no vàlida.")
        except:
            opcio = input("Vols actualitzar l'index? (S/N) ")
            
        if opcio in "Ss": 
            self._controlador.prepara_index()
        else:
            if self._t_model == "recuperacio":
                self._controlador.realitza_recuperacio(nom_database, document_query)
            else:
                self._controlador.realitza_agrupacio(nom_database, k)
        
    def visualitza_resultats(self, nom_database):
        self._controlador.visualitza_resultats(nom_database)

    def tria_menu(self, vegada):
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
                    if t_document == 1: t_document = "imatge"; train = self._carpeta_train_img
                    elif t_document == 2: t_document = "text"; train = self._carpeta_train_txt
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
                        t_distancia = int(input("Distància:\n1- Cosinus\n2- Interseccio\n\n"))
                    except:
                        print("ERROR: Opció NO vàlida. Tria una opció correcta!")
                        t_distancia = int(input("Distància:\n1- Cosinus\n2- Interseccio\n\n"))
                    if t_distancia == 1: t_document = "cosinus"
                    elif t_distancia == 2: t_distancia = "interseccio"
                    else: t_distancia = 0; print("\nOpció NO vàlida!\n")
                    
                while t_model == 0:
                    try:
                        t_model = int(input("Model:\n1- Recuperació\n2- Agrupament\n\n"))
                    except:
                        print("ERROR: Opció NO vàlida. Tria una opció correcta!")
                        t_model = int(input("Model:\n1- Recuperació\n2- Agrupament\n\n"))
                    if t_model == 1: 
                        t_model = "recuperacio"
                        try:
                            document_query = input("Introdueix el document Query: \n")
                            if t_document == "imatge":
                                if document_query not in os.listdir(self._carpeta_train_img):
                                    raise AssertionError 
                            else: 
                                if document_query not in os.listdir(self._carpeta_train_txt):
                                    raise AssertionError 
                        except AssertionError:
                            print("ERROR: L'arxiu especificat no existeeix a la nostra base de dades. Tria una opció correcta!")
                            document_query = input("\nIntrodueix el document Query: \n")
                        except:
                            print("ERROR: Opció NO vàlida. Tria una opció correcta!")
                            document_query = input("\nIntrodueix el document Query: ")
                    elif t_model == 2: 
                        t_model = "agrupament"
                        try:
                            k = int(input("\nIntrodueix el número de grups: \n"))
                        except:
                            print("ERROR: Opció NO vàlida. Tria una opció correcta!")
                            k = int(input("\nIntrodueix el número de grups: \n"))
                    else: t_model = 0; print("\nOpció NO vàlida!\n")
                
                self._controlador = Controller(t_document, t_representacio, t_distancia, train)
                self.crea_model(self._database, k, document_query)
                print("\nFi! \n\n--------------------------------------\n")
                return True
            
            except AssertionError as missatge:
                print("\nERROR: ", missatge)
                return True
                
        elif opcio == 2:
            if self._controlador == None:
                self._controlador = Controller(None, None, None, None)
                self.visualitza_resultats(self._database)
                return True
            else:
                self.visualitza_resultats(self._database)
                return True
        else:
            print("\n𝙵𝚒𝚗𝚜 𝚊𝚟𝚒𝚊𝚝!")
            return False