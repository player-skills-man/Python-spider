#encoding=utf-8
from flask import Flask, redirect, request

app = Flask(__name__)


@app.route("/pwd")
def index():
    print(request.remote_addr,request.user_agent)
    return redirect("http://www.baidu.com")


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
