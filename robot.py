from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def cadastrar_web(dataframe):
    # logando no sistema
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('http://automacao.empowerdata.com.br')

    email = browser.find_element(By.XPATH, '//*[@id="email"]')
    email.send_keys('aluno@empowerdata.com.br')

    senha = browser.find_element(By.XPATH, '//*[@id="password"]')
    senha.send_keys('empowerpython')

    time.sleep(0.5)

    botao_logar = browser.find_element(By.XPATH, '//*[@id="submit"]')
    botao_logar.click()

    time.sleep(2)

    # Percorrendo arquivo excel
    for _, linha in dataframe.iterrows():
        cliente_nome = browser.find_element(By.XPATH, '//*[@id="nome"]')
        cliente_nome.send_keys(linha['Nome'])

        cliente_email = browser.find_element(By.XPATH, '//*[@id="email"]')
        cliente_email.send_keys(linha['E-mail'])

        cliente_telefone = browser.find_element(By.XPATH, '//*[@id="telefone"]')
        cliente_telefone.send_keys(linha['Telefone'])

        cliente_cidade = browser.find_element(By.XPATH, '//*[@id="cidade"]')
        cliente_cidade.send_keys(linha['Cidade'])

        cliente_estado = browser.find_element(By.XPATH, '//*[@id="estado"]')
        cliente_estado.send_keys(linha['Estado'])

        time.sleep(0.5)

        botao_cadastrar = browser.find_element(By.XPATH, '//*[@id="submit"]')
        botao_cadastrar.click()

        time.sleep(2)

    browser.close()
