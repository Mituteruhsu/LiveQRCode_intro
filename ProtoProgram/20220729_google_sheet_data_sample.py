import pygsheets
import pandas as pd

gc = pygsheets.authorize(service_file='D:\Allen\GoogleSheetTestkey\ Personal key')
sht = gc.open_by_url('https://docs.google.com/spreadsheets/ your own address')
wks_title=sht.title
wks_list = sht.worksheets()
# print(sht.title, wks_list)
wks = sht[0]
# df = pd.DataFrame(wks.get_all_records())
# print(df)


def wks_data_match():
    
    import main_QRCode_01info_layout as Codeinfo
    # invoice=Codeinfo.recieve_seller_invoice_num
    invoice="SI"+"18070626" # 測試用
    wks.cell('C2').value = invoice
    D2 = wks.cell('D2').value
    if D2 != "#N/A":
        print(D2)
        return D2
    else:
        print('you need to update list')
    
if __name__ == "__main__":
    wks_data_match()



    # wksreformat=wksallvalue.set_number_format(pygsheets.FormatType.TEXT)
    # print(wksreformat)
    # print(wks.get_all_records())
    # print(wksallvalue)
    # print(wksallrecord)
#     # print(wks.set_text_format(str))

#     A2 = wks.cell('A2').value
#     print(A2)
#     if invoice == A2:
#         A2 = wks.cell('B2').value
#         print(A2)

# if __name__ == "__main__":
#     wks_data_match()


# c1.set_number_format(pygsheets.FormatType.NUMBER, '00.0000')

# # 3.選取要 Sheet 清單
# wks = sht[0]
# print(wks)
# wks2 = sht.worksheet_by_title("BtaxID")
#選取by順序
# wks = sht[0]

# #選取by名稱
# wks2 = sht.worksheet_by_title("BtaxID")
# print(wks2)
# #更新名稱
# wks.title = "NewTitle"
# #隱藏清單
# wks.hidden = False

# ==========三. Python 讀取 GoogleSheet 資料==========
#讀取
# A1 = wks.cell('A1')
# A1.value
# A2=wks.cell('A2')
# print(A2)

# print(A1)
# print(A1.value)


#讀取成 df
# df = pd.DataFrame(wks.get_all_records())
# print(wks.get_all_records())
# print(pd.DataFrame(wks.get_all_records()))
#讀取 df 也可以這樣寫
# print(wks.get_as_df())
# #匯出CSV
# wks.export(pygsheets.ExportType.CSV)

# ==========四. Python 更新 GoogleSheet 資料==========
# Python 做 GoogleSheet 的修改資料，利用 update_cell 語法可以修改單獨欄位的值，update_cells 可以修改多個欄位。

# dataframe to worksheet
# wk1.set_dataframe(df, 'A1') #從欄位 A1 開始

# Update
# wks.update_cell('A1', "Hey yank this numpy array")
# wks3.update_cells('A2:A5',[['name1'],['name2'],['name3'],['name4']])
# 使用update_cell容易出現問題，也可以修正成
# wks.cell('C3').value = 'SI01201001'
# -------------------------------------------------------
# -----pygsheets 帶有值的表格插入 (insert with values)
# 內建的函數就有這個 keyword arguments，直接使用即可，
# (注意 values 必須是 matrix。)

# # insert with values
# values = [['M', 'N', 'O']] # matrix
# insert_rows = 1 # add start from 2
# sheet_test01.insert_rows(insert_rows, number=1, values=values) 
# -------------------------------------------------------
# -----pygsheets 表格插入 (insert)
# 插入某一行，要注意邏輯是我們填入的數字的後一行
# (換句話說，我們如果填 1，「 1 不會動，會插入的是 2 」)

# # insert
# col = 1
# sheet_test01.insert_cols(col, number=3) # add 2, 3, 4 (B, C, D)

# row = 1
# sheet_test01.insert_rows(row, number=3) # add 2, 3, 4
# -------------------------------------------------------
# -----pygsheets 表格結尾填入 (append)
# 會直接插在文件的最末尾，注意 values 必須是 matrix

# # append
# values = [['X', 'Y', 'Z']] # matrix
# sheet_test01.append_table(values=values) 

# ==========五. Python 刪除 GoogleSheet 資料==========

# Python 做 GoogleSheet 利用 clear 可清除所有值，del_worksheet 可刪除Sheet。

# # 清除sheet內所有值 
# wks.clear()
 
# # 刪除sheet
# sht.del_worksheet(wks) 

#  ==========六. Python 串接 GoogleSheet 的其他應用==========

# set_dataframe ：可以匯入 Dataframe 資料
# share ：可以授權權限
# remove_permissions： 移除權限語法

# #在資料最後面，匯入 Dataframe
# wks.set_dataframe(df, start = "A"+str(len(wks.get_all_values())+1) ,copy_head=False)

# # 授權
# sht.share("test@gmail.com")

# # 移除權限
# sht.remove_permissions("test@gmail.com")


# Playing around Worksheet

# Open a worksheet

# wk1 = sh.sheet1 or wk1 =sh[0] # Open first worksheet

# Get title, id, and url of worksheet

# wk1.title       # Returns title of worksheet
# wk1.id          # Returns id of worksheet
# wk1.url         # Returns url of worksheet

# Get rows and cols count

# wk1.rows # returns number of rows
# wk1.cols # returns number of columns 

# Get cell object and cell value

# wk1.cell((row_number,col_number))       # Returns cell object
# wk1.cell((row_number,col_number)).value # Returns cell value as string
# set cell format
# c1.set_number_format(pygsheets.FormatType.NUMBER, '00.0000')
# Get value/values/records

# wk1.get_value('A1')        # Returns A1’s value
# wk1.get_value('A1', 'B2')  # Returns list of values 
# wk1.get_all_values()       # Returns list of all values in worksheet
# wk1.get_all_records()      # Returns a list of dictionaries