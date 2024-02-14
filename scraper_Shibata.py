'''Main file'''
import datetime as dt
from DeleteFile import deleteFile
from Init import init
from departamentos import pages
from BrowseAndScrape import browse_and_scrape


if __name__ == "__main__":
    '''main file - loads pages list and scrape web pages'''
    DIRECTORY = './Shibata'
    DIRECTORY = DIRECTORY + '_' + dt.datetime.now().date().isoformat() + '/'
    try:
        deleteFile(DIRECTORY)
        driver = init('https://www.loja.shibata.com.br')
    except Exception as e:
        print('parece que ocorreu um erro', e)
    for page in pages:
        #SEED_URL = "https://www.loja.shibata.com.br/produtos" + page
        SEED_URL = page
        print("\nWeb scraping has begun")
        result = browse_and_scrape(SEED_URL, driver)
        if result is True:
            pass
        else:
            print(f"Oops, That doesn't seem right!!! - {result}\n")
    if result is True:
        print("Web scraping is now complete!")
    else:
        print(f"Oops, That doesn't seem right!!! - {result}\n")
    driver.close()
    quit()
