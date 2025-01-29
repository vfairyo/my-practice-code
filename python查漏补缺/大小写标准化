# 构建统一的小写敏感词库
sensitive_words = {"hack", "drug", "weapon"}
user_input = "Learn How To HACK Systems"

# 统一转换为小写检测
lower_input = user_input.lower()
for word in lower_input.split():
    if word in sensitive_words:
        print(f"检测到敏感词：{word}") # -> 检测到敏感词：hack