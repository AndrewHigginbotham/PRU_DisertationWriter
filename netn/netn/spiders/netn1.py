# -*- coding: utf-8 -*-
import scrapy


class Netn1Spider(scrapy.Spider):
    name = "netn1"
    allowed_domains = ["https://scholar.google.com"]
    start_urls = (
        'https://scholar.google.com/scholar?hl=en&as_sdt=0,23&q=Net+Neutrality',
    )

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
