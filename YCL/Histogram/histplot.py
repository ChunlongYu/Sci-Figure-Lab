#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 14 23:08:17 2025

@author: chunlongyu
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# 设置样式（可选）
sns.set_style("white")  # 选项: "white", "dark", "whitegrid", "darkgrid", "ticks"

# 加载数据集
penguins = sns.load_dataset("penguins")   #sns中自带数据集

# 创建图形并设置图像参数
fig = plt.figure(figsize=(10, 6), dpi=100, facecolor='w')  # 白色背景

# 绘图
ax = sns.histplot(
    data=penguins,
    x="flipper_length_mm"
    #bins=20,              # 显式指定直方图箱数
    #kde=False,            # 关闭核密度估计
    #color="steelblue",    # 自定义颜色
    #edgecolor="black"     # 设置柱子边缘颜色
)

# 设置标题和标签（可选）
ax.set_title("Distribution of Flipper Length (mm)", fontsize=16)
ax.set_xlabel("Flipper Length (mm)", fontsize=14)
ax.set_ylabel("Count", fontsize=14)

# 美化刻度（可选）
ax.tick_params(axis='both', labelsize=12)

# 保存图像为 PDF
plt.savefig('Seaborn_histplot.png', dpi=300, bbox_inches='tight') #保存图片为dpi=300的png
plt.savefig('Seaborn_histplot.pdf', bbox_inches='tight', format='pdf') #保存为pdf矢量图

# 显示图像
plt.show()