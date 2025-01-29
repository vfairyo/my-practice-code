text = "ChatGPT的回复需要安全审核"
# 不可变性（以下操作都会生成新字符串）
new_text = text.replace("安全", "内容安全") # 替换操作

# 索引与切片
print(text[0:7]) # ChatGPT
print(text[-4:]) # 安全审核

# 常用方法
print(text.startswith("Chat")) # 判断开头 -> True
print("审核" in text) # 成员检测 -> True