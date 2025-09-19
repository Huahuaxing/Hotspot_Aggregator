# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import sqlite3


class WeiboHotPipeline:
    def open_spider(self, spider):
        # 定位Flask项目的instance文件夹
        # base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
        db_path = os.path.join(base_dir, "instance", "database.db")

        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute( 
            """
            CREATE TABLE IF NOT EXISTS weibo_hot(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                hotValue INTEGER
            )
            """
        )
        print("建表成功！")
    
    def process_item(self, item, spider):
        self.cursor.execute("INSERT INTO weibo_hot (title, hotValue) VALUES (?, ?)",
                            (item["title"], item["hotValue"]))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()


if __name__ == "__main__":
    print(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

