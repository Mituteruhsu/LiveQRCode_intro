import pygsheets
import pandas as pd

gc = pygsheets.authorize(service_file='qrcode-recieve-data-9cdb94f5bcc5.json')
sheet_url = ('https://docs.google.com/spreadsheets/d/1NIK8oKmTqEm2nOAHScXoDXNENdssGkUJ23fBBlt9cdw/edit#gid=0')
google_sheet = gc.open_by_url(sheet_url)
wks_title=google_sheet.title            #顯示sheet檔案名稱
wks_list = google_sheet.worksheets()    #顯示所有Worksheet '工作表' 名稱
wks = google_sheet[0]                   #選取worksheet by 順序 [0],[1],[2]
print(f'試算表名稱: {wks_title}', wks_list[0])
print('---------DataFrame (From Google Sheet)---------')
df = wks.get_as_df()
print(df)
print('-----------------------------------------------')

pdread = pd.read_csv('Invoice_Raw_data.csv')
x = input('是否顯示本地端資料(y/n)?')
if x == 'y' or x== 'Y':
    print('---------DataFrame (From Invoice_Raw_data.csv)---------')
    print(pdread)
    print('-----------------------------------------------')

# Upload data from CSV to Google Sheet
y = input('是否上傳本地端資料並覆蓋至Google Sheet(y/n)?')
if y == 'y' or y == 'Y':
    wks.set_dataframe(pdread, 'A1', copy_index=False, copy_head=True, extend=False, fit=False, escape_formulae=False)
    print('上傳完成')

# 用預設瀏覽器打開網頁
import webbrowser    
urL='https://docs.google.com/spreadsheets/d/1NIK8oKmTqEm2nOAHScXoDXNENdssGkUJ23fBBlt9cdw/edit#gid=0'
webbrowser.get('windows-default').open_new(urL)

