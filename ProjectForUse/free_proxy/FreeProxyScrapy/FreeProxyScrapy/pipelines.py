# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import requests
from scrapy.log import logger

# 检验代理
def vilidate(protocol, ip, port, TIMEOUT=5):
    # logger.info("开始检验:"+protocol+"//"+"ip"+":"+port)
    try:
        if protocol.upper() == "HTTP":
            proxies = {
                "http": "http://" + ip + ":" + port
            }
            requests.get("http://www.baidu.com", proxies=proxies, timeout=TIMEOUT)
            logger.info("存储:"+protocol+"//"+ip+":"+port)
            return True
        elif protocol.upper() == "HTTPS":
            proxies = {
                "https": "https://" + ip + ":" + port
            }
            requests.get("https://www.baidu.com", proxies=proxies, timeout=TIMEOUT)
            logger.info("存储:"+protocol+"//"+ip+":"+port)
            return True
        else:
            logger.info("not HTTP or HTTPS")
            return False
    except:
        logger.info("丢弃:" + ip)
        return False


# 过滤性管道---丢弃数据
class BlockGamePipeline(object):
    def process_item(self, item, spider):
        # 检验代理
        if not vilidate(protocol=item['protocol'],ip=item['ip'],port=item['port']):
            raise DropItem()
        else:
            return item

class FreeproxyscrapyPipeline(object):
    def process_item(self, item, spider):
        return item
