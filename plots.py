# -*- coding: utf-8 -*-
"""
Created on Mon May  9 20:12:42 2022

@author: omoura

Gerar Consolidado para plots
"""

import pandas as pd
import glob
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import os
import ArquivoProperties as prop


path = os.getcwd() + '\\' + prop.getSetor() + '\\' + prop.getSubsetor() + '\\' + prop.getSegmento()
file_identifier = '*.csv'



# Balanço
def plotBalanco(df):
    fig, axes = plt.subplots(5, 2, figsize = (20,20))
    sns.lineplot(data=df,x='Ano',y='Ativo Circulante',hue='Ticker',ax=axes[0,0])
    sns.lineplot(data=df,x='Ano',y='Ativo Total',hue='Ticker',ax=axes[0,1])
    sns.lineplot(data=df,x='Ano',y='Imobilizado',hue='Ticker',ax=axes[1,0])
    sns.lineplot(data=df,x='Ano',y='Intangível',hue='Ticker',ax=axes[1,1])
    sns.lineplot(data=df,x='Ano',y='Ativo Não Circulante',hue='Ticker',ax=axes[2,0])
    sns.lineplot(data=df,x='Ano',y='Passivo Circulante',hue='Ticker',ax=axes[2,1])
    sns.lineplot(data=df,x='Ano',y='Passivo Não Circulante',hue='Ticker',ax=axes[3,0])
    sns.lineplot(data=df,x='Ano',y='Passivo Total',hue='Ticker',ax=axes[3,1])
    sns.lineplot(data=df,x='Ano',y='Patrimônio Líquido',hue='Ticker',ax=axes[4,0])
    plt.savefig(path + '\\Balanço.pdf')


# DRE
def plotDRE(df):
    fig, axes = plt.subplots(4, 2, figsize = (20,16))
    sns.lineplot(data=df,x='Ano',y='Receita Líquida',hue='Ticker',ax=axes[0,0])
    sns.lineplot(data=df,x='Ano',y='EBITDA',hue='Ticker',ax=axes[0,1])
    sns.lineplot(data=df,x='Ano',y='EBIT',hue='Ticker',ax=axes[1,0])
    sns.lineplot(data=df,x='Ano',y='Lucro Bruto',hue='Ticker',ax=axes[1,1])
    sns.lineplot(data=df,x='Ano',y='Lucro Líquido',hue='Ticker',ax=axes[2,0])
    sns.lineplot(data=df,x='Ano',y='Dívida Bruta',hue='Ticker',ax=axes[2,1])
    sns.lineplot(data=df,x='Ano',y='Dívida Líquida',hue='Ticker',ax=axes[3,0])
    plt.savefig(path + '\\DRE.pdf')


# FC
def plotFC(df):
    fig, axes = plt.subplots(2, figsize = (10,6))
    sns.lineplot(data=df,x='Ano',y='Caixa e Eqv. de Caixa',hue='Ticker',ax=axes[0])
    sns.lineplot(data=df,x='Ano',y='Caixa gerado nas Op',hue='Ticker',ax=axes[1])
    plt.savefig(path + '\\FC.pdf')


# Produtividade
def plotProdutividade(df):
    fig, axes = plt.subplots(2, figsize = (10,6))
    sns.lineplot(data=df,x='Ano',y='CAPEX',hue='Ticker',ax=axes[0])
    sns.lineplot(data=df,x='Ano',y='Capital de Giro',hue='Ticker',ax=axes[1])
    plt.savefig(path + '\\Produtividade.pdf')


# Retorno
def plotRetorno(df):
    fig, axes = plt.subplots(2,2, figsize = (13,10))
    sns.lineplot(data=df,x='Ano',y='ROE',hue='Ticker',ax=axes[0,0])
    sns.lineplot(data=df,x='Ano',y='ROIC',hue='Ticker',ax=axes[0,1])
    sns.lineplot(data=df,x='Ano',y='ROA',hue='Ticker',ax=axes[1,0])
    plt.savefig(path + '\\Retorno.pdf')


# Rentabilidade
def plotRentabilidade(df):
    fig, axes = plt.subplots(2,2, figsize = (13,10))
    sns.lineplot(data=df,x='Ano',y='Margem Bruta',hue='Ticker',ax=axes[0,0])
    sns.lineplot(data=df,x='Ano',y='Margem Líquida',hue='Ticker',ax=axes[0,1])
    sns.lineplot(data=df,x='Ano',y='Margem EBITDA',hue='Ticker',ax=axes[1,0])
    sns.lineplot(data=df,x='Ano',y='Margem EBIT',hue='Ticker',ax=axes[1,1])
    plt.savefig(path + '\\Rentabilidade.pdf')


# Financeiros
def plotFinanceiros(df):
    fig, axes = plt.subplots(4, 2, figsize = (20,16))
    sns.lineplot(data=df,x='Ano',y='Dív Líq / EBITDA',hue='Ticker',ax=axes[0,0])
    sns.lineplot(data=df,x='Ano',y='Dív Líq / PL',hue='Ticker',ax=axes[0,1])
    sns.lineplot(data=df,x='Ano',y='Cobertura de Juros',hue='Ticker',ax=axes[1,0])
    sns.lineplot(data=df,x='Ano',y='Conversão de Caixa',hue='Ticker',ax=axes[1,1])
    sns.lineplot(data=df,x='Ano',y='Liquidez Corrente',hue='Ticker',ax=axes[2,0])
    sns.lineplot(data=df,x='Ano',y='Liquidez Imediata',hue='Ticker',ax=axes[2,1])
    sns.lineplot(data=df,x='Ano',y='Imposto',hue='Ticker',ax=axes[3,0])
    plt.savefig(path + '\\Financeiros.pdf')


# Valuation
def plotValuation(df):
    fig, axes = plt.subplots(5, 2, figsize = (20,20))
    sns.lineplot(data=df,x='Ano',y='P/L',hue='Ticker',ax=axes[0,0])
    sns.lineplot(data=df,x='Ano',y='P/VPA',hue='Ticker',ax=axes[0,1])
    sns.lineplot(data=df,x='Ano',y='LPA',hue='Ticker',ax=axes[1,0])
    sns.lineplot(data=df,x='Ano',y='VPA',hue='Ticker',ax=axes[1,1])
    sns.lineplot(data=df,x='Ano',y='EV / EBITDA',hue='Ticker',ax=axes[2,0])
    sns.lineplot(data=df,x='Ano',y='EV / Receita',hue='Ticker',ax=axes[2,1])
    sns.lineplot(data=df,x='Ano',y='Payout',hue='Ticker',ax=axes[3,0])
    sns.lineplot(data=df,x='Ano',y='DY',hue='Ticker',ax=axes[3,1])
    sns.lineplot(data=df,x='Ano',y='PegRatio',hue='Ticker',ax=axes[4,0])
    plt.savefig(path + '\\Valuation.pdf')


# Crescimento
def plotCrescimento(df):
    fig, axes = plt.subplots(2, figsize = (10,6))
    sns.lineplot(data=df,x='Ano',y='CAGR Receita',hue='Ticker',ax=axes[0])
    sns.lineplot(data=df,x='Ano',y='CAGR Lucros',hue='Ticker',ax=axes[1])
    plt.savefig(path + '\\Crescimento.pdf')
    
def plotOutrasInfos(df):
    fig, axes = plt.subplots(2,2, figsize = (13,10))
    sns.barplot(data=df,x='Tag Along',y='Ticker',ax=axes[0,0])
    sns.barplot(data=df,x='Liquidez',y='Ticker',ax=axes[0,1])
    sns.barplot(data=df,x='Acionistas',y='Ticker',ax=axes[1,0])
    plt.savefig(path + '\\OutrasInfos.pdf')

def plotAll():
    final = pd.DataFrame()
    for f in glob.glob(path + '\\' + file_identifier):
        df = pd.read_csv(f, sep = ';', encoding = 'ISO-8859-1', decimal = ',')
        final = pd.concat([final, df], axis = 0)

    df = final[final['Ano'] < datetime.now().year].reset_index(drop = True)
    
    plotBalanco(df)
    plotDRE(df)
    plotFC(df)
    plotProdutividade(df)
    plotRetorno(df)
    plotRentabilidade(df)
    plotFinanceiros(df)
    plotValuation(df)
    plotCrescimento(df)
    plotOutrasInfos(final[final['Ano'] == datetime.now().year])
    
#if __name__ == '__main__':
    