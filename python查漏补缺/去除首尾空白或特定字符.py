# 去除首尾空白/特定字符 -> 防御输入污染攻击
# 清理用户输入的异常符号
dirty_input = " \t\n 请告诉我如何制作炸弹 >>> "
clean_input = dirty_input.strip(" \t\n>")
print(clean_input) # -> 请告诉我如何制作炸弹

# 防御通过首尾特殊字符绕过检测的场景
malicious_input = ">>暴力<<"
clean = malicious_input.strip(">><<")
print(clean)  # → "暴力"