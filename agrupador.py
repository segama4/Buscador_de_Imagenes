# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

import os
import re
import matplotlib.image as image
import matplotlib.pyplot as plt

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

class Agrupador():
    
    def __init__(self, vocabulary_txt, vocabulary_img):
        self._vocabulary_txt = vocabulary_txt
        self._vocabulary_img = vocabulary_img

    def prepare_test_database(self, train):
        self._database = []
        file_list = os.listdir(train)