import cv2 as cv
import numpy as np
W=400
#Hàm vẽ hình elip
def my_ellipse(img, angle):
    thickness =2
    line_type =8
    
    cv.ellipse(img,
               (W //2 , W //2),  #tọa độ tâm
               (W //4, W//16),  #bao bởi hộp có size..
               angle,   #goc cua ellipse so voi truc X
               0,
               360,
               (255,0,255),  #color of ellipse
               thickness,  
               line_type)
#Hàm vẽ hình tròn đục
def my_filled_circle(img, center):
    thickness = -1
    line_type = 8
    cv.circle(img,
              center,
              W //32,
              (0,0,255),
              thickness,
              line_type)
#Hàm vẽ hình đa giác
def my_polygon(img):
    line_type =8
    #Tạo các điểm cho đa giác
    ppt = np.array([[W / 4, 7 * W / 8], [3 * W / 4, 7 * W / 8],
                    [3 * W / 4, 13 * W / 16], [11 * W / 16, 13 * W / 16],
                    [19 * W / 32, 3 * W / 8], [3 * W / 4, 3 * W / 8],
                    [3 * W / 4, W / 8], [26 * W / 40, W / 8],
                    [26 * W / 40, W / 4], [22 * W / 40, W / 4],
                    [22 * W / 40, W / 8], [18 * W / 40, W / 8],
                    [18 * W / 40, W / 4], [14 * W / 40, W / 4],
                    [14 * W / 40, W / 8], [W / 4, W / 8],
                    [W / 4, 3 * W / 8], [13 * W / 32, 3 * W / 8],
                    [5 * W / 16, 13 * W / 16], [W / 4, 13 * W / 16]], np.int32)
    ppt= ppt.reshape((-1,1,2))
    cv.fillPoly(img, [ppt], (10,8,203),line_type) #hình đa giác đầy, đỉnh là các điểm trong ppt, màu (255,255,255)
#Hàm vẽ đường thẳng
def my_line(img, start,end):
    thickness = 2
    line_type =8
    cv.line(img,
            start,
            end,
            (0,0,0),
            thickness,
            line_type)    
       
#hai cửa sổ hiển thị 2 ảnh
atom_window = "Drawing 1: Atom"
rook_window = "Drawing 2: Rook"
#Tạo 2 ảnh đen
size = W,W,3
atom_image = np.zeros(size, dtype = np.uint8)
rook_image = np.zeros(size, dtype = np.uint8)
#Vẽ các elip
my_ellipse(atom_image, 90)
my_ellipse(atom_image, 0)
my_ellipse(atom_image, 45)
my_ellipse(atom_image, -45)
#Vẽ tâm tròn đục
my_filled_circle(atom_image, (W//2,W//2))
#Vẽ đa giác
my_polygon(rook_image)
cv.rectangle(rook_image,   #hcn vẽ trên rook_image
             (0, 7*W//8),  #tọa độ 2 đỉnh đối diện
             (W,W),
             (0,255,255), #màu
             -1,
             8)
#Vẽ các đường thẳng
my_line(rook_image, (0, 15 * W // 16), (W, 15 * W // 16))
my_line(rook_image, (W // 4, 7 * W // 8), (W // 4, W))
my_line(rook_image, (W // 2, 7 * W // 8), (W // 2, W))
my_line(rook_image, (3 * W // 4, 7 * W // 8), (3 * W // 4, W))
#In ra màn hình
cv.imshow(atom_window, atom_image) #hiển thị ảnh
cv.moveWindow(atom_window, 0,200)
cv.imshow(rook_window, rook_image)
cv.moveWindow(rook_window,W,200)
cv.waitKey(0)  #chờ đến lúc bấm nút tắt
cv.destroyAllWindows()  #giải phóng bộ nhớ cho các cửa sổ đã tạo
