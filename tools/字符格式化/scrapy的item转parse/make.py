# item[''] = response.xpath('').extract()[0]
def makeline(str):
    strs = str.split("=")
    item_name = strs[0].strip() # item 字段名

    strs2 = strs[1].split("#")
    comment = strs2[1].strip() # 注释
    new_line = "item['"+item_name+"'] = response.xpath('your_xpath').get() # "+comment
    return new_line


lines = ["item = your_Item()\n",]
with open("input",encoding="utf-8") as f:
    while True:
        line = f.readline()
        if not line:
            break
        # makeline(line)
        lines.append(makeline(line))


with open("output","w") as f2:
    f2.write("\n".join(lines))