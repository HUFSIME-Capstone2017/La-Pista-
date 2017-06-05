import scrapy
from selenium import webdriver
import time
from scrapy.selector import Selector
from basic.yeji import yj

from connect_scrapy.items import connectItem

class DohopSpider(scrapy.Spider):
    name = "do"
    allowed_domains = ["flighthub.com"]
    start_urls = [yj]
    def __init__(self):
        scrapy.Spider.__init__(self)
        self.browser = webdriver.Chrome("/Users/choi/chromedriver")

    def parse(self, response):
        self.browser.get(response.url)
        time.sleep(15)

        html = self.browser.find_element_by_xpath('//*').get_attribute('outerHTML')
        selector = Selector(text=html)
        rows = selector.xpath('//*[@id="fares-search-package-list"]/ul/li')

        for row in rows:
            item = connectItem()
            item["SCH_COST"] = row.xpath('./div[1]/div[1]/div[1]/div[1]/span[2]/text()')[0].extract()
            item["AIR_INFO"] = row.xpath('./div[2]/ul/li/ul/li/div[1]/div[2]/div/text()')[0].extract()
            item["R_ORIGIN"] = row.xpath('./div[2]/ul/li/ul/li/div[2]/div[1]/span[2]/text()')[0].extract()
            item["DEP_T"] = row.xpath('./div[2]/ul/li/ul/li/div[2]/div[1]/strong/text()')[0].extract()
            item["DEP_DATE"] = row.xpath('./div[2]/ul/li/ul/li/div[2]/div[1]/span[1]/text()')[0].extract()
            item["R_DEST"] = row.xpath('./div[2]/ul/li/ul/li/div[2]/div[3]/span[2]/text()')[0].extract()
            item["ARR_T"] = row.xpath('./div[2]/ul/li/ul/li/div[2]/div[3]/strong/text()')[0].extract()
            item["ARR_DATE"] = row.xpath('./div[2]/ul/li/ul/li/div[2]/div[3]/span[1]/text()')[0].extract()
            item["L_LO"] = row.xpath('./div[2]/ul/li/ul/li/div[2]/div[4]/text()')[0].extract()
            yield item