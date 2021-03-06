# -*- coding: utf-8 -*-
"""
Created on Wed May 11 20:29:22 2022

@author: orlan

ROE
ROIC
ROA
EV / EBITDA
EV / Receita
P/L
P/VPA

"""

import os
import ArquivoProperties as prop
import pandas as pd
import glob
from datetime import datetime
import os.path


path_segm = os.getcwd() + '\\' + prop.getSetor() + '\\' + prop.getSubsetor() + '\\' + prop.getSegmento()
path_subsetor = os.getcwd() + '\\' + prop.getSetor() + '\\' + prop.getSubsetor()
path_setor = os.getcwd() + '\\' + prop.getSetor()

file_identifier = '*.csv'


def mediaSegmento(de, ate):
    final = pd.DataFrame()
    for f in glob.glob(path_segm + '\\' + file_identifier):
        df = pd.read_csv(f, sep = ';', encoding = 'ISO-8859-1', decimal = ',')
        final = pd.concat([final, df], axis = 0)
    
    df = final[(final['Ano'] >= de) & (final['Ano'] <= ate)].reset_index(drop = True)
    df = df[['ROE','ROIC','ROA','EV / EBITDA','EV / Receita','P/L','P/VPA','Margem Líquida','Margem EBITDA','Dív Líq / EBITDA']]
    
    print('-----------------------------------\n- Média Segmento de {0} ate {1}:'.format(de, ate))
    
    for c in df.columns.values:
        print('- {0}: {1}'.format(c, round(df[c].mean(),2)))
        
def mediaSubsetor(de, ate):
    final = pd.DataFrame()
    
    for dirpath, dirnames, filenames in os.walk(path_subsetor):
        for i in dirnames:
            for f in glob.glob(dirpath + '\\' + i + '\\' + file_identifier):
                df = pd.read_csv(f, sep = ';', encoding = 'ISO-8859-1', decimal = ',')
                final = pd.concat([final, df], axis = 0)
            
        
    df = final[(final['Ano'] >= de) & (final['Ano'] <= ate)].reset_index(drop = True)
    df = df[['ROE','ROIC','ROA','EV / EBITDA','EV / Receita','P/L','P/VPA','Margem Líquida','Margem EBITDA','Dív Líq / EBITDA']]
    
    print('-----------------------------------\n- Média Subsetor de {0} até {1}:'.format(de, ate))
    
    for c in df.columns.values:
        print('- {0}: {1}'.format(c, round(df[c].mean(),2)))
    
def mediaSetor(de, ate):
    final = pd.DataFrame()
    
    for dirpath, dirnames, filenames in os.walk(path_setor):
        for i in dirnames:
            for f in glob.glob(dirpath + '\\' + i + '\\' + file_identifier):
                df = pd.read_csv(f, sep = ';', encoding = 'ISO-8859-1', decimal = ',')
                final = pd.concat([final, df], axis = 0)
            
        
    df = final[(final['Ano'] >= de) & (final['Ano'] <= ate)].reset_index(drop = True)
    df = df[['ROE','ROIC','ROA','EV / EBITDA','EV / Receita','P/L','P/VPA','Margem Líquida','Margem EBITDA','Dív Líq / EBITDA']]
    
    print('-----------------------------------\n- Média Setor de {0} até {1}:'.format(de, ate))
    
    for c in df.columns.values:
        print('- {0}: {1}'.format(c, round(df[c].mean(),2)))
        
    
#if __name__ == '__main__':
    