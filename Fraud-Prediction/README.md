
# 🕵️‍♂️ Fraud Detection Project

## 📊 Overview

This project aims to build a predictive model for detecting fraudulent transactions using a dataset with **150,000 records** and **20 features**. The main objective is to **minimize fraud** and **maximize company profits**, even if it means being slightly more conservative in approvals.

---

## 🧾 Dataset Summary

* **Rows:** 150,000
* **Columns:** 20

### 📘 Data Dictionary

| Column Name                          | Type         | Description                                           |
| ------------------------------------ | ------------ | ----------------------------------------------------- |
| `score_1` to `score_10`              | Numeric      | Various evaluation scores (e.g., risk, quality)       |
| `country`                            | Text         | Country related to the purchase                       |
| `product`                            | Text         | Product name/code (excluded due to high cardinality)  |
| `product_category`                   | Text         | Product category                                      |
| `doc_delivery_1` to `doc_delivery_3` | Binary (0/1) | Indicators if documents were delivered                |
| `purchase_date`                      | Date         | Date of the transaction (excluded from model)         |
| `purchase_value`                     | Numeric      | Transaction amount                                    |
| `fraud_score_model`                  | Numeric      | Score from baseline fraud model (excluded from model) |
| `fraud`                              | Binary       | Fraud flag (target variable)                          |

---

## 🔍 Data Analysis Highlights

* **Country:** 90% of transactions come from Brazil and Argentina → grouped into *Brazil*, *Argentina*, and *Others*.
* **Product:** High cardinality (over 8,000 products); excluded from the model.
* **Product Category:** Kept only the top categories that concentrate \~80% of frauds; remaining grouped as "Others".
* **Document Delivery:** Transactions with `doc_delivery_1 = 1` show different fraud rates.
* **Scores:** `score_9`, `score_10`, `score_4`, `score_7`, `score_2`, `score_6`, and `score_3` were the most predictive.

---

## 🧠 Feature Engineering

* Grouped `country` into 3 categories.
* Reduced `product_category` to top 1,000 categories using **target encoding**.
* Null values filled using **median from training data**.
* Created `entrega_doc_2_nan` flag to capture nulls explicitly.
* Replaced nulls in `doc_delivery_2` with `0`.
* Created `hora_da_compra` to reflect fraud pattern by time of day.
* Applied **One-Hot Encoding** to other categorical variables.

---

## 🧪 Models Tested

* Logistic Regression (with class weight and undersampling)
* Decision Tree (with class weight and undersampling)
* Random Forest (with class weight and undersampling)
* XGBoost (with class weight)
* KNN and Naive Bayes

---

## 🏆 Best Model: Decision Tree

**Best Hyperparameters:**

```json
{
  "criterion": "gini",
  "max_depth": 5,
  "min_samples_split": 2,
  "min_samples_leaf": 1
}
```

**Evaluation Metrics:**

| Metric       | Value  |
| ------------ | ------ |
| AUC (Train)  | 0.8323 |
| AUC (Test)   | 0.8252 |
| KS Statistic | 0.5203 |
| KS P-Value   | 0.0000 |
| Precision    | 0.1394 |
| Recall       | 0.7713 |
| Accuracy     | 0.75   |

**Classification Report:**

```
              precision    recall  f1-score   support
           0       0.98      0.75      0.85     42735
           1       0.14      0.77      0.24      2265
```

---

## 🎯 Decision Threshold

* The **optimal threshold** for maximum profit is **0.47**.
* Fraud rate reduced from **3% to <2%**.
* Approval rate adjusted to **72%**.
* Result: +10% increase in profit compared to the previous model.

---

## ✅ Final Takeaways

* The model successfully **identifies frauds** with good precision and high recall.
* Strategic feature selection and encoding were essential to balance bias/variance.
* **Time-based and document submission features** proved highly valuable.
* Model provides a **practical improvement** over the baseline, justifying deployment.

---

## 🚀 Next Steps

* Modularizing code and deploy
* Monitor concept drift and retrain periodically
* Incorporate feedback loop for continuous learning

---

