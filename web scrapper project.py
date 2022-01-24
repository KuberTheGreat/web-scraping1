from matplotlib.pyplot import table
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests

start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

browser = webdriver.Chrome('/Users/kuber/Desktop/whjr projects/python/chromedriver')
browser.get(start_url)

time.sleep(10)

header = ['proper_name', 'distance', 'mass', 'radius']
star_data = []
new_star_data = []
final_star_data = []

def scrape():
    for i in range(0, 40):
        soup = BeautifulSoup(browser.page_source, 'html.parser')

        for table_tag in soup.find_all('table'):
            temp_list = []
            tr_tags = table_tag.find_all('tbody')

            for index, tr_tag in enumerate(tr_tags):
                if index == 0:
                    temp_list.append(tr_tag.find_all('tr')[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except:
                        temp_list.append(' ')
            
            star_data.append(temp_list)

def scrape_more_data():
    url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    star_table = soup.find_all('table')
    for index in star_table:
        table_rows = index.find_all('tr')
        temp_list = []

        for td_tag in table_rows:
            try:
                temp_list.append(td_tag[0].contents[0])
            except:
                temp_list.append(' ')
        new_star_data.append(temp_list)

scrape()
scrape_more_data()

for index, data in enumerate(star_data):
    final_star_data.append(data + final_star_data[index])

with open('more scrapper project.csv', 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)
    csv_writer.writerows(final_star_data)