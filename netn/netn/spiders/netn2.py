# -*- coding: utf-8 -*-
import scrapy


class Netn2Spider(scrapy.Spider):
    name = "netn2"
    #allowed_domains = ["https://scholar.google.com/scholar?hl=en"]
    start_urls = (
        'https://scholar.google.com/scholar?hl=en&as_sdt=0,23&q=Net+Neutrality',
    )

    def parse(self, response):
        pass
