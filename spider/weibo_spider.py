#引入requests库
import requests
import json
# 获取json文件
def hot_search():
    url = 'https://weibo.com/ajax/side/hotSearch'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
        "Cookie": "XSRF-TOKEN=XSzzsp7gG5P3-4xzj1ZnEfc8; _s_tentry=www.bing.com; UOR=www.bing.com,open.weibo.com,www.bing.com; Apache=334442842498.65564.1758104916488; SINAGLOBAL=334442842498.65564.1758104916488; ULV=1758104916499:1:1:1:334442842498.65564.1758104916488:; PC_TOKEN=c2cb056776; SCF=ArA4bDN4QFwBjFaV1hJZf8XgEP8PvG7y0mI61tRLDVbE1t-aWs0-D4Z6JRsdGhos7HAxVsnvF1tAg7H1VD27C9E.; SUB=_2A25FzsI-DeRhGeFH41UT8SzNyz2IHXVmolv2rDV8PUNbmtANLW7bkW9NeiU3WHjTXkQwqdunAgsW--E3Ck2mprr7; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhTBDlgG9GjPkA6SOX6qg_P5NHD95QN1KnNeo2EeK5pWs4Dqcjyi--Xi-zRiKn7i--fi-zRiKn0i--fiKnpiKLWeK.4e05N; ALF=02_1760706414; WBPSESS=xa97dzQNcEmw4gOut-1LGv5SOI0tpJ6dYQtkASX4gsK2LRu01GRxfEqokk3pccv82zsOmrzC3BgyVvB9n30R2l8Jx04IacL5xeHjZZ3MbP3whgBouUAzTNvREDx3i_Q_MaMkNn_ytrFPCTZGbzOTaw==",
        "Referer": "https://weibo.com/"
    }

    response = requests.get(url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        return None
    else:
        with open("weibo_response.json", "w", encoding="utf-8") as f:
            json.dump(response.json(), f, indent=2, ensure_ascii=False)
    return response.json()['data']

if __name__ == "__main__":
    hot_search()