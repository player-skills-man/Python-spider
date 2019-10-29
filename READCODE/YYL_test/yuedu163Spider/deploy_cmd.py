from scrapyd_api import ScrapydAPI

# 1，project部署
import os
# 使用命令行部署到服务器
new_project_name = "yuedu163Spider"
version = "2.0"
target = "100"
os.system("python scrapyd-deploy "+target+" -p "+new_project_name+" --version "+version)


