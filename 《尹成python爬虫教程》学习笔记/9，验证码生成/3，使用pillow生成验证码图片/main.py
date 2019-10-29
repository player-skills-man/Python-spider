from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def getChar():
    return chr(random.randint(65, 90))


def getColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def getColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


#  *n代表生成几个随机字，与下面生成字符的n对应
width = 60 * 6
height = 60
#  生成图片
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype(font='./Fonts/AdobeFanHeitiStd-Bold.otf',size=36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=getColor())
# 输出文字:
listChar = []
for t in range(6):
    char = getChar()
    listChar.append(char)
    draw.text((60 * t + 10, 10), char, font=font, fill=getColor2())
# 模糊:
# image = image.filter(ImageFilter.BLUR)
image.show()
image.save('code.jpg', 'jpeg') # 保存图片
print(''.join(listChar))
