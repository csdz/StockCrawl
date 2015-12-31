from scrapy.spider import BaseSpider, Request
from scrapy.selector import Selector
from stockdata.items import StockdataItem
class DmozSpider(BaseSpider):
	name = "stock"
	allowed_domains = ["stock.finance.sina.com.cn", "dmoz.org"]
	start_urls = [
		"http://stock.finance.sina.com.cn/fundInfo/api/openapi.php/CaihuiFundInfoService.getNav?symbol=519156&datefrom=&dateto=&page="
	]
	items = []
	page = 1

	def parse(self, response):
		import json
		body = response.body
		if self.data_extract(json.loads(body)):
			self.page += 1
			return Request(url=self.start_urls[0] + str(self.page), callback=self.parse)
		self.post_check()
		return self.items

	def data_extract(self, json_data):
		if json_data['result'] and json_data['result']['data'] and json_data['result']['data']['data'] and len(json_data['result']['data']['data']):
			t_data = json_data['result']['data']['data']
			for d in t_data:
				s = StockdataItem()
				s['date'] = d['fbrq'][:10]
				s['nav'] = d['jjjz']
				s['acc'] = d['ljjz']
				self.items.append(s)
			return True
		return False

	def post_check(self):
		self.items = list(set(self.items)).sort()
