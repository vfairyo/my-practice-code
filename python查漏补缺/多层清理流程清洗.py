def clean_input(text: str) -> str:
    # 1. 去除首尾垃圾字符
    text = text.strip(' \t\n!@#$%^&*()_+')
    # 2. 统一小写
    text = text.lower()
    # 3. 替换混淆字符
    return text.replace("$", "s").replace("1", "i")

dirty_input = "!!!HACK1NG$"
print(clean_input(dirty_input))  # → hacking