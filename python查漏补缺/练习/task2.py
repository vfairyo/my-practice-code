import re

def replace_phone_number(text: str) -> str:
    """将包含手机号的文本替换为[隐私信息已屏蔽]"""
    pattern = r'(?<!\d)1[3-9]\d{9}(?!\d)' # 匹配11位手机号的正则表达式
    replaced_text = re.sub(pattern,'[隐私信息已屏蔽]', text)
    return replaced_text

# 测试示例
text = "我的一个手机号码是13912345678"
print(replace_phone_number(text)) 