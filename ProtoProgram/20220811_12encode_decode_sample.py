from pyzbar.pyzbar import decode
import qrcode

x=b'AJ1993490911106300768000004B0000004EC0000000084179325V3rnn4plF6T5L/l1N5thrw==:**********:2:2:0:\xe8\xb1\xa1\xe5\x8d\xb0\xe9\x9b\xbb\xe5\xad\x90?'
# x=b'\xc3\xaf\xc2\xbe\xc2\x80\xc3\xaf\xc2\xbd\xc2\xb0\xc3\xaf\xc2\xbe\xc2\x84_\xc3\xaf\xc2\xbd\xc2\xbeA\xc3\xaf\xc2\xbd\xc2\xa4@\xc3\xaf\xc2\xbd\xc2\xaf\xc3\xaf\xc2\xbe\xc2\x85\xc3\xaf\xc2\xbe\xc2\x80\xc3\xaf\xc2\xbd\xc2\xb0L     :1:1775:'

utf8=x.decode('utf-8').encode('utf-8').decode('utf-8')
print(utf8)
big5=x.decode('big5', 'ignore')
print(big5)
# print('utf-8: ', x.decode('utf-8', 'ignore').encode('shift-jis', 'ignore').decode('utf-8', 'ignore'))
# print('big5: ', x.decode('big5', 'ignore'))
# print('shift-jis: ', x.decode('shift-jis', 'ignore'))
# print('re-encode shift-jis: ', x.decode('shift-jis', 'ignore').encode('shift-jis'))

# y=b'\xc3\xaf\xc2\xbe\xc2\x80\xc3\xaf\xc2'
# print(bytes(y).decode('big5', 'ignore'))
# y='\xc3\xaf\xc2\xbe\xc2\x80\xc3\xaf\xc2\xbd\xc2\xb0\xc3\xaf\xc2\xbe\xc2\x84_\xc3\xaf\xc2\xbd\xc2\xbeA\xc3\xaf\xc2\xbd\xc2\xa4@\xc3\xaf\xc2\xbd\xc2\xaf\xc3\xaf\xc2\xbe\xc2\x85\xc3\xaf\xc2\xbe\xc2\x80\xc3\xaf\xc2\xbd\xc2\xb0L     :1:1775:''
# print(type(y))

# s='\xef\xbe\x80\xef\xbd\xb0\xef\xbe\x84_\xef\xbd\xbeA\xef\xbd\xa4@\xef\xbd\xaf\xef\xbe\x85\xef\xbe\x80\xef\xbd\xb0L     :1:1775:'
# s = '你好'
# x="ﾀｰﾄ_ｾA､@ｯﾅﾀｰL     :1:1775:".encode('shift-jis')
# x=x.decode('big5')
# print(x)


# s_to_unicode = s.encode(encoding='utf-8').decode(encoding='utf-8')  # 要告訴decode原本的編碼是哪種
# print(s_to_unicode)

