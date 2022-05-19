# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 02:00:36 2022

@author: orlan

1º Rodar o selenium
2º colocar as infos restantes manualmente
3º Rodar sem o selenium
    
""" 

import os
import seleniumAnaliseFundamentalista as saf
import tratamentoResultado as tr
import infoMercado as im
import plots

os.chdir(r'C:\Users\orlan\Desktop\AnaliseFundamentalista')


saf.returnAllInformation()



# Colocar as infos manualmente

#tr.tratamento()


#im.mediaSetor(de = 2021, ate = 2021)
#im.mediaSubsetor(de = 2021, ate = 2021)
#im.mediaSegmento(de = 2021, ate = 2021)




#plots.plotAll()