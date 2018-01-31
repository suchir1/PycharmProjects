import cv2
import matplotlib.pyplot as plt

image_name = "/home/cheesecake/Desktop/chessboard.png"
img = cv2.imread(image_name)
plt.imshow(img)
plt.show()
ret, corners = cv2.findChessboardCorners(img, (8,8))
if ret == True:
    objpoints.append(objp)

    corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
    imgpoints.append(corners2)

        # Draw and display the corners
    img = cv2.drawChessboardCorners(img, (7,6), corners2,ret)
    plt.imshow('img',img)
    plt.show()