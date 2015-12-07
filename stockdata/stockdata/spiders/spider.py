from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from stockdata.items import StockdataItem
class DmozSpider(BaseSpider):
	name = "stock"
	allowed_domains = ["stock.finance.sina.com.cn", "dmoz.org"]
	start_urls = [
		"http://stock.finance.sina.com.cn/fundInfo/view/FundInfo_LSJZ.php?symbol=519156"
		# "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
		# "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
	]
	def parse(self, response):
	
		filename = 'wsn'
		open(filename, 'wb').write(response.body)
	
		hxs = Selector(response)
		sites = hxs.xpath('//div/div/table/tbody/tr')
		items = []
		for site in sites:
			info = site.xpath('./td[@class="f005"]')
			if len(info):
				s = StockdataItem()
				s['date'], s['nav'], s['acc'], s['growth'] = site.xpath('./td/text()').extract()
				items.append(s)
		return items
