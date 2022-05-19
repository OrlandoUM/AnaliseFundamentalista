# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 21:28:12 2022

@author: orlan
"""

import pandas as pd
import re
import numpy as np
import glob
import os
import ArquivoProperties as prop
import math

d = os.getcwd() + '\\' + prop.getSetor() + '\\' + prop.getSubsetor() + '\\' + prop.getSegmento()
file_extension = '*.csv'
cols = ['Ano','Ativo Total - (R$)', 'Ativo Circulante - (R$)', 'Caixa e Equivalentes de Caixa - (R$)',
         'Imobilizado - (R$)', 'Intangível - (R$)', 'Passivo Circulante - (R$)',
         'Passivo Não Circulante - (R$)', 'Patrimônio Líquido Consolidado - (R$)',
         'Receita Líquida - (R$)', 'Lucro Bruto - (R$)', 'EBITDA - (R$)', 'EBIT - (R$)',
         'Resultado Financeiro - (R$)', 'Impostos - (R$)', 'Lucro Líquido - (R$)',
         'Dívida Bruta - (R$)', 'Caixa Gerado nas Operações - (R$)','Ticker','Setor','Subsetor',
         'Segmento','Tag Along','Tag Along Tipo','Liquidez','Papeis','Listagem','Acionistas','EV'
         ,'DY','P/L','PegRatio','P/VPA','VPA','LPA','CAGR Receita','CAGR Lucros','Payout']

def tratamento():

    # importar arquivo
    for t in glob.glob(d + '//' + file_extension):
        
        df = pd.read_csv(t, sep = ';', decimal = ',', encoding = 'ISO-8859-1', usecols = cols)
        
        df.rename(columns = {'Ativo Total - (R$)':'Ativo Total', 'Ativo Circulante - (R$)':'Ativo Circulante'
                             , 'Caixa e Equivalentes de Caixa - (R$)': 'Caixa e Eqv. de Caixa'
                             , 'Imobilizado - (R$)': 'Imobilizado', 'Intangível - (R$)': 'Intangível'
                             , 'Passivo Circulante - (R$)': 'Passivo Circulante'
                             , 'Passivo Não Circulante - (R$)': 'Passivo Não Circulante'
                             , 'Patrimônio Líquido Consolidado - (R$)': 'Patrimônio Líquido'
                             , 'Receita Líquida - (R$)': 'Receita Líquida'
                             , 'Lucro Bruto - (R$)': 'Lucro Bruto', 'EBITDA - (R$)': 'EBITDA', 'EBIT - (R$)': 'EBIT'
                             , 'Resultado Financeiro - (R$)': 'Resultado Financeiro'
                             , 'Impostos - (R$)': 'IR', 'Lucro Líquido - (R$)': 'Lucro Líquido'
                             , 'Dívida Bruta - (R$)': 'Dívida Bruta'
                             , 'Caixa Gerado nas Operações - (R$)': 'Caixa gerado nas Op'}
                  , inplace = True)
        
        
        df = df.replace('-', np.nan)
        
    
        # Formatar os valores
        for c in ['Ativo Total','Ativo Circulante', 'Caixa e Eqv. de Caixa', 'Imobilizado', 'Intangível','Passivo Circulante', 'Passivo Não Circulante','Patrimônio Líquido', 'Caixa gerado nas Op', 'Receita Líquida','EBITDA', 'EBIT', 'Resultado Financeiro', 'IR','Lucro Bruto', 'Lucro Líquido', 'Dívida Bruta']:
            case = [df[c].apply(lambda x: str(x)[-1]) == 'M'
                    , df[c].apply(lambda x: str(x)[-1]) == 'K']
            then = [df[c].apply(lambda x: re.split("[ ]", str(x))[0]).replace('[.]','',regex = True).replace('[,]','.',regex = True).astype(float).round(2) * 1000000
                    , df[c].apply(lambda x: re.split("[ ]", str(x))[0]).replace('[.]','',regex = True).replace('[,]','.',regex = True).astype(float).round(2) * 1000]
            df[c] = np.select(case, then, default = np.nan)
        
        
        ev = df.loc[max(list(df.index)),'EV']
        if isinstance(ev, str):
            if ((ev == '') | (ev == '-') | (ev == '--') | (ev == 'R$') | (ev == 'R$ ') | (ev == 'R$ -') | (ev == 'R$ --')):
                ev = 0
            else:
                ev = re.sub('[ R$.]','', ev)
                ev = int(re.sub('[,]','.', ev))
        else:
            ev = 0
        df.loc[max(list(df.index)),'EV'] = ev
        


        
        listagem = df.loc[max(list(df.index)),'Listagem']
        if isinstance(listagem, str):
            if ((listagem == '') | (listagem == ' ') | (listagem == '-') | (listagem == '--') | (listagem == 'SEGMENTO DE LISTAGEM')):
                listagem = ''
        else:
            listagem = ''
        df.loc[max(list(df.index)),'Listagem'] = listagem
        
        
        
        papeis = df.loc[max(list(df.index)),'Papeis']
        if isinstance(papeis, str):
            if ((papeis == '') | (papeis == ' ') | (papeis == '-') | (papeis == '--')):
                papeis = 0
            else:
                papeis = int(re.sub('[.]','', papeis))
        else:
            papeis = 0
        df.loc[max(list(df.index)),'Papeis'] = papeis
        

        
        tag = df.loc[max(list(df.index)),'Tag Along']
        if isinstance(tag, str):
            if ((tag == '') | (tag == '-') | (tag == '--') | (tag == '%') | (tag == ' %') | (tag == '-%') | (tag == '--%')):
                tag = 0
            else:
                tag = re.sub('[%]','', tag)
                #tag = float(re.sub('[,]','.', tag))
        else:
            tag = 0
        df.loc[max(list(df.index)),'Tag Along'] = tag
        
        
        
        liquidez = df.loc[max(list(df.index)),'Liquidez']
        if isinstance(liquidez, str):
            if ((liquidez == '') | (liquidez == '-') | (liquidez == '--') | (liquidez == 'R$') | (liquidez == 'R$ ') | (liquidez == 'R$ -') | (liquidez == 'R$ --')):
                liquidez = 0
            else:
                liquidez = re.sub('[R$.]','', liquidez)
                liquidez = liquidez.strip()
                #liquidez = float(re.sub('[,]','.', liquidez))
        else:
            liquidez = 0
        df.loc[max(list(df.index)),'Liquidez'] = liquidez
        
        
        
        acionistas = df.loc[max(list(df.index)),'Acionistas']
        if isinstance(acionistas, str):
            if ((acionistas == '') | (acionistas == '-') | (acionistas == '--')):
                acionistas = 0
            else:
                acionistas = int(re.sub('[.]','', acionistas))
        else:
            acionistas = 0
        df.loc[max(list(df.index)),'Acionistas'] = acionistas
            
        
        
        # Criação de Variáveis
        df['Ativo Não Circulante'] = df['Ativo Total'] - df['Ativo Circulante']
        df['Passivo Total'] = df['Ativo Total'] - df['Patrimônio Líquido']
        df['Dívida Líquida'] = df['Dívida Bruta'] - df['Caixa e Eqv. de Caixa']
        
        case = [df['Receita Líquida'] == 0]
        then = [0]
        df['CAPEX'] = np.select(case, then, default = (df['Imobilizado'] + df['Intangível']) / df['Receita Líquida'])
        df['Capital de Giro'] = np.select(case, then, default = (df['Ativo Total'] - df['Passivo Total']) / df['Receita Líquida'])
        df['Margem Bruta'] = np.select(case, then, default = df['Lucro Bruto'] / df['Receita Líquida'])
        df['Margem Líquida'] = np.select(case, then, default = df['Lucro Líquido'] / df['Receita Líquida'])
        df['Margem EBIT'] = np.select(case, then, default = df['EBIT'] / df['Receita Líquida'])
        df['Margem EBITDA'] = np.select(case, then, default = df['EBITDA'] / df['Receita Líquida'])
        
        df['ROE'] = df['Lucro Líquido'] / df['Patrimônio Líquido']
        df['ROIC'] = (df['EBIT'] + df['IR']) / (df['Patrimônio Líquido'] + df['Dívida Bruta'])
        df['ROA'] = df['Lucro Líquido'] / df['Ativo Total']
        
        case = [df['EBITDA'] == 0]
        then = [0]
        df['Dív Líq / EBITDA'] = np.select(case, then, default = df['Dívida Líquida'] / df['EBITDA'])
        df['Conversão de Caixa'] = np.select(case, then, default = df['Caixa gerado nas Op'] / df['EBITDA'])
        df['EV / EBITDA'] = np.select(case, then, default = ev / df['EBITDA'])
        
        df['Dív Líq / PL'] = df['Dívida Líquida'] / df['Patrimônio Líquido']
        df['Cobertura de Juros'] = df['EBITDA'] / abs(df['Resultado Financeiro'])
        df['Liquidez Corrente'] = df['Ativo Circulante'] / df['Passivo Circulante']
        df['Liquidez Imediata'] = df['Caixa e Eqv. de Caixa'] / df['Passivo Circulante']
        df['Imposto'] = df['IR'] / df['EBIT']
        df['LPA'] = papeis / df['Lucro Líquido']
        df['VPA'] = df['Patrimônio Líquido'] / papeis
        df['EV / Receita'] = ev / df['Receita Líquida']
        
        
        
        df.to_csv(d + '/' + t[-9:], sep = ';', decimal = ',', index = False, encoding = 'latin-1')
        

    