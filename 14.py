# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:39:46 2019

@author: 南陌欢少
"""

import math
# display模块可以决定显示的内容以何种格式显示
from IPython import display
# matplotlib为python的2D绘图库
# cm为颜色映射表
from matplotlib import cm  
# 使用 GridSpec 自定义子图位置
from matplotlib import gridspec
# pyplot提供了和matlab类似的绘图API，方便用户快速绘制2D图表
from matplotlib import pyplot as plt
# numpy为python的科学计算包，提供了许多高级的数值编程工具
import numpy as np    
# pandas是基于numpy的数据分析包，是为了解决数据分析任务而创建的    
import pandas as pd     
# sklearn(scikit-_learn_)是一个机器学习算法库,包含了许多种机器学习得方式
# *   Classification 分类
# *   Regression 回归
# *   Clustering 非监督分类
# *   Dimensionality reduction 数据降维
# *   Model Selection 模型选择
# *   Preprocessing 数据预处理 
# metrics:度量（字面意思），它提供了很多模块可以为第三方库或者应用提供辅助统计信息
from sklearn import metrics
# tensorflow是谷歌的机器学习框架
import tensorflow as tf   
# Dataset无比强大得数据集
from tensorflow.python.data import Dataset

tf.logging.set_verbosity(tf.logging.ERROR)
# 为了观察数据方便，最多只显示10行数据
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format