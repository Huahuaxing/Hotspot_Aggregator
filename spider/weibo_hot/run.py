import os
from scrapy import cmdline

os.chdir("./spider/weibo_hot")
cmdline.execute("scrapy crawl weibo".split())