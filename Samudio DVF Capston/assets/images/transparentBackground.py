from PIL import Image

def convertImage():
    img = Image.open("./gapLogo.png")
    img = img.convert("RGBA")

    datas = img.getdata()

    newData = []

    for items in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save("./gapLogo2.png", "PNG")
    print("Successful")



img = Image.open("./gapLogo.png")
img = img.convert("RGBA")

datas = img.getdata()

newData = []

for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("./gapLogo2.png", "PNG")
