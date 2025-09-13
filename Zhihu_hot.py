import requests
from bs4 import BeautifulSoup
import json
from flask import Flask, render_template
import sys

def get_zhihu_hot():
    url = "https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50&desktop=true"
    # url = "https://www.zhihu.com/billboard"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Cookie": "_xsrf=q9MBtdKzjZ5vDpZymQncFJtu547XFIXE; _zap=fd91a3bd-183c-425f-a157-3b1935036362; d_c0=VfCT5csV3RqPTjpZkW4tV-hRer7k3NxBHaY=|1754293371; __zse_ck=004_5Db8PCjIlLg0iySN97Gg7tl8Z5brq=tMf6=XNKUvagIj6j=3h12i9ZLtr5JupxtFANyDCa4v1hmft/ISedEo9yiEyr/1nh8sywhF2u1gFmL=Ban/wUKQIwTydDZFcao1-sT7Edh/geeh/+ZIfK6ZiuXLnJIPp4N0Pf8n+jxj6NUt6z6kbLLS1zcqBHkcGWsDeiYsv3NGzHBsdnmXSjLaWoNfa9LtsivjxXOcdddUMfT7Gp+G+AEQV+1Gx1EoZyirO; HMACCOUNT=DDD33DFA167BE2CE; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1755344989,1756991619; q_c1=9eef4811c4f7421b9ccdff840624fb67|1757484724000|1757484724000; z_c0=2|1:0|10:1757484730|4:z_c0|80:MS4xN1A5VUxnQUFBQUFtQUFBQVlBSlZUWVhlcG1ud0E2SThTQ3lUQ1pSYjAzX0dlcElwNE4xdklRPT0=|d2c4365001ff6f3802d54cd5db38747cea4ac1b1db470623f25b954f67d942d7; tst=h; SESSIONID=FDsK62tYBIeIUHIYcno7YLUZCfQvMXkk3TvcAEsC4YH; JOID=Ul4cBU723Sf2cVQeRPC-PJZ09MtVtpZbvkJgZRKxkk2wJxlREgzr6ZhyXR5I3Ueq4JaYINL0jwgYGvJIy0pr8TQ=; osd=W10cB0__3if0cF0dRPK_NZV09spctZZZv0tjZRCwm06wJRhYEQzp6JFxXRxJ1ESq4peRI9L2jgEbGvBJwklr8zU=; BEC=e9bdbc10d489caddf435785a710b7029; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1757558585"
    }
    response = requests.get(url, headers=headers)

    # 保存response.json()为文件
    with open("response1.json", "w", encoding="utf-8") as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=2)

    data = response.json()
    results = []
    for item in data["data"]:
        title = item["target"]["title"]
        hot_value = item["detail_text"]
        qid = item["target"]["id"]
        link = f"https://www.zhihu.com/question/{qid}"
        results.append({"title": title, "link": link, "hot": hot_value})

    return results

print(type(__name__))
sys.exit()


app = Flask(__name__)

@app.route("/")
def index():
    data = get_zhihu_hot()
    return render_template("index.html", topics=data)



if __name__ == "__main__":
    app.run(debug=True)
    