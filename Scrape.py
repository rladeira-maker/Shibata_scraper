'''Retira os dados de cada "card" existente na página web- identificação
 do produto (product_id), nome do produto (title) e o preço praticado
  (price)'''
from WriteToCsv import write_to_csv


def scrape(source_url, soup):
    fileName = (str(source_url).rpartition('/')[-1]).replace('.html', '').rsplit(sep='?')[0]
    # fileName = 'teste'
    cards = (soup.find_all('div', class_='border-promotion'))
    for card in cards:
        product_bs4_tag = card('p', class_='text-success description center-block text-center visible-xs')
        product_name = product_bs4_tag[0].find_all('a')[0].get('title').strip()
        prices_bs4_tag = card.find_all("div", {"class": "info-price"})
        price_per_kilo = ''
        price_per_litre = ''

        match len(prices_bs4_tag):
            case 0:
                continue
            case 1:
                price_real = prices_bs4_tag[0].get_text().split(' ')[2].replace(',', '.')
                price_full = ''
                price_per_kilo = ''
            case 2:
                price_real = prices_bs4_tag[1].get_text().split(' ')[2].replace(',', '.')
                price_full = prices_bs4_tag[0].get_text().split(' ')[2].replace(',', '.')
                price_per_kilo = ''
            case 3:
                price_real = prices_bs4_tag[2].get_text().split(' ')[2].replace(',', '.')
                price_full = prices_bs4_tag[1].get_text().split(' ')[2].replace(',', '.')
                price_per_kilo = prices_bs4_tag[0].get_text().split(' ')[2].replace(',', '.')
        '''Extrai o peso/volume e calcula o valor do preço por litro ou quilo'''
        splited_title = product_name.split(' ')
        for item in splited_title:
            if not (price_per_kilo) and item.upper().find('KG') > 0 and ((item.upper().split('KG')[0]).replace('.','')).replace(',','').isnumeric():
                weight = float((item.upper().split('KG')[0]).replace(',','.'))
                price = price_real.replace(',','.')
                price_per_kilo = (str(round((float(price)/weight)*1 , 2)))#.replace('.', ',')
            if not (price_per_kilo) and item.upper().find('G') > 0 and ((item.upper().split('G')[0]).replace('.','')).replace(',','').isnumeric():
                weight = float((item.upper().split('G')[0]).replace(',','.'))
                price = price_real.replace(',','.')
                price_per_kilo = (str(round((float(price)/weight)*1000, 2)))#.replace('.', ',')
            if item.upper().find('L') > 0 and ((item.upper().split('L')[0]).replace('.','')).replace(',','').isnumeric():
                volume = float((item.upper().split('L')[0]).replace(',','.'))
                price = price_real.replace(',','.')
                price_per_litre = (str(round((float(price)/volume)*1 , 2)))#.replace('.', ',')
            if item.upper().find('ML') > 0 and ((item.upper().split('ML')[0]).replace('.','')).replace(',','').isnumeric():
                volume = float((item.upper().split('ML')[0]).replace(',','.'))
                price = price_real.replace(',','.')
                price_per_litre = (str(round((float(price)/volume)*1000, 2)))#.replace('.', ',')
        id_tag = card.find_all('button')
        id_number = (id_tag[1].get('id')).split('-')[1]
        list_to_save = [id_number, product_name, price_real, price_full, price_per_kilo, price_per_litre, fileName.upper(),"Shibata"]
        write_to_csv(list_to_save)
        # write_to_csv(list_to_save, fileName)
