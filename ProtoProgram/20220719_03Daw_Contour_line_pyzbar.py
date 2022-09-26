import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread("recive20220708a.jpg")                       # 開啟圖片
# print(decode(img))                                            # 進行解碼
gray_img = cv2.cvtColor(img,0)
barcode = decode(gray_img)
# print(barcode)

for qrcode in barcode:
    points = qrcode.polygon # 找到QRcode給的4個點
    # print(points)
    pts = np.array(points, np.int32)  # 透過np轉換qrcode.polygon的標點讓電腦可讀
    # print(pts)
    pts = pts.reshape((-1, 1, 2)) # 調整為三維轉換時不確定該維度要具有多少個項目，可使用「-1」代替
    print(pts)
    cv2.polylines(img, [pts], True, (0, 0, 255), 3)

cv2.imshow("Image", img)
# cv2.imshow("GrayImage", gray_img)
cv2.waitKey(0)
exit(0)