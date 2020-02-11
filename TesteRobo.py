from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def consultar():
    #opts = Options()
    #opts.set_headless()
    #assert opts.headless
    #browser = Chrome(options=opts)
    driver = Chrome()
    driver.get('http://www2.rio.rj.gov.br/multas/index.asp')

    form = driver.find_element_by_name('formulario')
    inputHtml = form.find_element_by_xpath('//tbody[1]/tr[1]/td[2]/input')
    inputHtml.send_keys("TES0000")

    imageHtml = form.find_element_by_tag_name('img').screenshot_as_png

    with open("img/screenshotTESTE.png", "wb") as file:
        file.write(imageHtml)
    
    #driver.close()
    #quit()

if(__name__ == "__main__"):
    consultar()