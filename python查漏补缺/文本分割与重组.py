# 用户输入清洗：拆分并检查每个词汇
user_input = "点击链接 http://malicious.com 领取比特币"
words = user_input.split() # 默认按空格进行切割了
print(words) #['点击链接', 'http://malicious.com', '领取比特币']

# 重组安全文本（替换危险域名）
safe_words = [w if "malicious" not in w else "链接已屏蔽" for w in words]
safe_text = " ".join(safe_words)
print(safe_text)