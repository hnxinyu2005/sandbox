"""
import csv

hero_names = [
    "安琪拉", "亚瑟", "项羽", "妲己", "嬴政", "孙尚香", "鲁班七号",
    "庄周", "刘禅", "高渐离", "阿轲", "钟无艳", "孙膑", "扁鹊",
    "白起", "芈月", "吕布", "周瑜", "元歌", "狄仁杰", "达摩",
    "典韦", "曹操", "宫本武藏", "李白", "马可波罗", "武则天",
    "司马懿", "老夫子", "关羽", "貂蝉", "程咬金", "露娜",
    "姜子牙", "李元芳", "刘邦", "韩信", "兰陵王", "王昭君",
    "杨戬", "女娲", "哪吒", "蔡文姬", "太乙真人", "干将莫邪",
    "鬼谷子", "东皇太一", "百里守约", "百里玄策", "弈星",
    "伽罗", "盾山", "沈梦溪", "李信", "上官婉儿", "瑶",
    "云中君", "曜", "镜", "澜", "夏洛特", "司空震"
]

# CSV 写入 hero
with open("data.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0]
new_rows = [header]

for name in hero_names:
    new_rows.append([name, "", "", ""])

with open("data.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerows(new_rows)
"""

import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
# 方法1：使用系统自带的中文字体（Windows通常有）
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号


# 数据准备
awards = ['一等奖', '二等奖', '三等奖', '四等奖', '五等奖', '六等奖', '七等奖']
avg_multipliers = [2.25, 3.89, 3.83, 2.96, 1.99, 1.34, 1.00]  # 两日平均倍率

# 突出显示的中间奖项（二、三、四等奖）
highlight_indices = [1, 2, 3]
highlight_color = '#FF6B6B'  # 醒目的红色
normal_color = '#4ECDC4'  # 常规颜色

# 创建颜色列表
colors = [highlight_color if i in highlight_indices else normal_color
          for i in range(len(awards))]

# 创建图形
plt.figure(figsize=(12, 7), facecolor='#F8F9FA')

# 绘制条形图
bars = plt.bar(awards, avg_multipliers, color=colors, edgecolor='black',
               linewidth=1.2, width=0.7, alpha=0.9)

# 添加数据标签
for bar, value in zip(bars, avg_multipliers):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.05,
             f'{value:.2f}倍', ha='center', va='bottom',
             fontsize=11, fontweight='bold')

# 突出显示中间奖项区域
plt.axvspan(0.5, 3.5, alpha=0.1, color='red', label='异常凸起区域')

# 设置标题和标签
plt.title('《小王送福运动会》真实中奖倍率异常分布\n',
          fontsize=18, fontweight='bold', pad=20)
plt.xlabel('奖项等级', fontsize=14, fontweight='semibold')
plt.ylabel('真实人数 / 理论期望人数（倍率）', fontsize=14, fontweight='semibold')

# 设置y轴范围，为顶部标签留出空间
plt.ylim(0, max(avg_multipliers) * 1.15)

# 添加网格线
plt.grid(axis='y', alpha=0.3, linestyle='--')

# 添加注释说明
plt.text(3.5, 3.5, '中间奖项异常凸起\n（二等奖、三等奖、四等奖）',
         fontsize=12, fontweight='bold',
         ha='center', va='center',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.3))

# 添加底部说明
plt.figtext(0.5, 0.01,
            '数据来源：真实人数为王者荣耀官方公示，理论模型假设为等概率随机开奖，基于2月12-13日的数据计算',
            ha='center', fontsize=9, style='italic', color='#666666')

# 调整布局
plt.tight_layout(rect=[0, 0.05, 1, 0.95])

# 保存图表（如果需要）
plt.savefig('小王送福_倍率分析.png', dpi=300, bbox_inches='tight')

# 显示图表
plt.show()