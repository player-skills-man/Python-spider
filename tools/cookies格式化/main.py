reslist = []

select = input("选择cookie数据格式(默认2):\n1:raw_cookie\n2:header_cookies\n>>")

# 格式化一行数据
def parseLine(line):
    res = "\"" + line.strip() + "\","
    res = res.replace("=", "\":\"")
    reslist.append(res)


if select == "2":
    print("解析header_cookies...OK")
    with open("header_cookies", encoding="utf-8") as f:
        cookies = f.read()
        cookies = cookies.replace("Cookie:"," ")
        lines = cookies.split(";")
        for line in lines:
            parseLine(line)
else:
    print("解析raw_cookies...OK")
    with open("raw_cookies", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                break
            parseLine(line)


with open("output","w",encoding="utf-8") as f2:
    f2.write("\n".join(reslist))