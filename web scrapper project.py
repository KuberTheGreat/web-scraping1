from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

browser = webdriver.Chrome('/Users/kuber/Desktop/whjr projects/python/chromedriver')
browser.get(start_url)

time.sleep(10)

def scrap():
    header = ['proper name', 'distance', 'mass', 'radius']
    star_data = []

    for i in range(0, 40):
        soup = BeautifulSoup(browser.page_source, 'html.parser')

        for table_tag in soup.find_all('table', attrs = ['class', 'wikitable sortable jquery-tablesorter']):
            temp_list = []
            tr_tags = table_tag.find_all('tbody', attr = 'tr')

            for index, tr_tag in enumerate(tr_tags):
                if index == 0:
                    temp_list.append(tr_tag.find_all('td')[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except:
                        temp_list.append(' ')
            star_data.append(temp_list)
    with open('scrapper project.csv', 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(header)
        csvwriter.writerows(star_data)

scrap()
