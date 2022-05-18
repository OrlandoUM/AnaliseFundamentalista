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

os.chdir(r'C:\Users\OMOURA\Desktop\AnaliseFundamentalista')


#saf.returnAllInformation()



# Colocar as infos manualmente

#tr.tratamento()


im.mediaSetor() # Criar funcionalidade de passar como parametro o nº de anos pra pegar a média
im.mediaSubsetor()
im.mediaSegmento()
# Criar a funcionalidade "Acompanhamento" para as ações que já invisto

#plots.plotAll()