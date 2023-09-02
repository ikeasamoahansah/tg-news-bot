from bs4 import BeautifulSoup
import requests
import csv

class Scrape:

    
    def get_soup(self, link):
        """Returns the html text"""
        response = requests.get(link)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    def find_soup(self, link):
        """Finds the soup using keywords"""
        my_list = []
        soup = self.get_soup(link)
        headings = soup.select('td.title span.titleline a')[0:60:2]
        for title in headings: my_list.append(title.getText().strip())
        return my_list

    def find_soup_url(self, link):
        """Finds the soup urls"""
        my_urls = []
        soup = self.get_soup(link)
        urls = soup.select('td.title span.titleline a')[0:60:2]
        for url in urls: my_urls.append(url.get('href'))
        return my_urls
    
    def zip_soup(self, link):
        linked_list = list(zip(self.find_soup(link), self.find_soup_url(link)))
        return linked_list

    def save_scrape(self, link):
        """Saves the scrapped material as a text file"""
        with open('scrape.txt', 'w', newline='') as file:
            writer = csv.writer(file)
            for data in self.zip_soup(link):
                writer.writerow(data)


