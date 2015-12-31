# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StockdataItem(scrapy.Item):
	# define the fields for your item here like:
	date = scrapy.Field() #日期
	nav = scrapy.Field() #单位净值(元)
	acc = scrapy.Field() #累计净值(元)
	growth = scrapy.Field() #净值增长率

	def __lt__(self, other):
		return self['date'] < other['date']

