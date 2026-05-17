import pandas as pd
import numpy as np
import re
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

print("正在加载数据...")
train = pd.read_csv("labeledTrainData.tsv", header=0, delimiter="\t", quoting=3)
test = pd.read_csv("testData.tsv", header=0, delimiter="\t", quoting=3)

def clean_review(raw_review):
    review_text = BeautifulSoup(raw_review, "html.parser").get_text()
    letters_only = re.sub("[^a-zA-Z]", " ", review_text)
    words = letters_only.lower().split()
    return " ".join(words)

print("正在清洗训练集文本...")
train['clean_review'] = train['review'].apply(clean_review)

print("正在清洗测试集文本...")
test['clean_review'] = test['review'].apply(clean_review)

print("正在进行 TF-IDF 向量化 (使用 unigram 和 bigram)...")
vectorizer = TfidfVectorizer(
    max_features=50000,
    ngram_range=(1, 2),
    sublinear_tf=True,
    stop_words='english'
)

X_train = vectorizer.fit_transform(train['clean_review'])
X_test = vectorizer.transform(test['clean_review'])
y_train = train['sentiment']

X_tr, X_val, y_tr, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
lr_val = LogisticRegression(C=2.0, solver='liblinear', max_iter=500)
lr_val.fit(X_tr, y_tr)

val_preds = lr_val.predict_proba(X_val)[:, 1]
print(f"本地验证集的 ROC AUC 分数: {roc_auc_score(y_val, val_preds):.5f}")

print("正在使用全量数据训练最终模型...")
model = LogisticRegression(C=2.0, solver='liblinear', max_iter=500)
model.fit(X_train, y_train)

print("正在预测测试集结果...")
predictions = model.predict_proba(X_test)[:, 1]

output = pd.DataFrame(data={"id": test["id"], "sentiment": predictions})
output.to_csv("submission.csv", index=False, quoting=3)
print("预测完成！结果已保存至 'submission.csv'")