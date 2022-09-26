import re

x=":2:2:1:野川蛋黃派10粒:1:65:可口可樂1250CC:1:38"
# x="DF622694131110708397000000003000000030000000008547587XKsayZY706hvyFpe6k3TQ==:**********:2:2:1:野川蛋黃派10粒:1:65:可口可樂1250CC:1:38"
# x="**ceepos**:1:1:1:95無鉛汽油:47.301:28.6"
result = re.search("[0-9]{1}:[0-9]{1}:[0-9]{1}:", x, flags=0) # 正則表達找出與關鍵類似的字元
x=x[(result.span()[1]):]

print(result)              # 印出與該組字元有關的內容    
print(result.group())      # match 中的內容
print(result.span())       # 字元的位置
print((result.span()[1]))  # 該組字元的頭
print("========================")
print(x)
print(type(x))
# print("========================")
# # x=x.replace(':', " ")
# print(x)
print("========================")
x=x.split(":")
print(x)
print(type(x))
print("========================")
n=3
output=[x[i:i + n] for i in range(0, len(x), n)]
print(output)
print(type(output))
print(len(output))
print("========================")


# pattern = re.compile(r'(?P<item>\w+):(?P<item_count>\d+):(?P<item_price>\d+)') # 尋找規則
# result_finditer = re.findall(pattern, x)
# print(result_finditer)
# print(type(result_finditer))
# print("list", result_finditer)
# print("========================")
print('品項 :', (output[0])[0])
print('數量 :', (output[0])[1])
print('金額 :', (output[0])[2])

print('品項 :', (output[1])[0])
print('數量 :', (output[1])[1])
print('金額 :', (output[1])[2])

for i in range(0, len(output)):
    # print('品項: ', (output[i])[0], sep="", end=" ")
    # print('數量: ', (output[i])[1], sep="", end=" ")
    # print('金額: ', (output[i])[2])
    item=((output[i])[0])
    item_quantity=((output[i])[1])
    items_pritce=((output[i])[2])
    # print("品項: "f'{item}')
    # print(f"品項: {item} 數量: {item_quantity} 金額: {items_pritce}")
    str2 = f"品項: {item} 數量: {item_quantity} 金額: {items_pritce}"
    print(str2)
    # print(len(str2))

