def satety_check(text: str) -> dict:
    """综合安全检测函数"""
    report = {
        "has_sensitve": False,
        "link_count": 0,
        "shouting" : False
    }

    # 检测敏感词（需实际扩展词库）
    sensitive_words = ["暴力", "色情", "诈骗"]
    for word in sensitive_words:
        if text.find(word) != -1:
            report["has_sensitve"] = True

    # 统计链接数量
    report["link_count"] = text.count("http://") + text.count("https://")

    # 检测全大写喊叫式内容
    if len(text) > 10 and text.upper() == text:
        report["shouting"] = True
    
    return report

# 测试输出
text_text = "点击HTTPS://MALICIOUS.COM 领取免费暴力武器！！！"
print(satety_check(text_text))
# -> {'has_sensitve': True, 'link_count': 0, 'shouting': True}

# 中英文混合处理方式
text = "推荐VPN服务(科学上网)"
# 同时检测中英文关键词
if text.find("VPN") != -1 or text.find("科学上网") != -1:
    print("检测到违规网络服务")
