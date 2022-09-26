import re
# x="DF622694131110708397000000003000000030000000008547587XKsayZY706hvyFpe6k3TQ==:**********:2:2:1:野川蛋黃派10粒:1:65:可口可樂1250CC:1:38"
# x="DE428972561110715819500000509000005492217427024804859nozbd7t7L+KffoUVC5eNQw==:**ceepos**:1:1:1:95無鉛汽油:47.301:28.6"
# x="YU468519311110428611300000206000002060000000072404190I7pvDp/dVQoPgVms+qfMbQ==:**********:2:2:1:水壺配件組(B1-1):8:0:Tritan運動透明水壺(B7-1):2:259:"
x='YV967283921110428158400000DEB00000E520000000024804859VCmyccXFkXITSajVRYxxZQ==:**********:3:3:0:ﾀｰﾄ_ｾA､@ｯﾅﾀｰL     :1:1775:'

# 1. 發票字軌 (10位)：記錄發票完整十碼號碼。
recieve = x[:10]
print("發票字軌 (10位)   : " + recieve)
# 2. 發票開立日期 (7位)：記錄發票三碼民國年、二碼月份、二碼日期。
recieve_date = x[10:17]
print("發票開立日期 (7位): " + recieve_date)
# 3. 隨機碼 (4位)：記錄發票上隨機碼四碼。
recieve_randam = x[17:21]
print("隨機碼 (4位)      : " + recieve_randam)
# 4. 銷售額 (8位)：記錄發票上未稅之金額總計八碼，將金額轉換以十六進位方式記載。若營業人銷售系統無法順利將稅項分離計算，則以00000000記載。
recieve_sale_Hex = x[21:29]
print("16進位:", recieve_sale_Hex)
recieve_sale = str(int(recieve_sale_Hex, 16))
print("銷售額 (8位)      : " + recieve_sale + "元")
# 5. 總計額 (8位)：記錄發票上含稅總金額總計八碼，將金額轉換以十六進位方式記載。
recieve_total_sale_Hex = x[29:37]
print("16進位:", recieve_total_sale_Hex)
recieve_total_sale = str(int(recieve_total_sale_Hex, 16))
print("總計額 (8位)      : " + recieve_total_sale + "元")
# 6. 買方統一編號 (8位)：記錄發票上買受人統一編號，若買受人為一般消費者則以 00000000記載。
recieve_buyer_invoice_num = x[37:45]
if recieve_buyer_invoice_num == "00000000":
    recieve_buyer_invoice_num = "一般消費者"
print("買方統一編號 (8位): " + recieve_buyer_invoice_num)
# 7. 賣方統一編號 (8位)：記錄發票上賣方統一編號。
recieve_seller_invoice_num = x[45:53]
print("賣方統一編號 (8位): " + recieve_seller_invoice_num)
# 8. 加密驗證資訊 (24位)：將發票字軌十碼及隨機碼四碼以字串方式合併後使用 AES 加密並採用 Base64 編碼轉換。
recieve_AESencode = x[53:77]
print("加密驗證資訊(24位): " + recieve_AESencode)
# 以上欄位總計77碼。下述資訊為接續以上資訊繼續延伸記錄，且每個欄位前皆以間隔符號“:”(冒號)區隔各記載事項，若左方二維條碼不敷記載，則繼續記載於右方二維條碼。
# 9. 營業人自行使用區 (10位)：提供營業人自行放置所需資訊，若不使用則以10個“*”符號呈現。
recieve_free_usage = x[77:87]
print("營業人使用區(10位): " + recieve)
# 10.二維條碼記載完整品目筆數：記錄左右兩個二維條碼記載消費品目筆數，以十進位方式記載。
recieve_Item = x[87:]
print("品目筆數          : " + recieve_Item)
# 11.該張發票交易品目總筆數：記錄該張發票記載總消費品目筆數，以十進位方式記載。
recieve_totle_Item = x[87:]
print("品目總筆數        : " + recieve_totle_Item)
# replaceC = recieve_totle_Item.replace(':', ': ')
# y=replaceC.split(': ')
# print("品目總筆數        : " + replaceC)
# print("品目總筆數        : " + y)

x = (x[(re.search("[0-9]{1}:[0-9]{1}:[0-9]{1}:", x, flags=0).span()[1]):]).split(":") # 正則表達找出與關鍵類似的字元
# =======split 將資料變成list一一拆解=======
# =======將list依照[1, 3, 5]的資料連接=======
print('x:', x)
items=','.join(x[0:len(x):3])
item_quantity=' '.join(x[1:len(x):3])
items_price=' '.join(x[2:len(x):3])
print(items)
print(item_quantity)
print(items_price)
# 12.中文編碼參數 (1位)：定義後續資訊的編碼規格，若以：
# (1) Big5編碼，則此值為0
# (2) UTF-8編碼，則此值為1
# (3) Base64編碼，則此值為2