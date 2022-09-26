from io import StringIO
  
# 生成一個StringIO物件，當前緩衝區內容為ABCDEF  
s = StringIO('ABCDEF' )  
# 從開頭寫入，將會覆蓋ABC  
# s.write('abc')  
# # 每次使用read()讀取前，必須seek()  
# # 定位到開頭  
# s.seek(0)  
# # 將輸出abcDEF  
# print (s.read())  
# # # 定位到第二個字元c  
# s.seek(2)  
# # # 從當前位置一直讀取到結束，將輸出cDEF  
# print (s.read())  
# s.seek(3) 
# # # 從第三個位置讀取兩個字元，將輸出DE  
# print (s.read(2))  
# s.seek(6) 
# print(s.read()) 
# # # 從指定位置寫入
# s.write('GH')  

# s.seek(0)  
# # # 將輸出abcDEFGH
# print(s.read())  

# # 如果讀取所有內容，可以直接使用getvalue()
# # 將輸出abcDEFGH  
print(s.getvalue())  