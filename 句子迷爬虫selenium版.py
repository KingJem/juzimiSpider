
# !/usr/bin/env python
# encoding: utf-8
"""
@version: v1.0
@author: King
@contact: qqqqivy@gmail.com
@file: sele.py
@time: 2019/4/28 0028 16:44

"""
import pymongo

MONGO_URL = 'localhost'
MONGO_DB = 'test'
MONGO_COLLECTION = 'juzi'



client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def get_content():
    for i in range(1, 76):
        url = "https://www.juzimi.com/length/%E7%9F%AD%E5%8F%A5%E5%AD%90?page={}".format(i)
        browser.get(url)

        html = browser.page_source
        html = etree.HTML(html, etree.HTMLParser())
        juzi_list = html.xpath('//div[@class="view-content"]//div')

        for juzi in juzi_list:
            content = juzi.xpath('./div/div/a[@class = "xlistju"]/text()')

            author = juzi.xpath('./div/div[@class="xqjulistwafo"]/a/text()')

            book = juzi.xpath('./div/div[@class="xqjulistwafo"]/span/a/text()')

            all_content = {
                "content": content,
                "author": author,
                "book": book,
            }
            if not (content == [] and author == [] and book == []):
                save_to_mongo(all_content)
                print(content,author,book)
                print(all_content)


def save_to_mongo(result):
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到MongoDB成功')
    except Exception as e:
        print('存储到MongoDB失败',e)


# 下一页
# next_page = web.find_element_by_class_name("pager-next")
# next_page.click()
if __name__ == '__main__':
    get_content()
