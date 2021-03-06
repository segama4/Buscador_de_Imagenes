# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem m貌duls                                                          #
#+--------------------------------------------------------------------------+#

import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

class Visualitzador(ABC):
    
    def __init__(self, resultat):
        self._database = resultat
        
    @abstractmethod
    def visualitza(self):
        raise NotImplementedError
        
        
class Visualitzador_Recuperacio(Visualitzador):
    
    def __init__(self, resultat):
        super().__init__(resultat)
            
    def visualitza(self):
        print("\n -- Visualitzant resultats --")
        
        index = 0
        opcio_2 = 1
        fig, axs = plt.subplots(1,5)
        pos = 0
        for i in range(index*5, (index*5)+5):
            self._database[1][i].visualitza(axs[pos])
            pos += 1
        plt.show()
        
        while opcio_2 in [1,2]:
            print("饾棙饾榾饾棸饾椉饾椆饾椆饾椂饾槀 饾椌饾槀饾椂饾椈饾棶 饾椉饾椊饾棸饾椂饾椉 饾槂饾椉饾椆饾棽饾槀 饾椏饾棽饾棶饾椆饾椂饾榿饾槆饾棶饾椏:\n\
    1 - Visualitzar els 5 documents seg眉ents.\n\
    2 - Visualitzar els 5 documents anteriors.\n\
    Altre n煤m. - Sortir")
        
            try: 
                opcio_2 = int(input("Opci贸: "))
            except:
                print("\nERROR: Opci贸 NO v脿lida. Tria una opci贸 correcta!")
                opcio_2 = int(input("Opci贸: "))
            
            if opcio_2 == 2 and index == 0:
                    while opcio_2 == 2: 
                        print("\nERROR: No hi ha documents anteriors. Tria una opci贸 correcta!")
                        opcio_2 = int(input("Opci贸: "))
            
            if opcio_2 == 1:
                index += 5
            else:
                index -= 5
        
            fig, axs = plt.subplots(1, 5)
            pos = 0
            for i in range(index*5, (index*5)+5): 
                self._database[1][i].visualitza(axs[pos])
                pos += 1 
            plt.show()
    
class Visualitzador_Agrupacio(Visualitzador):
    
    def __init__(self, resultat):
        super().__init__(resultat)
    
    def visualitza_basic(self):
        try: 
            for i in range(len(self._database[1])):
                fig, axs = plt.subplots()
                self._database[1][i][0].visualitza(axs)
                plt.show()
        except:
            print("\nERROR: Model erroni!")
            
    def visualitza_dinamic(self):
        try: 
            opcio = -1
            print("\nTrieu un grup ' 1 -",len(self._database[1]),"': (", len(self._database[1])+1," - Sortir )")
            while opcio < 1 or opcio > len(self._database[1])+1:
                opcio = int(input("Opci贸: "))
                if opcio < 1 or opcio > len(self._database[1])+1:
                    print("\nERROR: Opci贸 NO v脿lida. Tria una opci贸 correcta!") 
                elif opcio != len(self._database[1])+1 and len(self._database[1][opcio-1][1]) == 0: 
                    print("\nNo hi ha documents en aquest grup!")
                    opcio = -1
                
            if opcio > 0 and opcio < len(self._database[1])+1:         
                print("\n -- Visualitzant Grup", opcio, "--")
                #print(self._database[1][opcio][0].file_name)
                index = 0
                opcio_2 = 1
                opcio -= 1
                avancar = True
                if len(self._database[1][opcio][1]) >= 5:
                    fig, axs = plt.subplots(1, 5)
                    pos = 0
                    for i in range(index*5, (index*5)+5):
                        self._database[1][opcio][1][i].visualitza(axs[pos])
                        pos += 1
                    plt.show()
                else:
                    avancar = False
                    fig, axs = plt.subplots(1, len(self._database[1][opcio][1]))
                    pos = 0
                    for i in range(len(self._database[1][opcio][1])):
                        self._database[1][opcio][1][i].visualitza(axs[pos])
                        pos += 1
                    plt.show()
                
                while opcio_2 in [1,2]:
                    print("饾棙饾榾饾棸饾椉饾椆饾椆饾椂饾槀 饾椌饾槀饾椂饾椈饾棶 饾椉饾椊饾棸饾椂饾椉 饾槂饾椉饾椆饾棽饾槀 饾椏饾棽饾棶饾椆饾椂饾榿饾槆饾棶饾椏:\n\
            1 - Visualitzar els 5 documents seg眉ents.\n\
            2 - Visualitzar els 5 documents anteriors.\n\
            Altre n煤m. - Sortir")
                
                    try: 
                        opcio_2 = int(input("Opci贸: "))
                    except:
                        print("\nERROR: Opci贸 NO v脿lida. Tria una opci贸 correcta!")
                        opcio_2 = int(input("Opci贸: "))
                
                    if opcio_2 == 2 and index == 0:
                            while opcio_2 == 2: 
                                print("\nERROR: No hi ha documents anteriors. Tria una opci贸 correcta!")
                                opcio_2 = int(input("Opci贸: "))
                                
                    if opcio_2 == 1 and avancar == False:
                        while opcio_2 == 1: 
                            print("\nERROR: No hi ha documents posteriors. Tria una opci贸 correcta!")
                            opcio_2 = int(input("Opci贸: "))            
    
                    if opcio_2 == 1:
                        
                        index += 5
                        if index+5 > len(self._database[1][opcio][1]):
                            avancar = False  
                            fig, axs = plt.subplots(1, len(self._database[1][opcio][1])-index)
                            pos = 0
                            for i in range(index, len(self._database[1][opcio][1])-index):
                                self._database[1][opcio][1][i].visualitza(axs[pos])
                                pos += 1
                            plt.show()
                        else:
                            fig, axs = plt.subplots(1, 5)
                            pos = 0
                            for i in range(index*5, (index*5)+5):
                                self._database[1][opcio][1][i].visualitza(axs[pos])
                                pos += 1
                            plt.show()
                            
                    elif opcio_2 == 2:
                        index -= 5
                        avancar = True
                        fig, axs = plt.subplots(1, 5)
                        pos = 0
                        for i in range(index*5, (index*5)+5):
                            self._database[1][opcio][1][i].visualitza(axs[pos])
                            pos += 1
                        plt.show()
        except:
            print("\nERROR: Model erroni!")
            
    def escull_opcio(self):
        print("\n| 饾櫛饾殠饾殫饾殶饾殥饾殫饾殣饾殲饾殱饾殰 饾殜饾殨 饾殔饾殥饾殰饾殲饾殜饾殨饾殥饾殱饾殻饾殜饾殟饾殬饾殯! (饾殶饾殠饾殯饾殰饾殥饾殬 饾煾.饾煾.饾煿) |\n")
        print("饾棙饾榾饾棸饾椉饾椆饾椆饾椂饾槀 饾椌饾槀饾椂饾椈饾棶 饾椉饾椊饾棸饾椂饾椉 饾槂饾椉饾椆饾棽饾槀 饾椏饾棽饾棶饾椆饾椂饾榿饾槆饾棶饾椏:\n\
    1 - Visualitza el document m茅s pr貌xim al representant de cada grup.\n\
    2 - Navegar pels els documents d'un grup.\n\
    Altre n煤m. - Sortir")
        try:
            opcio = int(input("Opci贸: "))
        except:
            print("\nERROR: Opci贸 NO v脿lida. Tria una opci贸 correcta!")
            opcio = int(input("Opci贸: "))
        return opcio
    
    def visualitza(self):
        opcio = 1
        while opcio in [1,2]:
            opcio = self.escull_opcio()
            if opcio == 1:
                self.visualitza_basic()
            elif opcio == 2:
                self.visualitza_dinamic()