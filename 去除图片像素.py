from PIL import Image

img = Image.open(r"D:\Picture\cao2.jpg")
img = img.convert("RGBA")  # 转换获取信息
pixdata = img.load()

for y in range(img.size[1]):
    for x in range(img.size[0]):
        if sum(pixdata[x, y][:3]) > 105:
            pixdata[x, y] = (0, 0, 0, 0)
img.save(r'D:\Picture\cao_rgba_big.png')
