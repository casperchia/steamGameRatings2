# -*- coding: utf-8 -*-
import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "mySpider"
    allowed_domains = ["http://store.steampowered.com/"]
    start_urls = (
        'http://www.http://store.steampowered.com//',
    )

    def parse(self, response):
        pass
