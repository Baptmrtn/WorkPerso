# Import scrapy
import scrapy

# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess


class Duo_Scrap(scrapy.Spider):

	name = "Duo_Scrap"

	DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': None,}

	def start_requests(self):
		urls = ["https://www.duolingo.com/learn"]
		for url in urls:
			yield scrapy.FormRequest(url=url,callback=self.parse,formdata={'user': 'Bartou5', 'pass': 'bartuse78'})

	def parse(self,response):
		pass
		"""
		join = {}
		df = []
		for quote in response.css("table._2bk_b"):
			print(quote.css("tbody"))

			#join = {'Desciption' : quote.css("div._3J74XsK > div > p::text").get(),
			#'Price': quote.css("span._16nzq18::text").get()}
			#df.append(join)

		
		
		filename = f"Asos_nike_dataset.txt"
		with open(filename,'w') as f:
			f.write(df)
		self.log(f'Saved file {filename}')
		"""

# Run the Spider

process = CrawlerProcess()
process.crawl(Duo_Scrap)
process.start()