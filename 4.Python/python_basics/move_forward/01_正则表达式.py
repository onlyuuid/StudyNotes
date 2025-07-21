"""
正则表达式
"""
import re

pattern = r"^(1[3-9])\d{9}$"

def validate_phone_number(phone_number):
    res = re.match(pattern, phone_number)
    if res:
        return res
    else:
        return res

phone_list = ["13989562356","12256895623"," 15088555555"]
# for phone_number in phone_list:
#     result = validate_phone_number(phone_number)
#     print(result)

result = re.match(pattern, "15589562356")
obj = result.group(1)
print(obj)