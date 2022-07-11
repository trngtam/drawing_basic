import cv2

link = 'C:/Users/tran ngoc tam/Desktop/python/opencv.py/lena.JPG'
image = cv2.imread(link,0)
new_w = int(image.shape[1]/10)
new_h = int(image.shape[0]/10)
image = cv2.resize(image,(new_w, new_h))
charmap = " .,:;ox%#@"

with open("ngoctam.txt", 'w', encoding ='utf-8') as f:
    for i, row in enumerate(image):
        for j, col in enumerate(row):
            c = int((255-col)*10/256)
            f.write(charmap[c])
            print(charmap[c], end='')
        print(charmap[c], end='')
        print('\n', end='')
        f.write('\n')
    f.close()   

