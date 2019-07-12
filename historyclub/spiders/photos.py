import scrapy
from ..items import HistoryclubItem

base_url = "http://historyloversclub.com"
import requests
import os

def request_download(img):
    r = requests.get(img)
    name = os.path.basename(img)
    with open('photos1/' + name, 'wb') as f:
        f.write(r.content)

class PhotosSpider(scrapy.Spider):
    name = "photos"
    start_urls = [
        "http://historyloversclub.com/the-divine-beauty-of-the-unsurpassed-actress-audrey-hepburn-part-i/"
    ]

    def parse_item(self, response):
        img_url = response.xpath("//div[@class='thecontent']//@src").extract_first()
        img = base_url + img_url
        print("download image..." + img)
        request_download(img)

    def parse(self, response):
        img_urls = response.xpath("//div[@class='pagination']//@href")
        for url in img_urls.getall():
            yield scrapy.Request(url, callback=self.parse_item)

