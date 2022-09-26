# 正規表達式
import re

x="DF622694131110708397000000003000000030000000008547587XKsayZY706hvyFpe6k3TQ==:**********:2:2:1:野川蛋黃派10粒:1:65:可口可樂1250CC:1:38"

result = re.search("[a-zA-Z]{2}[0-9]{8}", x, flags=0)
print(result)
print(result.group())