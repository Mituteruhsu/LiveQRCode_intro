# LiveQRCode_intro
I put this for study purpose. 
This is an E-invoice reading project.   
There are planty of benefit in studying QRCode as a biginner of Python.  
If you find a better way of improving.  
Please let me know.  

Thank you!

# The project is simple

1. Start up webcam with openCV.
2. Use pyzbar and openCV to decode the QRcode.
3. Frame the QRcode with text.
4. Print out the data.
5. Store the data into csv.
6. Use google API to upload the reformated data.

# Problem

1. When you scan the QRCode with TestScan/QRCode_test_00.py, the "print(f'pymessage:{pybarcode}')" will get garbled.  
    It seems to be a problem with decode method.........

# What is in mind

1. Use AI to read the QRCode
2. Decode issue. The data is not 'utf-8' can be 'shift-jis' 'big5'
3. Methods of decode.
4. Get better understanding of QRCode with bytes.

# Reference

1. E- Invoice Platform:  
    https://www.einvoice.nat.gov.tw/EINSM/ein_upload/html/ENV/1428905476324-1.html