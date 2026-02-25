import time
import csv
import threading
import pandas as pd
import main_Global_Var as var
import main_QRCode_00scanner as QRCodeScan
import main_QRCode_01info_layout as myQRCodeInfo
from main_QRCode_01info_layout import ClassificationEngine, Category, SubCategory
import main_QRCode_02_reform_LocoCSV as CompanyInfo

# 定義常態運行子程序
def Scan_job():
    QRCodeScan.QRCodedata()

def get_user_classification(info, engine):
    print("\n--- 品項列表 ---")
    for i, item in enumerate(info.item_list):
        suggested = engine.classify_item(item['name'])
        print(f"{i+1}. {item['name']} (建議分類: {suggested if suggested else '未知'})")

    # 決定主分類
    print("\n請選擇此發票的主分類 (或按 Enter 使用第一個品項的建議分類):")

    # List all subcategories
    sub_cats = list(SubCategory)
    for i, sc in enumerate(sub_cats):
        print(f"{i}: {sc.parent.value} - {sc.label}")

    choice = input("輸入編號或直接輸入分類名稱: ")
    selected_sub_cat = None
    if choice == "" and info.item_list:
        suggested = engine.classify_item(info.item_list[0]['name'])
        if suggested:
            selected_sub_cat = SubCategory.from_label(suggested)
    elif choice.isdigit():
        idx = int(choice)
        if 0 <= idx < len(sub_cats):
            selected_sub_cat = sub_cats[idx]
    else:
        selected_sub_cat = SubCategory.from_label(choice)

    if not selected_sub_cat:
        selected_sub_cat = SubCategory.DELIVERY_711 # Default or handle other
        # Actually let's just use OTHER if not found
        for sc in SubCategory:
            if sc.label == "其它": # If I had it
                selected_sub_cat = sc
                break

    # Learning: Update engine with the first item's name if it was unknown
    if info.item_list and selected_sub_cat:
        engine.update_mapping(info.item_list[0]['name'], selected_sub_cat.label)

    return selected_sub_cat

if __name__ == '__main__':
    var.var()    # 先初始化Global var
    engine = ClassificationEngine()
    # 建立子程序
    t1 = threading.Thread(target = Scan_job)
    t1.daemon = True
    t1.start()

    processed_invoices = set()
    last_list = []

    print("等待掃描 QR Code... (按 Ctrl+C 結束)")
    while True:
        if var.QRCodeList and var.QRCodeList != last_list:
            last_list = var.QRCodeList.copy()
            
            info = myQRCodeInfo.reInfo(last_list)
            if info and info.recieve not in processed_invoices:
                print(f'\n發現新發票: {info.recieve}')

                # 分類邏輯
                sub_cat = get_user_classification(info, engine)
                info.sub_category = sub_cat.label
                info.category = sub_cat.parent.value

                # 獲取賣方名稱
                seller_name = CompanyInfo.Dict_get_value_check('SI' + info.recieve_seller_invoice_num)

                # 付費方式 (暫定手動或預設)
                payment_method = "現金" # 可擴展為讓用戶選擇

                print(f'Date: {info.recieve_date}')
                print(f'Seller: {seller_name}')
                print(f'Total Sale Amount: {info.recieve_total_sale}')
                print(f'Category: {info.category} / {info.sub_category}')

                # 寫入 CSV
                csv_file = 'Invoice_Raw_data.csv'
                fieldnames = ['Date', 'Invoice_Num', 'Category', 'SubCategory', 'Consumer', 'Payment_Method', 'Content', 'Amount', 'Seller_Inv', 'Seller_Name']

                file_exists = False
                try:
                    with open(csv_file, 'r', encoding='utf-8') as f:
                        file_exists = True
                except FileNotFoundError:
                    file_exists = False

                with open(csv_file, 'a', newline='', encoding='utf-8') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    if not file_exists:
                        writer.writeheader()

                    writer.writerow({
                        'Date': info.recieve_date,
                        'Invoice_Num': info.recieve,
                        'Category': info.category,
                        'SubCategory': info.sub_category,
                        'Consumer': info.recieve_buyer_invoice_num,
                        'Payment_Method': payment_method,
                        'Content': f"{seller_name}: {info.item_list[0]['name'] if info.item_list else ''}",
                        'Amount': info.recieve_total_sale,
                        'Seller_Inv': 'SI' + info.recieve_seller_invoice_num,
                        'Seller_Name': seller_name
                    })
                
                processed_invoices.add(info.recieve)
                print(f'發票 {info.recieve} 已存檔。')
            
            time.sleep(0.5)