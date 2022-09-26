import dis
import base64
import binascii

getBytes = b'\xef\xbe\x80\xef\xbd\xb0\xef\xbe\x84_\xef\xbd\xbeA\xef\xbd\xa4@\xef\xbd\xaf\xef\xbe\x85\xef\xbe\x80\xef\xbd\xb0'

print("[05]: %s" % type(getBytes))
print("[06]: %s" % getBytes)
reverseBytes = getBytes[::-6]
print("[08]: %s" % reverseBytes)

bytesToHex = binascii.b2a_hex(reverseBytes)
print("[11]: %s" % bytesToHex)

bytesHexToASCII = bytesToHex.decode('ascii')
print("[14]: %s" % bytesHexToASCII)

hexToDec = int(bytesHexToASCII, 16)
print("[17]: %s" % hexToDec)


print('======分隔=======')


line = b'\xef\xbe\x80\xef\xbd\xb0\xef\xbe\x84_\xef\xbd\xbeA\xef\xbd\xa4@\xef\xbd\xaf\xef\xbe\x85\xef\xbe\x80\xef\xbd\xb0'
# dis.dis(line)
linedecode=line.decode('utf-8')
print(linedecode)
print(line.decode('utf-8','ignore').encode('shift-jis','ignore').decode('big5'))
# linejp=linedecode.decode('shift-jis')
# print(linejp)
# print('orig: ', line)
str='幫寶適一級幫'
str_utf8=str.encode('utf-8')
print("utf8: ", str_utf8)
str_utf16=str.encode('utf-16')
print("utf16: ", str_utf16)
str_big5=str.encode('BIG5')
print("BIG5:  ", str_big5)

# str_Shift_JS=line.decode('shift-jis')
# print("Shift-JS:  ", str_Shift_JS)
print('----------------------------')
str_base64=base64.b64encode(str_utf8)
print("strutf8:  ", str_base64)
str_base64=base64.b64encode(str_big5)
print("strbig5:  ", str_base64)


# def string_encoding(data: bytes):
#     """
#     獲取字符編碼類型
#     :param data: 字節數據
#     :return:
#     """
#     # data = b'\xef\xbe\x80\xef\xbd\xb0\xef\xbe\x84_\xef\xbd\xbeA\xef\xbd\xa4@\xef\xbd\xaf\xef\xbe\x85\xef\xbe\x80\xef\xbd\xb0'
#     CODES = ['UTF-8', 'GB18030', 'BIG5']
#     # 遍歷編碼類型
#     for code in CODES:
#         try:
#             decode_d=data.decode(code, 'ignore')
#             print(decode_d)
            
#         except UnicodeDecodeError:
#             continue
#     return 'unknown'

# data = b'\xef\xbe\x80\xef\xbd\xb0\xef\xbe\x84\xef\xbd\xbe\xef\xbd\xa4\xef\xbd\xaf\xef\xbe\x85\xef\xbe\x80\xef\xbd\xb0'
# if __name__ == "__main__":
#     string_encoding(data)
