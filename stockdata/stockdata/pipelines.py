# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors


class StockdataPipeline(object):
	
	def __init__(self):
		self.dbpool = adbapi.ConnectionPool('MySQLdb',
			db = 'stock',
			user = 'root',
			passwd = '123456',
			cursorclass = MySQLdb.cursors.DictCursor,
			charset = 'utf8',
			use_unicode = False
		)
	
	def process_item(self, item, spider):
		query = self.dbpool.runInteraction(self._conditional_insert, item)
		return item
	
	def _conditional_insert(self, tx, item):
		tx.execute('insert into xhlh(date, nav, acc, growth) values (%s, %s, %s, %s)', (item['date'], item['nav'], item['acc'], item['growth'][:-1]))
