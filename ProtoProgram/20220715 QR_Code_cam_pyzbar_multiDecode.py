from sys import exit

from PIL import Image
import numpy as np
import pyzbar
import cv2
 
# 加載圖片並把它轉換爲灰度圖片
image = cv2.imread('recive20220708a.jpg')
img = Image.open(r'recive20220708a.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#cv2.imshow("sobel_Image", gray)
#cv2.waitKey(0)
#使用Canny做邊緣檢測
gradient = cv2.Canny(gray , 20 ,520)
#cv2.imshow("Canny_Image", gradient)
#cv2.waitKey(0)

(_, thresh) = cv2.threshold(gradient, 225, 255, cv2.THRESH_BINARY) # 二值化
cv2.imshow("threshold_Image", thresh)
#cv2.waitKey(0)
# 構建kernel然後應用到 thresholded 圖像上
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 5))#形態學處理，定義矩形結構
closed = cv2.dilate(thresh, kernel, iterations = 1)#膨脹圖像，連接斷點
#cv2.imshow("dilate_Image", closed)
#cv2.waitKey(0)

im, contours, hierarchy = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#print contours
x = len(contours)
a = []
s = []

#打印面積
for i in range(0,x):
    s.append(cv2.contourArea(contours[i]))

#保留面積大於8000的輪廓
for m in range(0,x):
    if s[m] >= 8000 and s[m] <= 25000 :
        a.append(s[m])
    else:
        continue
        
z = max(a)

#for j in a:
#    print "a was : %f",j

for k in range(0,x):
    #增加一些篩選條件
    if s[k] >= 8000 and s[k] <= 25000 and ((z - s[k]) <= 8500 ) :
        rect = cv2.minAreaRect(contours[k])#返回矩形的中心點座標，長寬，旋轉角度
        box = np.int0(cv2.boxPoints(rect))
        cv2.drawContours(image, [box], -1, (255, 0, 0), 2)#畫一個方框把條形碼區域圈起來

        u,v,w,t = cv2.boundingRect(contours[k]) #獲取輪廓座標
        #print u,v,w,t
        #根據座標把條碼裁剪下來並保存
        o = (u,v,u+w,v+t)
        barcode = img.crop(o)
        barcode.save(r'recive20220708a_crop.jpg')
        #print "s : %f",s[k]
        #構建解碼器
        scanner = pyzbar.ImageScanner()
        scanner.parse_config('enable')
        pil = Image.open('recive20220708a_crop.jpg').convert('L')
        width, height = pil.size
        #解碼
        raw = pil.tostring()
        image0 = pyzbar.Image(width, height, 'Y800', raw)
        scanner.scan(image0)
        for symbol in image0:
            print ('decoded', symbol.type, 'symbol', '"%s"' % symbol.data)
    else:
        continue

cv2.imshow("Image", image)
cv2.waitKey(0)
exit(0)