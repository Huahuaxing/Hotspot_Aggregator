from collections.abc import Iterable
import scrapy
import json
from weibo_hot.items import WeiboHotItem

class WeiboSpider(scrapy.Spider):
    name = "weibo"
    allowed_domains = ["weibo.com"]
    start_urls = ["https://weibo.com/ajax/side/hotSearch"]

    def start_requests(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
            "Cookie": "XSRF-TOKEN=XSzzsp7gG5P3-4xzj1ZnEfc8; _s_tentry=www.bing.com; Apache=334442842498.65564.1758104916488; SINAGLOBAL=334442842498.65564.1758104916488; ULV=1758104916499:1:1:1:334442842498.65564.1758104916488:; SCF=ArA4bDN4QFwBjFaV1hJZf8XgEP8PvG7y0mI61tRLDVbE1t-aWs0-D4Z6JRsdGhos7HAxVsnvF1tAg7H1VD27C9E.; SUB=_2A25FzsI-DeRhGeFH41UT8SzNyz2IHXVmolv2rDV8PUNbmtANLW7bkW9NeiU3WHjTXkQwqdunAgsW--E3Ck2mprr7; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhTBDlgG9GjPkA6SOX6qg_P5NHD95QN1KnNeo2EeK5pWs4Dqcjyi--Xi-zRiKn7i--fi-zRiKn0i--fiKnpiKLWeK.4e05N; ALF=02_1760706414; WBPSESS=xa97dzQNcEmw4gOut-1LGv5SOI0tpJ6dYQtkASX4gsK2LRu01GRxfEqokk3pccv82zsOmrzC3BgyVvB9n30R2l8Jx04IacL5xeHjZZ3MbP3whgBouUAzTNvREDx3i_Q_MaMkNn_ytrFPCTZGbzOTaw==; UOR=www.bing.com,open.weibo.com,chatgpt.com",
            "Referer": "https://weibo.com/"
        }
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers, callback=self.parse)


    def parse(self, response):
        print(response.text)
        data = json.loads(response.text)
        realtime_list = data.get("data", {}).get("realtime", [])

        for idx, item in enumerate(realtime_list, start=1):
            hot_item = WeiboHotItem()
            hot_item["rank"] = idx
            hot_item["title"] = item.get("word")
            yield hot_item