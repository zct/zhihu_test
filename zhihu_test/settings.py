# -*- coding: utf-8 -*-

# Scrapy settings for zhihu_test project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'zhihu_test'

SPIDER_MODULES = ['zhihu_test.spiders']
NEWSPIDER_MODULE = 'zhihu_test.spiders'

ITEM_PIPELINES = {
        'zhihu_test.pipelines.ZhihuTestPipeline': 300,
        }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihu_test (+http://www.yourdomain.com)'
