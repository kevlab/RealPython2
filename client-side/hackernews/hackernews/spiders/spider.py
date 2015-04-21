from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from hackernews.items import HackernewsItem

class MySpider(BaseSpider):
    # name spider
    name = "hackernews"

    allowed_domains = ["news.ycombinator.com/"]
    start_urls = ["https://news.ycombinator.com/"]

    # parse and return scraped data
    # used XPath to parse and extract the data using HTML tags
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select('//td[@class="title"]')  # finds all <td> tags where class="title"
        items = []
        for title in titles:
            item = HackernewsItem()
            item["title"] = title.select("a/text()").extract()
            item["url"] = title.select("a/@href").extract()
            items.append(item)
        return items
