# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

from scrapy.conf import settings
from zhihu_test.items import ZhihuTestItem

class ZhihuTestPipeline(object):
    def __init__(self):
        self.zh_user_file =open('./zh_user.txt', 'wb')
        self.filter_company = ['腾讯', '阿里', 'google', 'facebook']

    def process_item(self, item, spider):
        for company_name in self.filter_company:
            if(company_name in json.dumps(dict(item['jobs']), ensure_ascii=False).encode('utf8')):
                self.zh_user_file.write(json.dumps(dict(item), ensure_ascii=False).encode('utf8') + '\n')
                break


        return item

    def spider_closed(self, spider):
        self.zh_user_file.close()
        self.zh_followee_file.close()
        self.zh_follower_file.close()
        self.zh_ask_file.close()
        self.zh_answer_file.close()

