from selenium import webdriver
from tickers.ticker import ticker
from xpaths.xpath import xpath


fiis = []
fiis.append(ticker('HCTR11','FII'))
fiis.append(ticker('MFII11','FII'))
fiis.append(ticker('BARI11','FII'))
fiis.append(ticker('HABT11','FII'))
fiis.append(ticker('IRDM11','FII'))
fiis.append(ticker('TORD11','FII'))
fiis.append(ticker('BTLG11','FII'))
fiis.append(ticker('CPTS11','FII'))
fiis.append(ticker('DEVA11','FII'))
fiis.append(ticker('URPR11','FII'))
fiis.append(ticker('CVBI11','FII'))
fiis.append(ticker('XPLG11','FII'))
fiis.append(ticker('MXRF11','FII'))
fiis.append(ticker('BRCO11','FII'))
fiis.append(ticker('BBPO11','FII'))
fiis.append(ticker('BCFF11','FII'))
fiis.append(ticker('HSML11','FII'))
fiis.append(ticker('RBRF11','FII'))
fiis.append(ticker('RBRR11','FII'))
fiis.append(ticker('SARE11','FII'))
fiis.append(ticker('RZAT11','FII'))
fiis.append(ticker('XPCI11','FII'))


xpaths_fiis = []
xpaths_fiis.append(xpath('P/VP','//*[@id="cards-ticker"]/div[3]/div[2]/span'))
xpaths_fiis.append(xpath('Razão Social','//*[@id="table-indicators"]/div[1]/div[2]/div/span'))
xpaths_fiis.append(xpath('CNPJ','//*[@id="table-indicators"]/div[2]/div[2]/div/span'))
xpaths_fiis.append(xpath('PÚBLICO-ALVO','//*[@id="table-indicators"]/div[3]/div[2]/div/span'))
xpaths_fiis.append(xpath('MANDATO','//*[@id="table-indicators"]/div[4]/div[2]/div/span'))
xpaths_fiis.append(xpath('SEGMENTO','//*[@id="table-indicators"]/div[5]/div[2]/div/span'))
xpaths_fiis.append(xpath('TIPO DE FUNDO','//*[@id="table-indicators"]/div[6]/div[2]/div/span'))
xpaths_fiis.append(xpath('PRAZO DE DURAÇÃO','//*[@id="table-indicators"]/div[7]/div[2]/div/span'))
xpaths_fiis.append(xpath('TIPO DE GESTÃO','//*[@id="table-indicators"]/div[8]/div[2]/div/span'))
xpaths_fiis.append(xpath('TAXA DE ADMINISTRAÇÃO','//*[@id="table-indicators"]/div[9]/div[2]/div/span'))
xpaths_fiis.append(xpath('VACÂNCIA','//*[@id="table-indicators"]/div[10]/div[2]/div/span'))
xpaths_fiis.append(xpath('NUMERO DE COTISTAS','//*[@id="table-indicators"]/div[11]/div[2]/div/span'))
xpaths_fiis.append(xpath('COTAS EMITIDAS','//*[@id="table-indicators"]/div[12]/div[2]/div/span'))
xpaths_fiis.append(xpath('VAL. PATRIMONIAL P/ COTA','//*[@id="table-indicators"]/div[13]/div[2]/div/span'))
xpaths_fiis.append(xpath('VALOR PATRIMONIAL','//*[@id="table-indicators"]/div[14]/div[2]/div/span'))
xpaths_fiis.append(xpath('ÚLTIMO RENDIMENTO','//*[@id="table-indicators"]/div[15]/div[2]/div/span'))


driver = webdriver.Chrome()
for ticker in fiis:
    print(ticker.name)

    driver.get("https://investidor10.com.br/" + ticker.type.lower() + "s/" + ticker.name)

    for xpath in xpaths_fiis:
        print(xpath.label + ": " + driver.find_element("xpath", xpath.path).text)

    print("---")