from scrapyd_api import ScrapydAPI

# 1，project部署
# import os
# # 使用命令行部署到服务器
# new_project_name = "test2"
# version = "1"
# target = "100"
# os.system("python scrapyd-deploy "+target+" -p "+new_project_name+" --version "+version)


# 2，project运行调用
# project_name = "test2"
# spider_name = "cnblog_spider"
# api = ScrapydAPI('http://localhost:6800')
# api.schedule(project_name,spider_name)

# # 3,删除project
api = ScrapydAPI('http://localhost:6800')
project_name = "cnblogSpider"
res = api.delete_project(project=project_name)
if res:
    print(project_name, "删除成功")
else:
    print(project_name, "删除操作出现错误")

