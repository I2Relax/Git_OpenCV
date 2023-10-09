import cv2 as cv
import numpy as np

# Duong dan den hinh anh muon hien thi
image_path = "soc.jpg"

# Doc anh tu duong dan
image = cv.imread(image_path)

# Kiem tra xem doc duoc anh hay khong
if image is None:
    print("Can't read.")
else:
    # Hien thi hinh anh trong mot cua so
    cv.imshow("Image", image)

    #Hien thi kich thuoc anh
    (h, w, d) = image.shape
    print("width={}, height={}, depth={}".format(w, h, d))

    #Lay gia tri mau tai diem [60,90]
    (B, G, R) = image[60, 90]
    print("R={}, G={}, B={}".format(R, G, B))

    #Cat anh tu toa do tren cung ben trai [a,b] den  toa do duoi cung ben phai [c,d]
    #image[a:c, b:d]
    tr = image[50:460, 100:470]
    cv.imshow('The rest', tr)

    # Cho nguoi dung nhan phim bat ky de dong cua so
    cv.waitKey(0)

    # Dong tat ca cua so OpenCV
    cv.destroyAllWindows()