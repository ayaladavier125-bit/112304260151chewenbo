import pandas as pd
import numpy as np
import re
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import roc_auc_score
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

def clean_review(raw_review):
    review_text = BeautifulSoup(raw_review, "html.parser").get_text()
    review_text = re.sub(r'https?://\S+|www\.\S+', ' ', review_text)
    review_text = re.sub(r'\S+@\S+', ' ', review_text)
    review_text = re.sub(r"n't", " not", review_text)
    review_text = re.sub(r"'s", " ", review_text)
    letters_only = re.sub("[^a-zA-Z]", " ", review_text)
    words = letters_only.lower().split()
    return " ".join(words)

print("加载数据...")
train = pd.read_csv("labeledTrainData.tsv/labeledTrainData.tsv", header=0, delimiter="\t", quoting=3)
test = pd.read_csv("testData.tsv/testData.tsv", header=0, delimiter="\t", quoting=3)

print("清洗训练集文本...")
train['clean_review'] = train['review'].apply(clean_review)

print("清洗测试集文本...")
test['clean_review'] = test['review'].apply(clean_review)

print("TF-IDF 向量化 (使用 unigram, bigram, trigram)...")
vectorizer = TfidfVectorizer(
    max_features=80000,
    ngram_range=(1, 3),
    sublinear_tf=True,
    stop_words='english',
    min_df=3,
    max_df=0.95,
    use_idf=True,
    smooth_idf=True
)

X_train = vectorizer.fit_transform(train['clean_review'])
X_test = vectorizer.transform(test['clean_review'])
y_train = train['sentiment']

print("划分验证集...")
X_tr, X_val, y_tr, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

print("网格搜索调参...")
param_grid = {
    'C': [1, 2, 5, 10, 20],
    'penalty': ['l1', 'l2']
}
grid_search = GridSearchCV(
    LogisticRegression(solver='liblinear', max_iter=1000),
    param_grid,
    cv=5,
    scoring='roc_auc',
    n_jobs=-1,
    verbose=1
)
grid_search.fit(X_tr, y_tr)

print(f"最佳参数: {grid_search.best_params_}")
print(f"交叉验证最佳得分: {grid_search.best_score_:.5f}")

best_model = grid_search.best_estimator_
val_preds = best_model.predict_proba(X_val)[:, 1]
print(f"验证集 ROC AUC: {roc_auc_score(y_val, val_preds):.5f}")

print("使用全量数据训练最终模型...")
final_model = LogisticRegression(
    C=grid_search.best_params_['C'],
    penalty=grid_search.best_params_['penalty'],
    solver='liblinear',
    max_iter=1000
)
final_model.fit(X_train, y_train)

print("预测测试集...")
predictions = final_model.predict_proba(X_test)[:, 1]

output = pd.DataFrame(data={"id": test["id"], "sentiment": predictions})
output.to_csv("submission.csv", index=False, quoting=3)
print("优化完成！结果已保存至 'submission.csv'")