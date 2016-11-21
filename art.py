from PIL import Image
import sys

LIGHT_LEVEL = ('.', ',', ';', '!', 'v', 'l', 'L', 'F', 'E', '$', '#', '@')

if len(sys.argv) < 2:
    print('USAGE: python art.py [image path]')
    exit(1)
im = Image.open(sys.argv[1])
im = im.convert('L')
(x_size, y_size) = im.size

if x_size < 100 or y_size < 100:
    print('Size is too small.')
    print('Must each side length is bigger than 100px')
    exit(1)

#result = open('result.txt', 'w')

im_s = im.resize((x_size//5, y_size//10), Image.BICUBIC)
for y in range(im_s.size[1]):
    for x in range(im_s.size[0]):
        grayscale = im_s.getpixel((x,y))
        print(LIGHT_LEVEL[int(grayscale/256*len(LIGHT_LEVEL))], end="")
        #result.write(LIGHT_LEVEL[int(grayscale/256*len(LIGHT_LEVEL))])
    print('\n', end="")
    #result.write('\n')

