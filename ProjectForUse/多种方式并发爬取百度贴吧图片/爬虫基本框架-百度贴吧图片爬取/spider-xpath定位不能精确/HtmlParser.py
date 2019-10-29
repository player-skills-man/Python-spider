# html解析器
import re
import urllib.parse
from lxml import etree

# html解析器
class HtmlParser(object):

    def parse(self, page_url, content):
        '''
        用于解析网页内容抽取URL和数据
        :param page_url: 下载页面的URL
        :param content: 下载的网页内容
        :return:返回URL和数据
        '''
        if page_url is None or content is None:
            return
        html = etree.HTML(content.encode("utf-8"))
        new_urls = self._get_new_urls(page_url,html)
        new_data = self._get_new_data(page_url,html)
        return new_urls,new_data


    def _get_new_urls(self, page_url, html_xpath):
        '''
        抽取新的URL集合
        :param page_url: 下载页面的URL
        :param html_xpath:xpath doc
        :return: 返回新的URL集合
        '''
        new_urls = set()

        # 贴吧页面
        links = html_xpath.xpath('//*[@id="frs_list_pager"]//@href')
        links.extend(html_xpath.xpath('//*[@class="thread_list_bottom clearfix"]//@href'))
        print("debug HtmlParser->links=", len(links))
        for new_url in links:
            #拼接成完整网址
            new_full_url = urllib.parse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls
    def _get_new_data(self, page_url, html_xpath):
        '''
        抽取有效数据
        :param page_url:下载页面的URL
        :param html_xpath:
        :return:返回有效数据
        '''
        imgs = html_xpath.xpath('//*[@class="threadlist_pic j_m_pic "]/@bpic')
        print("debug HtmlParser->imgs=", len(imgs))
        return imgs
