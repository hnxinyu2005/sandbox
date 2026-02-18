import math

total = math.comb(36,7)
print(f"总组合数 = {total}\n")

# 固定参数
N = 36
K = 7
n = 7

# 计算中 k 个的概率
def prob_k(k):
    return math.comb(7, k) * math.comb(N - K, n - k) / total

for k in range(0, 8):
    p = prob_k(k)
    print(f"p(中{k}个) = {p:.6%}")
print()

p_7th = prob_k(1) # 七等奖概率
real_7th_12 = 19947058  # 2月12日七等奖人数
real_7th_13 = 28661965
real_7th_14 = 32371733
real_7th_15 = 39908004
real_7th_16 = 39794271
real_7th_17 = 38689753
real_7th_18 = 36392314

# 理论期望人数
total_12 = real_7th_12 / p_7th  # 2月12日总参与人数
total_13 = real_7th_13 / p_7th  # 2月13日总参与人数
total_14 = real_7th_14 / p_7th
total_15 = real_7th_15 / p_7th
total_16 = real_7th_16 / p_7th
total_17 = real_7th_17 / p_7th
total_18 = real_7th_18 / p_7th

print(f"2月12日反推总参与人数: {total_12:,.0f} 人")
print(f"2月13日反推总参与人数: {total_13:,.0f} 人")
print(f"2月14日反推总参与人数: {total_14:,.0f} 人")
print(f"2月15日反推总参与人数: {total_15:,.0f} 人")
print(f"2月16日反推总参与人数: {total_16:,.0f} 人")
print(f"2月17日反推总参与人数: {total_17:,.0f} 人")
print(f"2月18日反推总参与人数: {total_18:,.0f} 人")

# 奖项与命中个数k的对应关系
award_k_mapping = {
    "一等奖": 7,
    "二等奖": 6,
    "三等奖": 5,
    "四等奖": 4,
    "五等奖": 3,
    "六等奖": 2,
    "七等奖": 1,
    "未中奖": 0
}

# 计算单天的理论期望人数
def calculate_theoretical_expectation(total_participants):
    theoretical_expectation = {}
    for award, k in award_k_mapping.items():
        p = prob_k(k)  # 该奖项对应的理论概率
        expectation = total_participants * p  # 期望人数 = 总人数 × 概率
        theoretical_expectation[award] = expectation
    return theoretical_expectation

# 计算两天的理论期望人数
theo_exp_12 = calculate_theoretical_expectation(total_12)
theo_exp_13 = calculate_theoretical_expectation(total_13)
theo_exp_14 = calculate_theoretical_expectation(total_14)
theo_exp_15 = calculate_theoretical_expectation(total_15)
theo_exp_16 = calculate_theoretical_expectation(total_16)
theo_exp_17 = calculate_theoretical_expectation(total_17)
theo_exp_18 = calculate_theoretical_expectation(total_18)

# 整理理论期望人数字典（方便后续计算）
theo_awards = {
    "2月12日": theo_exp_12,
    "2月13日": theo_exp_13,
    "2月14日": theo_exp_14,
    "2月15日": theo_exp_15,
    "2月16日": theo_exp_16,
    "2月17日": theo_exp_17,
    "2月18日": theo_exp_18
}

print("2月12日各奖项理论期望人数：")
for award, exp in theo_exp_12.items():
    print(f"{award}: {exp:,.0f} 人")

print("2月13日各奖项理论期望人数：")
for award, exp in theo_exp_13.items():
    print(f"{award}: {exp:,.0f} 人")

print("2月14日各奖项理论期望人数：")
for award, exp in theo_exp_14.items():
    print(f"{award}: {exp:,.0f} 人")

print("2月15日各奖项理论期望人数：")
for award, exp in theo_exp_15.items():
    print(f"{award}: {exp:,.0f} 人")

print("2月16日各奖项理论期望人数：")
for award, exp in theo_exp_16.items():
    print(f"{award}: {exp:,.0f} 人")

print("2月17日各奖项理论期望人数：")
for award, exp in theo_exp_17.items():
    print(f"{award}: {exp:,.0f} 人")

print("2月18日各奖项理论期望人数：")
for award, exp in theo_exp_18.items():
    print(f"{award}: {exp:,.0f} 人")

# 新增：整理四天所有奖项的实际人数（对应表格数据）
real_awards = {
    "2月12日": {
        "一等奖": 17,
        "二等奖": 5955,
        "三等奖": 222605,
        "四等奖": 2288605,
        "五等奖": 9694748,
        "六等奖": 19739067,
        "七等奖": 19947058
    },
    "2月13日": {
        "一等奖": 15,
        "二等奖": 5041,
        "三等奖": 242278,
        "四等奖": 3233189,
        "五等奖": 14621737,
        "六等奖": 29226486,
        "七等奖": 28661965
    },
    "2月14日": {
        "一等奖": 15,
        "二等奖": 3594,
        "三等奖": 136364,
        "四等奖": 1876303,
        "五等奖": 11440380,
        "六等奖": 30168084,
        "七等奖": 32371733
    },
    "2月15日": {
        "一等奖": 15,
        "二等奖": 2597,
        "三等奖": 107899,
        "四等奖": 1636031,
        "五等奖": 10574080,
        "六等奖": 30940475,
        "七等奖": 39908004
    },
    "2月16日": {
        "一等奖": 17,
        "二等奖": 2758,
        "三等奖": 117766,
        "四等奖": 1823383,
        "五等奖": 11519801,
        "六等奖": 31397483,
        "七等奖": 39794271
    },
    "2月17日": {
        "一等奖": 16,
        "二等奖": 3538,
        "三等奖": 150738,
        "四等奖": 2058959,
        "五等奖": 11709488,
        "六等奖": 31308541,
        "七等奖": 38689753
    },
    "2月18日": {
        "一等奖": 17,
        "二等奖": 2524,
        "三等奖": 108141,
        "四等奖": 1656571,
        "五等奖": 10377541,
        "六等奖": 29366609,
        "七等奖": 36392314
    }
}

# 新增：计算并输出「实际人数 ÷ 理论期望人数」
print("\n实际人数 ÷ 理论期望人数")
for date in ["2月12日", "2月13日", "2月14日", "2月15日", "2月16日", "2月17日", "2月18日"]:
    print(f"\n{date}：")
    # 仅计算有实际数据的奖项（未中奖无实际数据，跳过）
    for award in ["一等奖", "二等奖", "三等奖", "四等奖", "五等奖", "六等奖", "七等奖"]:
        real_num = real_awards[date][award]
        theo_num = theo_awards[date][award]
        # 避免除以0，理论值为0时特殊处理
        if theo_num == 0:
            ratio = "无理论值（除数为0）"
        else:
            ratio = real_num / theo_num
            # 保留4位小数，方便查看
            ratio = round(ratio, 4)
        print(f"  {award}: 实际/理论 = {ratio}")