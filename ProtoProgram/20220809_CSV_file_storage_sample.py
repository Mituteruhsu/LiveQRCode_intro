import csv

# ---CSV檔案寫入標題 writeheader---
# writer.writeheader()
# ---在writerow的地方傳入字典key-value對應---
# writer.writerow({'Username':'booker33','Id':1,'First Name':'Ana','Last Name':'Booker'})

file_name='Invoice_Compay.csv'

# -----------1. Creat Dictionary File(建檔完不再使用)-----------
# header_key=input("Enter header, use',' to split:").split(',')
# value=input("Enter dict_arrayuse, ',' to split:").split(',')
# dict_arr = dict(zip(header_key, value))
# print(header_key)
# print(type(header_key))
# print(dict_arr)
# print(type(dict_arr))
# try:
#     with open('Invoice_Compay.csv', 'a', newline='', encoding='utf-8') as file:
#         csv.DictWriter(file, header_key).writeheader()
#         csv.DictWriter(file, header_key).writerow(dict_arr)
#         file.close()
# except IOError:
#     print("I/O error")
# --------------------------------------------------------------

def csv_writer(Inv_num,Cpinfo):
    with open('Invoice_Compay.csv', 'a', newline='', encoding='utf-8') as file:
        csv.DictWriter(file, ['Invoice_num', 'Company']).writerow({'Invoice_num':'SI'+Inv_num,'Company':Cpinfo})
        file.close()

def csv_delet(deletinput):
    import pandas as pd
    df = pd.read_csv(file_name)
    print('----------File Read----------')
    print(df)
    df=pd.DataFrame(df)
    drop_value=df.index[df['Invoice_num'].str.contains(deletinput)].tolist()
    print('-----------------------------')
    print('本資料會被刪除', df.loc[drop_value])
    
    enterconfierm=input('請輸入y/n確認: ')
    if enterconfierm == 'y' or enterconfierm =='Y':
        df = df.drop(index=drop_value)
        df.drop_duplicates(inplace=True)
        df.to_csv(file_name, index=False, encoding='utf-8')
        print('-----------deleted-----------')
        print(df)
        print(type(df))
    else:
        csv_delet(input('請輸入欲刪除的Invoice_num: '))
        print(('-----------------------------'))
    
def csv_reader():
    import pandas as pd
    # -----read the csv as pd-----
    with open(file_name, 'r', encoding='utf-8') as file:
        reader_dic = pd.read_csv(file)
        print(reader_dic)
        file.close()
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        dict_from_csv = dict(reader)
        print(dict_from_csv)
        print(type(dict_from_csv))
        file.close()
        return dict_from_csv

def Dict_get_value_check(Iv_num):
    Iv_num_input='SI'+Iv_num
    result_company=csv_reader().get(Iv_num_input)
    if result_company is None:
        print('please update ivnum')
        Inv_num=input('Invoice_num '+Iv_num+': ')
        Cpinfo=input('Company_name: ')
        csv_writer(Inv_num,Cpinfo)
    else:
        print(Iv_num_input, result_company)
        return result_company


# ------new_value_input---------
# Inv_num='72404190'
# Cpinfo='三次方企業社'
# csv_writer(Inv_num,Cpinfo)
# --------delet_test-------------
# deletinput=input('請輸入欲刪除的Invoice_num: ')
# csv_delet(deletinput)
# ---------read_file-------------
# csv_reader()
# ------Value_check_test---------
# Dict_get_value_check('18070629')

