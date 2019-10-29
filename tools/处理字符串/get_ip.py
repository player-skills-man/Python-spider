import re

def make_line(line):
    try:
        url = re.findall(r'<A HREF=(.+)? ADD_DATE',line)[0]
        name = re.findall(r'ADD_DATE="\d+.+>(.+)?</A>',line)[0]
        new_line = url + ", # " + name
        return new_line
    except:
        print(line)
        return ""

lines = ["2019-10-04,yyl免费代理网站总结:",]
with open("免费代理网站总结.xml",encoding="utf-8") as f:
    while True:
        line = f.readline()
        if not line:
            break
        lines.append(make_line(line))

with open("free_ip_webs.txt","w") as f2:
    f2.write("\n".join(lines))