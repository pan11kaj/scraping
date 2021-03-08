from selenium import webdriver;
from bs4 import BeautifulSoup;
import csv,time;
url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome("chromedriver")
browser.get(url)
time.sleep(10)
def scrape():
    headers = ["name","distance","mass","radius"]
    planet_data = []
    for i in range(0,500):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for th_tag in soup.find_all("th",attrs={"class":"headerSort"}):
            tr_tags = th_tag.find_all("tr")
            temp_list = []
            for index,tr_tag in enumerate(tr_tags):
                if index ==0:
                    temp_list.append(tr_tags.find_all("td"))
                else:
                    try:
                        temp_list.append(tr_tags.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table/thead/tr/th[2]').click()
    with open("scrapper_to.csv",'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)

scrape()