def sensitive_count(text: str, sensitive: list) -> dict:
    """统计用户输入的每个敏感词出现次数"""
    # 字典推导式（Dictionary Comprehension）
    # {key_expression: value_expression for item in iterable}
    details = {word: text.count(word) for word in sensitive} 
    total = sum(details.values())
    return {
        "has_sensitive": total > 0,
        "count": total,
        "details": details
    }

sensitive_pattern = ["身份证号", "手机号", "银行卡号"]
test_text = "身份证号 420220213416464646464 身份证号 手机号 银行卡号 银行卡号 银行卡号"
print(sensitive_count(test_text, sensitive_pattern))