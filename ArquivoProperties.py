# -*- coding: utf-8 -*-
"""
Created on Tue May 10 22:01:00 2022

@author: orlan
"""

import configparser as cp

config = cp.RawConfigParser()
config.read('ConfigFile.properties', encoding = 'utf-8')

def getEmail():
    return(config['StatusInvestSecao']['statusInvest.email'])

def getSite():
    return(config['StatusInvestSecao']['statusInvest.site'])

def getSenha():
    return(config['StatusInvestSecao']['statusInvest.senha'])

def getSetor():
    return(config['AcaoSecao']['acao.setor'])

def getSubsetor():
    return(config['AcaoSecao']['acao.subsetor'])

def getSegmento():
    return(config['AcaoSecao']['acao.segmento'])

def getTickers():
    t = config['AcaoSecao']['acao.tickers']
    t = t.split(',')
    return(t)