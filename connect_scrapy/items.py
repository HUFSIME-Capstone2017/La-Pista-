# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class connectItem(scrapy.Item):
    SCH_COST = scrapy.Field()
    AIR_INFO = scrapy.Field()
    R_ORIGIN = scrapy.Field()
    DEP_T = scrapy.Field()
    DEP_DATE = scrapy.Field()
    R_DEST = scrapy.Field()
    ARR_T = scrapy.Field()
    ARR_DATE = scrapy.Field()
    L_LO = scrapy.Field()
