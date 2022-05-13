# -*- coding: utf-8 -*-
"""
Created on Tue May 10 23:08:01 2022

@author: orlan

print element.text
print element.tag_name
print element.parent
print element.location
print element.size

"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
import numpy as np
from datetime import datetime
import ArquivoProperties as prop


def getBalançoPatrimonial(driver):
    aux = driver.find_elements_by_css_selector('.btn.btn-show.btn-secondary.waves-effect')[-1]
    actions = ActionChains(driver)
    actions.move_to_element(aux).perform()
    
    time.sleep(1)
    driver.find_elements_by_css_selector('.btn.btn-show.btn-secondary.waves-effect')[-1].click() # botão Ver Mais
    time.sleep(2)
    
    '''valores anuais'''
    #driver.execute_script("window.scrollTo(0, 9480);")
    aux = driver.find_element_by_xpath('//div[@data-balanco-grid]//div[@class="select-wrapper"]/input')
    actions = ActionChains(driver)
    actions.move_to_element(aux).perform()
    
    time.sleep(2)
    driver.find_element_by_xpath('//div[@data-balanco-grid]//div[@class="select-wrapper"]/input').click()
    time.sleep(1)
    driver.find_element_by_xpath('//div[@data-balanco-grid]//div[@class="select-wrapper"]/ul/li[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[contains(text(), 'Balanço Patrimonial')]").click()
    
    '''Informações Contábeis'''
    bp = driver.find_elements_by_class_name('scroll')[2]
    bp = bp.find_element_by_tag_name('table')
    bp = bp.text
    bp = bp.split('\n')
    
    '''Tratamento lista'''
    try:
        while True:
            bp.remove('show_chart')
    except ValueError:
        pass
    
    try:
        while True:
            bp.remove('format_quote')
    except ValueError:
        pass
    
    '''Convert into DataFrame'''
    colunas = bp[0].split()
    bp.remove(bp[0])
    a = np.reshape(bp,(int(len(bp)/len(colunas)),len(colunas)))
    bp = pd.DataFrame(a, columns = colunas)
    
    return(bp)

def getDemonstracaoResultadoExercicio(driver):
    aux = driver.find_element_by_xpath('//div[@data-dre-grid]//div[@class="select-wrapper"]/input')
    actions = ActionChains(driver)
    actions.move_to_element(aux).perform()
    
    #driver.execute_script("window.scrollTo(0, 7480);")
    time.sleep(1)
    driver.find_elements_by_css_selector('.btn.btn-show.btn-secondary.waves-effect')[-3].click() # botão Ver Mais
    time.sleep(2)
    
    '''valores anuais'''
    #driver.execute_script("window.scrollTo(0, 7380);")
    aux = driver.find_element_by_xpath('//div[@data-dre-grid]//div[@class="select-wrapper"]/input')
    actions = ActionChains(driver)
    actions.move_to_element(aux).perform()
    
    time.sleep(2)
    driver.find_element_by_xpath('//div[@data-dre-grid]//div[@class="select-wrapper"]/input').click()
    time.sleep(1)
    driver.find_element_by_xpath('//div[@data-dre-grid]//div[@class="select-wrapper"]/ul/li[3]').click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[contains(text(), 'Resultado')]").click()
    time.sleep(1)
    
    '''Informações Contábeis'''
    dre = driver.find_elements_by_class_name('scroll')[0]
    dre = dre.find_element_by_tag_name('table')
    dre = dre.text
    dre = dre.split('\n')
    
    '''Tratamento lista'''
    try:
        while True:
            dre.remove('show_chart')
    except ValueError:
        pass
    
    try:
        while True:
            dre.remove('format_quote')
    except ValueError:
        pass
    
    try:
        while True:
            dre.remove('2T2021 - 1T2022')
    except ValueError:
        pass
    
    try:
        while True:
            dre.remove('1T2021 - 4T2021')
    except ValueError:
        pass
    
    try:
        while True:
            dre.remove('# ÚLT. 12M')
    except ValueError:
        pass
    
    
    '''Convert into DataFrame'''
    dre[0] = '# Ult.12M ' + dre[0]
    colunas = dre[0].split()
    dre.remove(dre[0])
    a = np.reshape(dre,(int(len(dre)/len(colunas)),len(colunas)))
    dre = pd.DataFrame(a, columns = colunas)
    dre = dre[['#','2021','2020','2019','2018','2017']]
    return(dre)

def getFluxoDeCaixa(driver):
    #driver.execute_script("window.scrollTo(0, 8200);")
    aux = driver.find_elements_by_css_selector('.btn.btn-show.btn-secondary.waves-effect')[-2]
    actions = ActionChains(driver)
    actions.move_to_element(aux).perform()
    
    time.sleep(1)
    driver.find_elements_by_css_selector('.btn.btn-show.btn-secondary.waves-effect')[-2].click() # botão Ver Mais
    time.sleep(2)
    
    '''valores anuais'''
    #driver.execute_script("window.scrollTo(0, 8000);")
    aux = driver.find_element_by_xpath('//div[@data-fluxocaixa-grid]//div[@class="select-wrapper"]/input')
    actions = ActionChains(driver)
    actions.move_to_element(aux).perform()
    
    time.sleep(2)
    driver.find_element_by_xpath('//div[@data-fluxocaixa-grid]//div[@class="select-wrapper"]/input').click()
    time.sleep(1)
    driver.find_element_by_xpath('//div[@data-fluxocaixa-grid]//div[@class="select-wrapper"]/ul/li[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[contains(text(), 'Fluxo de caixa')]").click()
    time.sleep(1)
    
    '''Informações Contábeis'''
    fc = driver.find_elements_by_class_name('scroll')[1]
    fc = fc.find_element_by_tag_name('table')
    fc = fc.text
    fc = fc.split('\n')
    
    '''Tratamento lista'''
    try:
        while True:
            fc.remove('show_chart')
    except ValueError:
        pass
    
    try:
        while True:
            fc.remove('format_quote')
    except ValueError:
        pass
    
    '''Convert into DataFrame'''
    colunas = fc[0].split()
    fc.remove(fc[0])
    a = np.reshape(fc,(int(len(fc)/len(colunas)),len(colunas)))
    fc = pd.DataFrame(a, columns = colunas)
    return(fc)

def getTagAlong(driver):
    tagAlongTipo = driver.find_element_by_xpath('//div[@title="Tipo do ativo"]/strong').text

    tagAlong = driver.find_elements_by_xpath("//span[@class='sub-value legend-tooltip pr-2 d-inline-block']")[0]
    tagAlong = tagAlong.find_element_by_xpath('..').text
    tagAlong = tagAlong.split('\n')
    tagAlong = tagAlong[-1]
    return(tagAlongTipo, tagAlong)
    
def getLiquidez(driver):
    liq = driver.find_elements_by_xpath("//span[@class='sub-value legend-tooltip pr-2 d-inline-block']")[1]
    liq = liq.find_element_by_xpath('..').text
    liq = liq.split('\n')
    liq = liq[-1]
    return(liq)

def getPapeis(driver):
    papeis = driver.find_element_by_xpath("//div[@title='Total de papéis disponíveis para negociação']")
    papeis = papeis.find_element_by_xpath('..')
    papeis = papeis.text
    papeis = papeis.split('\n')
    papeis = papeis[-1]
    return(papeis)

def getListagem(driver):
    listagem = driver.find_element_by_xpath("//div[@title='Segmento de listagem na B3']").text
    listagem = listagem.split('\n')
    listagem = listagem[-1]
    return(listagem)

def getAcionistas(driver):
    acionistas = driver.find_elements_by_xpath("//*[contains(text(), 'Investidores')]")[0]
    acionistas = acionistas.find_element_by_xpath("..").text
    acionistas = acionistas.split('\n')
    acionistas = acionistas[-1]
    return(acionistas)

def getValorDeFirma(driver):
    vf = driver.find_element_by_xpath("//div[@title='Soma do valor de mercado das ações com a dívida líquida dessa empresa']").text
    vf = vf.split('\n')
    vf = vf[-1]
    return(vf)

def returnAllInformation():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # Abrir site
    driver.get(prop.getSite())
    time.sleep(15)

    driver.maximize_window()
    time.sleep(2)

    # Remover propaganda
    driver.find_element_by_class_name('btn-close').click()
    time.sleep(1)

    # LogIn
    driver.find_elements_by_xpath("//*[contains(text(), 'ENTRAR')]")[0].click()
    time.sleep(1)
    driver.find_element_by_id('Email').send_keys(prop.getEmail())
    driver.find_element_by_id('Password').send_keys(prop.getSenha())
    driver.find_element_by_id('btn-login').click()
    time.sleep(5)

    # procurar ativo
    for t in prop.getTickers():
        driver.execute_script("window.scrollTo(0, 0);")
        driver.find_elements_by_xpath("//*[contains(text(), 'search')]")[0].click()
        driver.find_element_by_css_selector('.Typeahead-input.input.tt-input').send_keys(t)
        time.sleep(5)
        driver.find_element_by_css_selector('.Typeahead-suggestion.Typeahead-selectable').click()
        time.sleep(5)
        
        
        
        # Balanço Patrimonial
        bp = getBalançoPatrimonial(driver)
        
        # Fluxo de Caixa
        fc = getFluxoDeCaixa(driver)
        
        # DRE
        dre = getDemonstracaoResultadoExercicio(driver)
        
        
        
        # Tag Along
        tagAlongTipo, tagAlong = getTagAlong(driver)
        
        
        # Liquidez
        liq = getLiquidez(driver)
        
        
        
        # Papéis
        papeis = getPapeis(driver)
        
        # Listagem
        listagem = getListagem(driver)
        
        # Acionistas
        acionistas = getAcionistas(driver)
        
        # Valor de Firma
        vf = getValorDeFirma(driver)
        
        
        final = pd.concat([bp,dre], ignore_index = True)
        final = pd.concat([final,fc], ignore_index = True)
        final = final.set_index('#').T
        final = final.reset_index()
        final.rename(columns={'index':'Ano'}, inplace = True)
        final.loc[datetime.now().year, 'Ano'] = datetime.now().year
        final.loc[datetime.now().year, 'EV'] = vf
        final.loc[datetime.now().year, 'Tag Along'] = tagAlong
        final.loc[datetime.now().year, 'Tag Along Tipo'] = tagAlongTipo
        final.loc[datetime.now().year, 'Liquidez'] = liq
        final.loc[datetime.now().year, 'Papeis'] = papeis
        final.loc[datetime.now().year, 'Listagem'] = listagem
        final.loc[datetime.now().year, 'Acionistas'] = acionistas
        final['Ticker'] = t
        final['Setor'] = prop.getSetor()
        final['Subsetor'] = prop.getSubsetor()
        final['Segmento'] = prop.getSegmento()
        final['DY'] = ''
        final['P/L'] = ''
        final['PegRatio'] = ''
        final['P/VPA'] = ''
        final['VPA'] = ''
        final['LPA'] = ''
        final['CAGR Receita'] = ''
        final['CAGR Lucros'] = ''
        final['Payout'] = ''
        final.to_csv(prop.getSetor()+'/'+prop.getSubsetor()+'/'+prop.getSegmento()+'/'+t+'.csv', decimal = ',', sep = ';', index = False, encoding = 'ISO-8859-1')

    driver.quit()