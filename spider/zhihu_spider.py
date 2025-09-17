import requests

def fetch_zhihu_hot():
    url = "https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total"
    headers = {
        "User-Agent": "",
        "cookie": "_xsrf=q9MBtdKzjZ5vDpZymQncFJtu547XFIXE; _zap=fd91a3bd-183c-425f-a157-3b1935036362; d_c0=VfCT5csV3RqPTjpZkW4tV-hRer7k3NxBHaY=|1754293371; HMACCOUNT=DDD33DFA167BE2CE; q_c1=9eef4811c4f7421b9ccdff840624fb67|1757484724000|1757484724000; z_c0=2|1:0|10:1757484730|4:z_c0|80:MS4xN1A5VUxnQUFBQUFtQUFBQVlBSlZUWVhlcG1ud0E2SThTQ3lUQ1pSYjAzX0dlcElwNE4xdklRPT0=|d2c4365001ff6f3802d54cd5db38747cea4ac1b1db470623f25b954f67d942d7; tst=h; __zse_ck=004_YuTgvsiHxle/bjgVFWvS9jhSL4nh23myKQwgmpmlYr5W6ncItdo1uto2rNRE6OeMLZ0n=iuIqEj7dO=qp4tqG7WBJjon5J646d45ESnTtqqgjvHfzz6bgXIvsLzORwKs-RHiC1SB6mp8cCQRsIv8XmZvBdbeeZhHPKwWcIcQZ4F2pPwzw8W48VkhR+r9Qh2yjsH7BNvS84k/Eg6DuKn1aAXh7x6xsKN3vx4oU/lEdOfQO6h4vAUuyGvc1eIV01TZd; BEC=d892da65acb7e34c89a3073e8fa2254f; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1756991619; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1758025581; SESSIONID=GEAMvQ5UkAGHJceiT1T9m6XI8PtfHPIwHGPPtwXerUG; JOID=VlETBEjwxcvRiqQkUfOv27-GAfhLuo-LmPv4HgWciYOYxMBMN56cB7qApipUVnT5L5lxfhMAgxynFQhypAH-wCM=; osd=W1kSBUj9zcrQiqksUPKv1reHAPhGso6KmPbwHwSchIuZxcBBP5-dB7eIpytUW3z4Lpl8dhIBgxGvFAlyqQn_wSM="
    }

    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        data = r.json()

        hot_list = []
        for item in data["data"][:10]:
            hot_list.append({
                "title": item["target"]["title"],
                "url": item["target"]["url"]
            })
        return hot_list
    except Exception as e:
        print("知乎爬虫出错：", e)
        return []

if __name__ == "__main__":
    hot_list = fetch_zhihu_hot()
    
