with open("1",encoding="utf-8") as f:
    str = f.readlines()

with open("2","w") as f2:
    for line in str:
        f2.write(line.split(":")[0])
        f2.write("\n")