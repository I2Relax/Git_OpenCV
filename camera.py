import cv2 as cv

# Mo camera
cap = cv.VideoCapture(0)  #So 0 la camera mac dinh cua laptop

# Kiem tra camera co mo duoc khong
if not cap.isOpened():
    print("Can't open camera.")

while True:
    # Doc hinh anh tu camera
    ret, frame = cap.read()

    # Neu khong the doc, thoat khoi vong lap
    if not ret:
        print("Can't read camera.")
        break

    # Hien thi hinh anh
    cv.imshow('Camera_laptop', frame)

    # Thoat khoi vong lap khi an phim 'z'
    if cv.waitKey(1) & 0xFF == ord('z'):
        break

# Giai phong tai nguyen
cap.release()
cv.destroyAllWindows()
