from PIL import Image

LIGHT_LEVEL = ('.', ',', ';', '!', 'v', 'l', 'L', 'F', 'E', '$', '#', '@')

im = Image.open('./rocket.jpg')
im = im.convert('L')
(x_size, y_size) = im.size

im_s = im.resize((x_size//5, y_size//10), Image.BICUBIC)
for y in range(im_s.size[1]):
    for x in range(im_s.size[0]):
        grayscale = im_s.getpixel((x,y))
        print(LIGHT_LEVEL[int(grayscale/256*len(LIGHT_LEVEL))], end="")
    print('\n', end="")

