import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

img = cv2.VideoCapture(0)

# def putText(x,y,text,color=(0,0,0)):
#     global img
#     fontpath = 'NotoSansTC-Regular.otf'
#     font = ImageFont.truetype(fontpath, 20)
#     imgPil = Image.fromarray(img)
#     draw = ImageDraw.Draw(imgPil)
#     draw.text((x, y), text, fill=color, font=font)
#     img = np.array(imgPil)

def boxSize(arr):
    global data
    box_roll = np.rollaxis(arr,1,0)
    xmax = int(np.amax(box_roll[0]))
    xmin = int(np.amin(box_roll[0]))
    ymax = int(np.amax(box_roll[1]))
    ymin = int(np.amin(box_roll[1]))
    return (xmin,ymin,xmax,ymax)

qrcode = cv2.QRCodeDetector()             # QRCode 偵測器

while True:
    ret, frame = img.read()
    if not ret:
        print("Cannot receive frame")
        break
    img0 = cv2.resize(frame,(0,0),fx=1,fy=1)     # 縮小尺寸，加快速度
    ok, data, bbox, rectified = qrcode.detectAndDecodeMulti(img0)  # 辨識 QRCode
    if ok:
        for i in range(len(data)):
            text = data[i]            # QRCode 內容
            box = boxSize(bbox[i])    # QRCode 座標
            cv2.rectangle(img0,(box[0],box[1]),(box[2],box[3]),(0,0,255),5)  # 繪製外框
            # putText(box[0],box[3],text,color=(0,0,255))                     # 顯示文字
    cv2.imshow('img', img0)
    if cv2.waitKey(1) == ord('q'):
        break

img.release()
cv2.destroyAllWindows()