'''Extrai todas as páginas de um segmento (hortfrut, por exemplo) até a
última. Cada página é enviada para scrape.py (soup e url)'''
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from Scrape import scrape
#from Init import init


def browse_and_scrape(seed_url, driver, page_number=1):
    # Fetch the URL - We will be using this to append to images and info routes
    source_url = seed_url
    # driver = init(seed_url)
    if page_number == 1:
        driver.get(seed_url)
        driver.implicitly_wait(2)
        sleep(7)
    # Aqui são acrescentadas novas linhas quando usamos esse programa no Spani   
    # Page_number from the argument gets formatted in the URL & Fetched
    try:
        # Prepare the soup
        soup = BeautifulSoup(driver.page_source, "html.parser")
        print(f"Now Scraping - {source_url}")
        scrape(source_url, soup)
        # Invoke the scrape function
        # Recursively invoke the same function with the increment 
        elem = driver.find_element(By.CSS_SELECTOR, 'span.hidden-xs:nth-child(1)')
        elem.click()
        sleep(3)
        seed_url = driver.current_url
        #print(seed_url)
        if ('page=' + str(page_number)) in seed_url:
            return True
        # This if clause stops the script when it hits an empty page
        # The script exits here
        browse_and_scrape(seed_url, driver, (page_number+1))
        return True
    except NoSuchElementException:
        return True
    except Exception as e:
        return e
