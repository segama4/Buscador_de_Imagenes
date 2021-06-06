# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

import os

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

class Controller():
    
    def __init__(self, vocabulary_txt, vocabulary_img):
        self._vocabulary_txt = vocabulary_txt
        self._vocabulary_img = vocabulary_img

    def prepare_test_database(self, train):
        self._database = []
        file_list = os.listdir(train)