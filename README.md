# 机器学习实验：基于 TF-IDF 的情感预测

## 1. 学生信息

- **姓名**：车文博
- **学号**：112304260151
- **班级**：数据1231

> 注意：姓名和学号必须填写，否则本次实验提交无效。

***

## 2. 实验任务

本实验基于给定文本数据，使用 **TF-IDF 向量化** 将文本转为向量特征，再结合 **逻辑回归分类模型** 完成情感预测任务，并将结果提交到 Kaggle 平台进行评分。

本实验重点包括：

- 文本预处理（HTML标签移除、特殊字符处理、文本清洗）
- TF-IDF 特征提取（unigram、bigram、trigram）
- 模型超参数调优（网格搜索 GridSearchCV）
- 分类模型训练与预测
- Kaggle 结果提交与分析

***

## 3. 比赛与提交信息

- **比赛名称**：Bag of Words Meets Bags of Popcorn
- **比赛链接**：https://www.kaggle.com/c/word2vec-nlp-tutorial
- **提交日期**：2026-05-17
- **GitHub 仓库地址**：https://github.com/ayaladavier125-bit/112304260151chewenbo
- **GitHub README 地址**：https://github.com/ayaladavier125-bit/112304260151chewenbo/blob/main/README.md

> 注意：GitHub 仓库首页或 README 页面中，必须能看到"姓名 + 学号"，否则无效。

***

## 4. Kaggle 成绩

请填写你最终提交到 Kaggle 的结果：

- **Public Score**：待提交后填写
- **Private Score**（如有）：待提交后填写
- **排名**（如能看到可填写）：待填写

***

## 5. Kaggle 截图

请在下方插入 Kaggle 提交结果截图，要求能清楚看到分数信息。

![Kaggle截图](./images/kaggle_score.png)

> 建议将截图保存在 `images` 文件夹中。\
> 截图文件名示例：`2023123456_张三_kaggle_score.png`

***

## 6. 实验方法说明

### （1）文本预处理

请说明你对文本做了哪些处理，例如：

- 分词
- 去停用词
- 去除标点或特殊符号
- 转小写

**我的做法：**\
本实验对文本进行了以下预处理操作：
1. 使用 BeautifulSoup 移除 HTML 标签
2. 使用正则表达式移除网址链接（`https?://\S+` 和 `www\.\S+`）
3. 使用正则表达式移除邮箱地址（`\S+@\S+`）
4. 处理否定词，将 `n't` 转换为 ` not`，保留语义信息
5. 移除所有格符号 `'s`
6. 移除非字母字符，仅保留英文字母
7. 转换为小写并分词
8. 重组为字符串供 TF-IDF 处理

***

### （2）TF-IDF 特征表示

请说明你如何使用 TF-IDF，例如：

- 特征数量设置
- ngram 范围设置
- TF-IDF 参数配置

**我的做法：**\
本实验使用 TF-IDF 向量化方法将文本转换为数值特征：
- **特征数量**：80,000 个最大特征（优化版本）/ 50,000 个（基础版本）
- **N-gram 范围**：(1, 3) 即 unigram、bigram 和 trigram（优化版本）/ (1, 2)（基础版本）
- **sublinear_tf**：设置为 True，降低高频词的权重干扰
- **stop_words**：使用英语停用词
- **min_df**：3，忽略出现次数少于3的词
- **max_df**：0.95，忽略出现频率超过95%的词
- **use_idf** 和 **smooth_idf**：启用 IDF 平滑处理

***

### （3）分类模型

请说明你使用了什么分类模型，例如：

- Logistic Regression
- Random Forest
- SVM
- XGBoost

并说明最终采用了哪一个模型。

**我的做法：**\
本实验使用 **Logistic Regression（逻辑回归）** 作为分类模型，原因如下：
1. 对于文本分类任务，逻辑回归具有较好的可解释性和稳定性
2. 结合 L1/L2 正则化可以有效防止过拟合
3. 使用 `liblinear` 求解器，支持 L1 和 L2 正则化
4. 通过网格搜索自动选择最佳的正则化参数 C 和 penalty 类型

最终模型参数通过 GridSearchCV 5折交叉验证确定：
- 正则化参数 C：搜索范围 [1, 2, 5, 10, 20]
- 正则化类型：L1 或 L2

***

## 7. 实验流程

请简要说明你的实验流程。

**我的实验流程：**

1. **加载数据**：读取训练集 `labeledTrainData.tsv` 和测试集 `testData.tsv`
2. **文本预处理**：
   - 使用 BeautifulSoup 移除 HTML 标签
   - 使用正则表达式移除网址和邮箱
   - 处理否定词（`n't` → `not`）
   - 移除非字母字符，转小写
3. **TF-IDF 向量化**：
   - 配置特征数量、N-gram 范围、停用词等参数
   - 在训练集上 fit_transform，在测试集上 transform
4. **划分验证集**：将训练集划分为 80% 训练和 20% 验证
5. **网格搜索调参**：使用 GridSearchCV 5折交叉验证寻找最佳超参数
6. **模型训练**：
   - 使用最佳参数在验证集上训练
   - 使用全量训练数据训练最终模型
7. **预测与提交**：在测试集上预测，生成 submission.csv
8. **提交 Kaggle**：将预测结果提交到 Kaggle 平台评分

***

## 8. 文件说明

请说明仓库中各文件或文件夹的作用。

**我的项目结构：**

```text
project/
├─ data/                    # 存放原始数据文件
│   └─ (数据文件在压缩包外层目录)
├─ src/                     # 存放源代码
│   ├─ sentiment_analysis.py          # 优化版情感分析代码（TF-IDF + GridSearchCV）
│   └─ sentiment_analysis_basic.py    # 基础版情感分析代码
├─ notebooks/               # 存放实验 notebook（如有）
├─ images/                  # 存放 README 中使用的图片
│   └─ kaggle_score.png      # Kaggle 提交结果截图
├─ submission/              # 存放提交文件
│   └─ submission.csv         # Kaggle 提交文件
└─ README.md                 # 项目说明文档
```

**各文件/文件夹详细说明：**

- `data/`：数据文件夹，存放实验使用的训练集和测试集 TSV 文件
- `src/sentiment_analysis.py`：优化版本的情感分析代码，包含完整的文本清洗、TF-IDF 向量化（80,000特征、trigram）、网格搜索调参、模型训练和预测流程
- `src/sentiment_analysis_basic.py`：基础版本的情感分析代码，包含基本的文本清洗和 TF-IDF 向量化（50,000特征、bigram）
- `notebooks/`：Jupyter notebook 文件夹，用于存放交互式实验代码
- `images/`：图片文件夹，存放 README 文档中引用的图片，如 Kaggle 截图
- `submission/submission.csv`：Kaggle 竞赛提交文件，包含测试集评论的情感预测概率
- `README.md`：项目说明文档，包含学生信息、实验任务、方法说明、实验流程等

***

## 9. 实验结果

### 本地验证结果

- **验证集 ROC AUC 分数**：约 0.97+

### 优化措施

1. **文本预处理优化**：
   - 移除 HTML 标签、网址、邮箱
   - 处理否定词保留语义信息
   - 移除所有格符号

2. **TF-IDF 参数优化**：
   - 增加特征数量到 80,000
   - 扩展 N-gram 范围到 (1, 3)
   - 添加 min_df 和 max_df 过滤极端词频

3. **模型调优**：
   - 使用 GridSearchCV 进行5折交叉验证
   - 自动搜索最佳正则化参数 C 和 penalty 类型

***

## 10. 依赖环境

```
pandas
numpy
re
beautifulsoup4 (bs4)
scikit-learn (sklearn)
```

安装命令：
```bash
pip install pandas numpy beautifulsoup4 scikit-learn
```

***

## 11. 运行说明

1. 确保数据文件 `labeledTrainData.tsv` 和 `testData.tsv` 位于正确路径
2. 运行优化版本：
   ```bash
   python src/sentiment_analysis.py
   ```
3. 运行基础版本：
   ```bash
   python src/sentiment_analysis_basic.py
   ```
4. 生成的 `submission.csv` 文件位于项目根目录，可直接提交到 Kaggle

***

> **作者**：车文博 \
> **学号**：112304260151 \
> **班级**：数据1231 \
> **日期**：2026-04-29