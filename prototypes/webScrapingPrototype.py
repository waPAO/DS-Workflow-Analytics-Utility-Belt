import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

'''
This web scraping OOP tool will be using the Chrome web driver, please download
and locate the path of the driver to use and access this program.
'''

class WebScrapingEngine:
    def init(self, driver_path, website_url):
        self.driver_path = driver_path
        self.website_url = website_url
        # setup parameters and run management for selenium service
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver_service = Service(executable_path=driver_path)
        driver = webdriver.Chrome(options=options, service=driver_service)
        driver.get(website_url)
        self.content = driver.page_source
        self.soup = BeautifulSoup(self.content)
      
    def find_elements(self, identifier, class_name, tag):
        results = []
        for element in self.soup.findAll(attrs={f'{identifier}: {class_name}'}):
            name = element.find(tag)
            if name not in results:
                results.append(name.text)
    
    def create_csv(results1, results2, name1, name2, file_name):
        series1 = pd.Series(results1, name=name1)
        series2 = pd.Series(results2, name=name2)
        df = pd.DataFrame({name1: series1, name2: series2})
        df.to_csv(file_name, index=False, encoding='utf-8')