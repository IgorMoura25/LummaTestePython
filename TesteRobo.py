from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def Consultar():
    #opts = Options()
    #opts.set_headless()
    #assert opts.headless
    #browser = Chrome(options=opts)
    browser = Chrome()
    browser.get('http://www2.rio.rj.gov.br/multas/index.asp')

    search_form = browser.find_element_by_name('RBwSyEvVoIvg')
    search_form.send_keys('TES0000')
    search_form.submit()

    results = browser.find_elements_by_class_name('result')
    print(results[0].text)
    browser.close()
    quit()

if(__name__ == "__main__"):
    Consultar()