# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from math import sqrt


class MyscraperPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['pk'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['pk'])
            negative = item['fields']['negative']
            positive = item['fields']['positive']

            if positive + negative > 0:
                rating = float(positive) * 100 / (positive + negative)
                wilson = (((float(positive) + 1.9208) / (float(positive) + float(negative)) - 1.96 * sqrt((float(positive) * float(negative)) / (float(positive) + float(negative)) + 0.9604) / (float(positive) + float(negative))) / (1 + 3.8416 / (float(positive) + float(negative)))) * 100
            else:
                rating = 0
                wilson = 0

            item['fields']['rating'] = rating
            item['fields']['wilson'] = wilson
            return item
