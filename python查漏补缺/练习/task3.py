import re

def create_mixed_pattern(keyword):
    # 检测全角符号与半角符号混合使用的敏感词（如"色　情"）
    symbols = r'[^\u4e00-\u9FFF]*'  # 匹配任何非中文的字符（包括零个）
    return symbols.join(re.escape(c) for c in keyword)

def detect_obfuscated_words(text, sensitive_words):
    detected = []
    for word in sensitive_words:
        pattern = re.compile(create_mixed_pattern(word), flags=re.UNICODE)
        if pattern.search(text):
            detected.append(word)
    return detected

# 验证测试案例
test_cases = [
    ("色情信息", ["色情"]),       # 直接匹配
    ("色 情内容", ["色情"]),      # 半角空格
    ("色　情视频", ["色情"]),     # 全角空格
    ("色！＠情", ["色情"]),       # 全角符号
    ("冰毒交易", ["冰毒"]),       # 无分隔符
    ("正规色情用品", ["色情"]),   # 直接匹配
    ("色_情", ["色情"])          # 下划线
]

sensitive_words = ["色情", "冰毒"]
for text, expected in test_cases:
    result = detect_obfuscated_words(text, sensitive_words)
    print(f"输入：{text}")
    print(f"预期：{expected} → 实际：{result}\n")