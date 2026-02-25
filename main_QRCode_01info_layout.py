import re
import json
import os
from enum import Enum
from dataclasses import dataclass, field
from typing import List, Dict, Optional

class Category(Enum):
    FOOD = "飲食"
    CLOTHING = "衣物"
    MEDICAL = "醫藥/衛生"
    HOUSING = "住(租金/房貸)"
    HOUSEHOLD_GOODS = "生活物品"
    TRANSPORT = "行(交通費/油錢)"
    EDUCATION = "教育(學費)"
    ENTERTAINMENT = "娛樂(場地門票)"
    FINANCE = "理財"
    WINNING = "發票中獎"
    OTHER = "其它"

class SubCategory(Enum):
    # (value, label, parent_category)
    VEGETABLE = ("vegetable", "菜錢", Category.FOOD)
    DRINK = ("drink", "飲料", Category.FOOD)
    RESTAURANT = ("restaurant", "餐廳", Category.FOOD)
    SNACK = ("snack", "零食", Category.FOOD)

    PARKING = ("parking", "停車費", Category.TRANSPORT)
    GASOLINE = ("gasoline", "油錢", Category.TRANSPORT)

    WATER_ELECTRIC = ("water_electric", "水電", Category.HOUSING)
    PHONE = ("phone", "手機/電話", Category.HOUSING)

    SUNDRIES = ("sundries", "雜貨", Category.HOUSEHOLD_GOODS)
    TISSUE = ("tissue", "衛生紙", Category.HOUSEHOLD_GOODS)

    MOVIE = ("movie", "電影票", Category.ENTERTAINMENT)

    FUND = ("fund", "基金", Category.FINANCE)
    TAX = ("tax", "稅金", Category.FINANCE)

    DELIVERY_711 = ("delivery_711", "網購取件-7-11", Category.OTHER)

    def __init__(self, value, label, parent):
        self._value_ = value
        self._label = label
        self._parent = parent

    @property
    def label(self): return self._label

    @property
    def parent(self): return self._parent

    @classmethod
    def from_label(cls, label):
        for item in cls:
            if item.label == label: return item
        return None

    @classmethod
    def from_value(cls, value):
        for item in cls:
            if item.value == value: return item
        return None

@dataclass
class QRCodeInfo:
    recieve: str = ""                   # 1. 發票字軌號碼 (10)
    recieve_date: str = ""              # 2. 發票開立日期 (7)
    recieve_randam: str = ""            # 3. 隨機碼 (4)
    recieve_sale: str = ""              # 4. 銷售額 (8)
    recieve_total_sale: str = ""        # 5. 總計額 (8)
    recieve_buyer_invoice_num: str = "" # 6. 買方統一編號 (8)
    recieve_seller_invoice_num: str = ""# 7. 賣方統一編號 (8)
    recieve_AESencode: str = ""         # 8. 加密驗證資訊 (24)

    after77: str = ""
    recieve_free_usage: str = ""        # 9. 營業人自行使用區 (10碼)
    recieve_Item: str = ""              # 10.二維條碼記載完整品目筆數
    recieve_totle_Item: str = ""        # 11.該張發票交易品目總筆數
    codetype: str = ""                  # 12.中文編碼參數 (1碼)

    # Store items as a list of dictionaries for better handling
    item_list: List[Dict[str, str]] = field(default_factory=list)

    # Classification results
    category: str = "其它"
    sub_category: str = ""

    @property
    def items(self) -> str:
        return " ".join([i['name'] for i in self.item_list])

    @property
    def item_quantity(self) -> str:
        return " ".join([i['qty'] for i in self.item_list])

    @property
    def items_price(self) -> str:
        return " ".join([i['price'] for i in self.item_list])

class ClassificationEngine:
    def __init__(self, config_path='classification_map.json'):
        self.config_path = config_path
        self.mapping = self._load_mapping()

    def _load_mapping(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"keywords": {}, "exact_items": {}}

    def _save_mapping(self):
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(self.mapping, f, ensure_ascii=False, indent=4)

    def classify_item(self, item_name):
        # 1. Exact match
        if item_name in self.mapping["exact_items"]:
            return self.mapping["exact_items"][item_name]

        # 2. Keyword match
        for sub_cat_label, keywords in self.mapping["keywords"].items():
            for kw in keywords:
                if kw in item_name:
                    return sub_cat_label

        return None

    def update_mapping(self, item_name, sub_cat_label):
        self.mapping["exact_items"][item_name] = sub_cat_label
        self._save_mapping()

    def add_keyword(self, sub_cat_label, keyword):
        if sub_cat_label not in self.mapping["keywords"]:
            self.mapping["keywords"][sub_cat_label] = []
        if keyword not in self.mapping["keywords"][sub_cat_label]:
            self.mapping["keywords"][sub_cat_label].append(keyword)
        self._save_mapping()
    
def recode(x):      # 判別 0 , 1 , 2 是否為 Big5, UTF-8, Base64
    print("-----Processing barcode data-----")
    match = re.search("[0-9]:[0-9]:[0-9]:", x)
    if not match:
        return x

    y = list(filter(None, match.group(0).split(':')))
    try:
        encode_type = int(y[2])
    except (IndexError, ValueError):
        return x

    if encode_type == 0: # Big5
        try:
            # If it was decoded as utf-8 but was actually Big5,
            # this trick sometimes works if the bytes were compatible,
            # but it's better to handle bytes from the start.
            # Keeping the user's original logic for now but making it safer.
            print('-----Attempting Big5 re-decoding-----')
            new_x = x.encode('latin1').decode('big5')
            # Note: latin1 is often used to get the original bytes from a mis-decoded utf-8 string if it was 1-to-1.
            # But the original code used shift-jis. I'll stick to a safer approach.
            return new_x
        except Exception:
            try:
                return x.encode('shift-jis').decode('big5')
            except Exception:
                print('Big5 decoding failed')
                return x
    elif y == 1:
        print('-----utf-8 decoded!!-----')
        return x
    elif y == 2:
        print('undefinde decode: base64') 

def reInfo(qr_list):
    """
    qr_list: A list of QR code strings from the same invoice.
    """
    if not qr_list:
        return None

    # Identify QR1 (starts with invoice number) and QR2 (starts with **)
    qr1 = ""
    qr2_list = []
    for qr in qr_list:
        if qr.startswith("**"):
            qr2_list.append(qr)
        elif len(qr) >= 77:
            qr1 = qr

    if not qr1:
        # If we only have QR2, we can't do much without the header
        return None

    # Process QR1
    qr1 = recode(qr1)
    recieve = qr1[:10]
    recieve_date = qr1[10:17]
    recieve_randam = qr1[17:21]
    recieve_sale_Hex = qr1[21:29]
    recieve_sale = str(int(recieve_sale_Hex, 16))
    recieve_total_sale_Hex = qr1[29:37]
    recieve_total_sale = str(int(recieve_total_sale_Hex, 16))
    recieve_buyer_invoice_num = qr1[37:45]
    if recieve_buyer_invoice_num == "00000000":
        recieve_buyer_invoice_num = "一般消費者"
    recieve_seller_invoice_num = qr1[45:53]
    recieve_AESencode = qr1[53:77]

    after77 = qr1[77:]
    y = after77.split(':')
    z = [i for i in y if i != ""]
    if len(z) < 4:
        # Something is wrong, but let's try to proceed
        recieve_free_usage = ""
        recieve_Item = "0"
        recieve_totle_Item = "0"
        codetype = "1"
    else:
        recieve_free_usage = z[0]
        recieve_Item = z[1]
        recieve_totle_Item = z[2]
        codetype = z[3]

    if codetype == '0': codetype_label = '0:Big5'
    elif codetype == '1': codetype_label = '1:UTF-8'
    elif codetype =='2': codetype_label = '2:Base64'
    else: codetype_label = codetype

    all_items = []

    # Extract items from QR1
    match = re.search("[0-9]{1}:[0-9]{1}:[0-9]{1}:", qr1)
    if match:
        item_data = qr1[match.end():].split(":")
        for i in range(0, len(item_data) // 3 * 3, 3):
            if i+2 < len(item_data):
                all_items.append({
                    "name": item_data[i],
                    "qty": item_data[i+1],
                    "price": item_data[i+2]
                })

    # Extract items from QR2
    for qr2 in qr2_list:
        # QR2 often starts with ** and then items.
        # Sometimes there's also a count similar to QR1 if it's not the last one?
        # Usually it's just **:Item:Qty:Price
        qr2_content = qr2[2:]
        if qr2_content.startswith(":"):
            qr2_content = qr2_content[1:]

        # Check if there's also a count header in QR2 (some implementations do this)
        match = re.search("[0-9]{1}:[0-9]{1}:[0-9]{1}:", qr2_content)
        if match:
            item_data = qr2_content[match.end():].split(":")
        else:
            item_data = qr2_content.split(":")

        for i in range(0, len(item_data) // 3 * 3, 3):
             if i+2 < len(item_data):
                all_items.append({
                    "name": item_data[i],
                    "qty": item_data[i+1],
                    "price": item_data[i+2]
                })

    return QRCodeInfo(
        recieve=recieve,
        recieve_date=recieve_date,
        recieve_randam=recieve_randam,
        recieve_sale=recieve_sale,
        recieve_total_sale=recieve_total_sale,
        recieve_buyer_invoice_num=recieve_buyer_invoice_num,
        recieve_seller_invoice_num=recieve_seller_invoice_num,
        recieve_AESencode=recieve_AESencode,
        after77=after77,
        recieve_free_usage=recieve_free_usage,
        recieve_Item=recieve_Item,
        recieve_totle_Item=recieve_totle_Item,
        codetype=codetype_label,
        item_list=all_items
    )

# x="DF622694131110708397000000003000000030000000008547587XKsayZY706hvyFpe6k3TQ==:**********:2:2:1:野川蛋黃派10粒:1:65:可口可樂1250CC:1:38"
# x="YV967283921110428158400000DEB00000E520000000024804859VCmyccXFkXITSajVRYxxZQ==:**********:3:3:0:ﾀｰﾄ_ｾA､@ｯﾅﾀｰL     :1:1775:"
# reInfo(x)