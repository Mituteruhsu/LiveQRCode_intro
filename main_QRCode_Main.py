import time
import threading
import main_Global_Var as var
import main_QRCode_00scanner as QRCodeScan
import main_QRCode_01info_layout as myQRCodeInfo


# 定義常態運行子程序
def Scan_job():
    QRCodeScan.QRCodedata()


if __name__ == '__main__':
    var.var()    # 先初始化Global var
    # 建立子程序
    t1 = threading.Thread(target = Scan_job)
    # t2 = threading.Thread(target = Web_insert)
    # 執行子程序
    t1.start()
    # t2.start()
    # 使用 join 等待 t1 執行完畢
    # t2.join()

    strcheck = ""
    while True:
        if var.QRCodeStr != "" and var.QRCodeStr != strcheck:
            strcheck = var.QRCodeStr
            # print(f"main variable.QRCodeStr={strcheck}")
            # myQRCodeInfo.QRCodeInfo(checkStr)
            info=myQRCodeInfo.reInfo(strcheck)
            
            # recieve_date=info.recieve_date
            # recieve=info.recieve
            # recieve_total_sale=info.recieve_total_sale    
            print(f'Recieve Num: {info.recieve}')
            print(f'Date: {info.recieve_date}')
            print(f'Randam Code: {info.recieve_randam}')
            print(f'Sale Amount: {info.recieve_sale}')
            print(f'Total Sale Amount: {info.recieve_total_sale}')
            print(f'Buyer Invoice Num: {info.recieve_buyer_invoice_num}')
            print(f'Seller Invoice Num: {info.recieve_seller_invoice_num}')
            print(f'AES encode: {info.recieve_AESencode}')
            print(f'Text after 77: {info.after77}')
            print(f'Free Usage: {info.recieve_free_usage}')
            print(f'Total Items Count: {info.recieve_Item}')
            print(f'Recieve Items Count: {info.recieve_totle_Item}')
            print(f'Encode Type: {info.codetype}')
            print(f'Item Name: {info.items}')
            print(f'Item Quantity: {info.item_quantity}')
            print(f'Item Price: {info.items_price}')
            
                        
