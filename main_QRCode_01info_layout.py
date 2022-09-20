import re
from dataclasses import dataclass
from pyzbar.pyzbar import decode

@dataclass
class QRCodeInfo:
    recieve: str                        # 1. 發票字軌號碼 (10)：記錄發票完整10碼字軌號碼。
    recieve_date: str                   # 2. 發票開立日期 (7)：記錄發票3碼民國年份2碼月份2碼日期共7碼。
    recieve_randam: str                 # 3. 隨機碼 (4)：記錄發票4碼隨機碼。
    recieve_sale: str                   # 4. 銷售額 (8)：記錄發票未稅總金額總計8碼，將金額轉換以十六進位方式記載。若買受人為非營業人且銷售系統無法順利將稅項分離計算，則以00000000記載，不足8碼左補0。
    recieve_total_sale: str             # 5. 總計額 (8)：記錄發票含稅總金額總計8碼，將金額轉換以十六進位方式記載，不足8碼左補0。
    recieve_buyer_invoice_num: str      # 6. 買方統一編號 (8)：記錄發票買受人統一編號，若買受人為一般消費者則以00000000記載。
    recieve_seller_invoice_num: str     # 7. 賣方統一編號 (8)：記錄發票賣方統一編號。
    recieve_AESencode: str              # 8. 加密驗證資訊 (24)：將發票字軌號碼10碼及隨機碼4碼以字串方式合併後使用AES 加密並採用 Base64 編碼轉換，AES所採用之金鑰產生方式請參考第叁、肆章及「加解密API使用說明書」。
# ==============================================================================================================================================================================================
# 以上欄位總計77碼。下述資訊為接續以上資訊繼續延伸記錄，且每個欄位前皆以間隔符號“:” (冒號)區隔各記載事項，若左方二維條碼不敷記載，則繼續記載於右方二維條碼。    
# ==============================================================================================================================================================================================
    recieve_free_usage: str             # 9. 營業人自行使用區 (10碼)：提供營業人自行放置所需資訊，若不使用則以10個“*”符號呈現。
    recieve_Item: str                   # 10.二維條碼記載完整品目筆數：記錄左右兩個二維條碼記載消費品目筆數，以十進位方式記載。
    recieve_totle_Item: str             # 11.該張發票交易品目總筆數：記錄該張發票記載消費品目總筆數，以十進位方式記載。
# ==============================================================================================================================================================================================
                                        # 12.中文編碼參數 (1碼)：定義後續資訊的編碼規格，若以：
                                        # (1) Big5編碼，則此值為0
                                        # (2) UTF-8編碼，則此值為1
                                        # (3) Base64編碼，則此值為2
# ==============================================================================================================================================================================================
    items: str                          # 13.品名：商品名稱，請避免使用間隔符號“:”(冒號)於品名。
    item_quantity: str                  # 14.數量：商品數量，以十進位方式記載。
    items_price: str                    # 15.單價：商品單價，以十進位方式記載。
    
def recode(x):
    print("-----From barcode.data.decode('utf-8')----- \n", x)
    y= list(filter(None, re.search("[0-9]{1}:[0-9]{1}:[0-9]{1}:", x, flags=0).group(0).split(':'))) # 正則表達找出與關鍵類似的字元
    y= int(y[2])
    if y != 1 and y == 0:
        try:
            print('-----big5 decoded!!-----')
            x=x.encode('shift-jis').decode('big5')
            print(x)
            return x
        except:
            print('not decodeable')
        finally:
            return x
    elif y != 1 and y == 2:
        print('undefinde decode: base64') 
    elif y == 1:
        print('-----utf-8 decoded!!-----')
        return x

def reInfo(x):
    import re
    x=recode(x) # 判別0,1,2 是否為utf-8, base64, big5
    recieve = x[:10]
    recieve_date = x[10:17]
    recieve_randam = x[17:21]
    recieve_sale_Hex = x[21:29]
    recieve_sale = str(int(recieve_sale_Hex, 16))
    recieve_total_sale_Hex = x[29:37]
    recieve_total_sale = str(int(recieve_total_sale_Hex, 16))
    recieve_buyer_invoice_num = x[37:45]
    if recieve_buyer_invoice_num == "00000000":
        recieve_buyer_invoice_num = "一般消費者"
    recieve_seller_invoice_num = x[45:53]
    recieve_AESencode = x[53:77]
    recieve_free_usage = x[77:87]
    recieve_Item = x[87:]
    recieve_totle_Item = x[87:]
    # print("發票字軌(10位)    : " + self.recieve)
    # print("發票開立日期 (7位): " + self.recieve_date)
    # print("隨機碼 (4位)      : " + self.recieve_randam)
    # print("銷售額 (8位)      : " + self.recieve_sale + " 元")
    # print("總計額 (8位)      : " + self.recieve_total_sale + " 元")
    # print("買方統一編號 (8位): " + self.recieve_buyer_invoice_num)
    # print("賣方統一編號 (8位): " + self.recieve_seller_invoice_num)
    # print("加密驗證資訊(24位): " + self.recieve_AESencode)
    # print("營業人使用區(10位): " + self.recieve_free_usage)
    # print("品目筆數          : " + self.recieve_Item)
    # print("品目總筆數        : " + self.recieve_totle_Item)
    # =======span 鎖定品目比數後方資料彙整=======
    x = (x[(re.search("[0-9]{1}:[0-9]{1}:[0-9]{1}:", x, flags=0).span()[1]):]).split(":") # 正則表達找出與關鍵類似的字元
    # print(x)
    # =======split 將資料變成list一一拆解=======
    # =======將list依照[1, 3, 5]的資料連接=======
    items=','.join(x[0:len(x):3])
    item_quantity=' '.join(x[1:len(x):3])
    items_price=' '.join(x[2:len(x):3])
    # print(items, item_quantity, items_price)
    return QRCodeInfo(
        recieve,
        recieve_date,
        recieve_randam,
        recieve_sale,
        recieve_total_sale,
        recieve_buyer_invoice_num,
        recieve_seller_invoice_num,
        recieve_AESencode,
        recieve_free_usage,
        recieve_Item,
        recieve_totle_Item,
        items,
        item_quantity,
        items_price
        )

# x="DF622694131110708397000000003000000030000000008547587XKsayZY706hvyFpe6k3TQ==:**********:2:2:1:野川蛋黃派10粒:1:65:可口可樂1250CC:1:38"
# x="YV967283921110428158400000DEB00000E520000000024804859VCmyccXFkXITSajVRYxxZQ==:**********:3:3:0:ﾀｰﾄ_ｾA､@ｯﾅﾀｰL     :1:1775:"
# reInfo(x)