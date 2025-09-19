from collections.abc import Iterable
import scrapy
import json
import os
from weibo_hot.items import WeiboHotItem

class WeiboSpider(scrapy.Spider):
    name = "weibo"
    allowed_domains = ["weibo.com"]
    start_urls = ["https://weibo.com/ajax/side/hotSearch"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.collected_results = []

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/117.0 Safari/537.36",
        "Referer": "https://weibo.com/",
        "Cookie": "XSRF-TOKEN=XSzzsp7gG5P3-4xzj1ZnEfc8; _s_tentry=www.bing.com; Apache=334442842498.65564.1758104916488; SINAGLOBAL=334442842498.65564.1758104916488; ULV=1758104916499:1:1:1:334442842498.65564.1758104916488:; SCF=ArA4bDN4QFwBjFaV1hJZf8XgEP8PvG7y0mI61tRLDVbE1t-aWs0-D4Z6JRsdGhos7HAxVsnvF1tAg7H1VD27C9E.; SUB=_2A25FzsI-DeRhGeFH41UT8SzNyz2IHXVmolv2rDV8PUNbmtANLW7bkW9NeiU3WHjTXkQwqdunAgsW--E3Ck2mprr7; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhTBDlgG9GjPkA6SOX6qg_P5NHD95QN1KnNeo2EeK5pWs4Dqcjyi--Xi-zRiKn7i--fi-zRiKn0i--fiKnpiKLWeK.4e05N; ALF=02_1760706414; UOR=www.bing.com,open.weibo.com,chatgpt.com; WBPSESS=xa97dzQNcEmw4gOut-1LGv5SOI0tpJ6dYQtkASX4gsK2LRu01GRxfEqokk3pccv82zsOmrzC3BgyVvB9n30R2t2mPWIVBZbKXQbQaNsM-0MqazOfoW8Yv0dA_v66g556ty8z2G4AUt6qsd84zKU42Q=="
    }

    # 使用 DEFAULT_REQUEST_HEADERS 注入请求头，避免覆写 start_requests
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": headers
    }


    def parse(self, response):
        try:
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
            out_path = os.path.join(base_dir, "weibo_hot.json")
            data = json.loads(response.text)
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            realtime_list = data.get("data", {}).get("realtime", [])
            for id, item in enumerate(realtime_list, 1):
                hot_item = WeiboHotItem()
                if item.get("is_ad") == 1 or item.get("topic_ad") == 1:
                    continue
                hot_item["title"] = item.get("word")
                hot_item["hotValue"] = item["num"]
                yield hot_item
        except Exception as e:
            self.logger.error(f"解析失败：{e}，状态码：{response.status}")


    # def closed(self, reason):
    #     try:
    #         base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    #         out_path = os.path.join(base_dir, "weibo_hot.json")
    #         with open(out_path, "w", encoding="utf-8") as f:
    #             json.dump(self.collected_results, f, ensure_ascii=False, indent=2)
    #         self.logger.info(f"已写入 {len(self.collected_results)} 条数据到 {out_path}")
    #     except Exception as e:
    #         self.logger.error(f"写入文件失败：{e}")