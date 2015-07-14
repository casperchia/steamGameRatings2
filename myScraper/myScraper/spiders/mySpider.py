# -*- coding: utf-8 -*-
import scrapy
import re
from myScraper.items import GameItem


class MyspiderSpider(scrapy.Spider):
    name = "mySpider"
    allowed_domains = ["store.steampowered.com"]
    start_urls = []
    for x in xrange(0, 400000):
        start_urls.append("http://store.steampowered.com/app/" + str(x) + "/")

    def parse(self, response):
        if len(response.xpath('//*[@id="agecheck_form"]')) > 0:
            m = re.search('app/(\d+)', response.url)
            appid = int(m.group(1))
            request = scrapy.FormRequest(
                "http://store.steampowered.com/agecheck/app/" + str(appid),
                formdata={'ageYear': '1990', 'ageMonth': 'January', 'ageDay': '1'},
                callback=self.parse
            )
            yield request
        else:
            if 'app' in response.url:
                if (len(response.xpath('//div[@class="apphub_AppName"]/text()')) > 0):
                    item = GameItem()
                    m = re.search('app/(\d+)', response.url)
                    item['appid'] = int(m.group(1))
                    item['name'] = response.xpath('//div[@class="apphub_AppName"]/text()').extract()
                    item['positive'] = 0
                    item['negative'] = 0

                    posSelector = response.xpath('//*[@id="ReviewsTab_positive"]/a/span[@class="user_reviews_count"]/text()')
                    if (len(posSelector) > 0):
                        positiveString = posSelector.extract()[0].replace("(", "").replace(")", "").replace(",", "")
                        item['positive'] = int(positiveString)

                    negSelector = response.xpath('//*[@id="ReviewsTab_negative"]/a/span[@class="user_reviews_count"]/text()')
                    if (len(negSelector) > 0):
                        negativeString = negSelector.extract()[0].replace("(", "").replace(")", "").replace(",", "")
                        item['negative'] = int(negativeString)

                    yield item
