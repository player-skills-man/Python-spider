from scrapyd_api import ScrapydAPI

# 1，project部署
import os


# 2，project运行调用
# project_name = "test2"
# spider_name = "cnblog_spider"
# api = ScrapydAPI('http://localhost:6801')

api = ScrapydAPI('http://localhost:6801')
print("project : spider")
for project in api.list_projects():
    for spider in api.list_spiders(project):
        print("{} : {}".format(project,spider))
        api.schedule(project,spider) #schedule ->post(url, data=data...)