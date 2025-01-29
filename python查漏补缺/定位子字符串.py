import re
# 高效关键词检测
# 检测隐私信息泄露
text = "我的身份证号码是110101199003077654"
sensitive_pattern = ["身份证号", "手机号", "银行卡号"]

for pattern in sensitive_pattern:
    if text.find(pattern) != -1: # 返回-1表示未找到
        print(f"警告：检测到{pattern}字段！") # -> 警告：检测到身份证号字段！

# 与正则表达式配合使用
if text.find("身份证号") != -1:
    id_card = re.search(r"\d{17}[\dXx]", text) # 查找身份证号 (没找到返回0)
    if id_card:
        print(f"发现身份证号：{id_card.group()}")