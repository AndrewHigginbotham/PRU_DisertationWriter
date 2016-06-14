# -*- coding: utf-8 -*-
import scrapy


class Netn1Spider(scrapy.Spider):
    name = "netn1"
    allowed_domains = ["https://scholar.google.com/scholar?hl=en"]
    start_urls = (
        'http://www.https://scholar.google.com/scholar?hl=en/',
    )

    def parse(self, response):
        pass
