# Librerías
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
#import pandas as pd


def main():

    """
    Función principal

    """
# Opciones de navegación
    options =  webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')


    options.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.notifications": 2
    })



    driver_path = 'C:\\Users\\Administrador\\Downloads\\chromedriver.exe'

    driver = webdriver.Chrome(driver_path, chrome_options=options)

    # Iniciarla en la pantalla 2
    driver.set_window_position(2000, 0)
    driver.maximize_window()
    time.sleep(1)

    # Inicializamos el navegador
    driver.get('https://web.telegram.org/z/#6101583730')

    time.sleep(30)



    #driver.quit()


    #escribir email
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#telegram-search-input')))\
        .send_keys('ventas online')

    time.sleep(10)
    try:
        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,
                                            '/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div')))\
            .click()
                        
        time.sleep(10)
    except:
        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,
                                            '/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/div')))\
            .click()
        
        time.sleep(10)


    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[1]/div/div/div/div/div[2]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div/div[1]')))\
        .send_keys(r"https://images.app.goo.gl/H3UxKsuAYMYxVqbu9",Keys.ENTER)
        

    time.sleep(5)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#telegram-search-input')))\
        .send_keys('mi princesa')

    time.sleep(10)
    try:
        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,
                                            '/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div')))\
            .click()
                        
        time.sleep(10)
    except:
        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,
                                            '/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/div')))\
            .click()
                        
        time.sleep(10)

    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[1]/div/div/div/div/div[2]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div/div[1]')))\
        .send_keys(r"https://images.app.goo.gl/H3UxKsuAYMYxVqbu9", Keys.ENTER)

    time.sleep(10)

    driver.quit()


    """/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/div

    #escribir contraseña
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input')))\
        .send_keys('barriga123456')
    time.sleep(5)


    #Iniciar sesion
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'button._42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy'.replace(' ', '.'))))\
        .click()


    time.sleep(5)
    ##Parte 2 Comentario y like 

    #driver.get('https://www.facebook.com/photo.php?fbid=4682923240897&set=pb.1528347242.-2207520000.&type=3')
    driver.get('https://m.facebook.com/story.php?story_fbid=pfbid0AZmHqaFD7URBnpXk8jHjnWvtRMW7YhNUNQTijZHXBohZmXRTa7fDDoGmA8KCMPh3l&id=100055777984144&mibextid=Nif5oz')

    time.sleep(20)
    WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[1]/div/div[4]/div/div[1]/div/div/div/footer/div/div/div[1]/a')))\
        .click()

    #/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]
    time.sleep(5)

    #Comentario
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[1]/div/div[4]/div/div[1]/div/div/div/div[2]/div/div/div[7]/div[2]/form/div[1]/div[2]/div[1]/div/textarea')))\
        .send_keys('esto es un test', Keys.ENTER)
    #/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[1]/div[5]/div/div/div[2]/div[1]/form/div/div/div[1]/div/div[1]/p

    #Enter
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[1]/div/div[4]/div/div[1]/div/div/div/div[2]/div/div/div[7]/div[2]/form/div[1]/div[3]/button')))\
        .click()

    time.sleep(15)



    driver.quit()"""

if __name__ == '__main__':
    main()

