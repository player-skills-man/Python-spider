import gvcode

s, v = gvcode.generate()    #序列解包

s.show()    #显示生成的验证码图片
s.save("vcode.jpg")
print(v)    #打印验证码字符串