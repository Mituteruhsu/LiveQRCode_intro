import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread("recive20220708a.jpg")                       # 開啟圖片
print(decode(img))                                            # 進行解碼
print('==================')
print(type(decode(img)))                                      # type = list      
print('==================')
# pyzbar中的decode會回傳4個基本的值(data, type, rect, polygon)
for barcode in decode(img):                                   # 列出裡面包含的檔案
    print('data=', barcode.data)
    print('------------------')
    print('type=', barcode.type)
    print('------------------')
    print('rect=', barcode.rect)
    print('------------------')
    print('polygon=', barcode.polygon)
    print('------------------')
    print('quality=', barcode.quality)
    print('------------------')
    print('orientation=', barcode.orientation)