import re


x=":2:2:1:野川蛋黃派10粒:1:65:可口可樂1250CC:1:38"
# x="*:1:1:1:95無鉛汽油:47.301:28.6"
# content = '''email:123456@163.com
# email:234567@163.com
# email:345678@163.com
# '''
pattern = re.compile(r'(?P<item>\w+):(?P<item_count>\d+):(?P<item_price>\d+)')
# pattern = re.search(r'(?P<item>\w+):(?P<item_count>\d+):(?P<item_price>\d+)')
result_finditer = re.findall(pattern, x)
print(type(result_finditer))
print("list", result_finditer)
print(result_finditer)
print('品項 :', (result_finditer[1])[0])
print('數量 :', (result_finditer[1])[1])
print('金額 :', (result_finditer[1])[2])

for i in range(1, len(result_finditer)):
    print('品項: ', (result_finditer[i])[0], sep="", end=" ")
    print('數量: ', (result_finditer[i])[1], sep="", end=" ")
    print('金額: ', (result_finditer[i])[2])
    item=((result_finditer[i])[0])
    item_quantity=((result_finditer[i])[1])
    items_pritce=((result_finditer[i])[2])
    # print("品項: "f'{item}')
    # print(f"品項: {item} 數量: {item_quantity} 金額: {items_pritce}")
    str2 = f"品項: {item} 數量: {item_quantity} 金額: {items_pritce}"
    print(str2)
    print(len(str2))

