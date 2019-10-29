#coding:utf-8
import codecs

class DataOutput(object):

    def __init__(self):
        self.num = 0 # 计数
        self.datas=[]
    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout=codecs.open('baike-mycrawler-redis.html','w',encoding='utf-8')
        fout.write("<html>")
        fout.write("<head><meta charset='utf-8'/></head>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data['url'])
            fout.write("<td>%s</td>"%data['title'])
            fout.write("<td>%s</td>"%data['summary'])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()

    # 图片存储到文件
    def store_img_data_to_jpg(self,datas):
        if datas is not None:
            f_name = "./imgs/"+str(self.num) +'.jpg'
            with open(f_name, 'wb') as f:
                f.write(datas)
                # print("图片下载成功：",f_name)
            self.num +=1
        else:
            print("图片下载失败")


