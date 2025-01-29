# 识别高频风险行为
# 检测刷屏广告行为
user_history = [
    "点击链接领取优惠",
    "限时特价点击购买",
    "免费获取课程资料点击这里"
]

# 统计"点击"关键词出现频率
click_count = sum(sentence.count("点击") for sentence in user_history)
if click_count >= 3:
    print(f"触发广告刷屏检测（点击次数：{click_count}）") # -> 触发广告刷屏检测（点击次数：3）

# 检测恶意重复内容
spam_text = "代开发票 代开发票 代开发票"
if spam_text.count("代开发票") > 2:
    print("检测到重复广告信息")
    