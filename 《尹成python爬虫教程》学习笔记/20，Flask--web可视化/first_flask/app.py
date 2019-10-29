# 超级简单，直接运行就OK了
from flask import Flask,render_template

app = Flask(__name__) # flask 初始化


@app.route('/') #网页路由：根目录
def hello_world():
    return 'Hello World!'

@app.route('/re')
def hello_world2():
    return render_template("regex.html")

if __name__ == '__main__':
    app.run()
