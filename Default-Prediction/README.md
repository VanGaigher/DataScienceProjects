
# Credit Risk Prediction

This project aims to develop a Machine Learning model to **predict the credit risk** of new customers, classifying them into two categories: **good payer (class: 0)** or **default (class: 1)**.

## The Challenge in the Financial Sector

In the financial sector, granting credit is fundamental to stimulating consumption and increasing company profits. However, this practice must be carefully balanced with the **mitigation of risks**, such as default and fraud. Credit analysis, robust security systems, and diversification of credit offerings are essential strategies to achieve this balance.

With technological advancements, the automation of these processes using **artificial intelligence and machine learning** allows for more accurate risk prediction, ensuring that credit is granted sustainably, benefiting both the customer and the institution.

## Model Objectives

Our model seeks to optimize credit risk prediction with a focus on the following objectives:

  * **Reduce the false positive rate**: Minimize cases where the customer is mistakenly classified as a defaulter but is actually a good payer.
  * **Decrease the false negative rate**: Reduce cases where the customer is mistakenly classified as a good payer when, in fact, they are a defaulter.

We prioritize the **reduction of false negatives** because the financial impact of a defaulting customer being classified as a good payer is more significant for companies.

## Dataset

The dataset used for model development contains the following columns:

  * `Idade` (Age): The customer's age.
  * `Renda` (Income): The customer's salary.
  * `Score`: A credit score based on features. Higher credit scores indicate a low risk of default.
  * `hist_inadim_meses` (Default History Months): Total months in default.
  * `valor_emprestimo` (Loan Amount): Amount of loan granted to the customer.
  * `relacao_dividarenda` (Debt-to-Income Ratio): Debt-to-income ratio.
  * `classe_emprego` (Employment Class): Type of employment.
  * `possui_imovel` (Has Property): Indicates if the customer owns properties.
  * `possui_veiculo` (Has Vehicle): Indicates if the customer has vehicles.
  * `inadimplente` (Default): Target variable (0 for good payer, 1 for defaulter).

### Exploratory Data Analysis (EDA)

  * Customers have diverse ages, ranging from 18 to 70 years old, with a standard deviation of 14.
  * Customer income also varies significantly, from $1,000 to almost $20,000.
  * **No strong correlations** were found between features, nor with the target variable.
  * A higher concentration of non-defaulting customers with high scores was observed, which is expected. However, some customers with high scores still defaulted, suggesting that `Score` alone is not the best predictor.
  * Non-defaulters tend to have a **lower debt-to-income ratio**. It's crucial to handle this feature carefully to avoid *data leakage*, considering it was collected **before** credit was granted.

### ANOVA Tests

ANOVA tests were conducted to check the relationship between some features and the score/months of default:

  * **`Income` vs `Score`**: $p\_value = 0.6257$. Failed to reject the null hypothesis; it's assumed that all salary ranges have the same average score.
  * **`Income` vs `Default History Months`**: $p\_value = 0.2174$. Failed to reject the null hypothesis; it's assumed that all salary ranges have the same average months of default.
  * **`Employment Class` vs `Score`**: $p\_value = 0.2540$. Failed to reject the null hypothesis; it's assumed that all employment types have the same average score.

### Pre-processing

For feature scaling, the **MinMax Scaler** was applied. This choice was made because the features do not follow a normal distribution, and the MinMax Scaler transforms the data to a scale between 0 and 1 while preserving the original distribution shape.

## Machine Learning Models

Two Machine Learning models were tested: Logistic Regression and a Tuned Decision Tree.

### Logistic Regression

| Metric            | Value      |
| :---------------- | :--------- |
| ROC-AUC           | 0.8676     |
| Accuracy          | 0.77       |
| Precision         | 0.6197     |
| Recall            | 0.6984     |

**Confusion Matrix:**

```
[[110  27]
 [ 19  44]]
```

**Classification Report:**

```
              precision    recall  f1-score   support

           0       0.85      0.80      0.83       137
           1       0.62      0.70      0.66        63

    accuracy                           0.77       200
   macro avg       0.74      0.75      0.74       200
weighted avg       0.78      0.77      0.77       200
```

### Decision Tree (Tuned)

| Metric            | Value      |
| :---------------- | :--------- |
| ROC-AUC           | 0.9983     |
| Accuracy          | 0.98       |
| Precision         | 0.9836     |
| Recall            | 0.9523     |

**Confusion Matrix:**

```
[[136   1]
 [  3  60]]
```

**Classification Report:**

```
              precision    recall  f1-score   support

           0       0.98      0.99      0.99       137
           1       0.98      0.95      0.97        63

    accuracy                           0.98       200
   macro avg       0.98      0.97      0.98       200
weighted avg       0.98      0.98      0.98       200
```

-----

## Conclusion: Best Model

Based on the evaluation metrics, the **Tuned Decision Tree model** clearly outperforms Logistic Regression for this credit risk prediction task.

The Decision Tree achieved significantly higher performance across all key metrics:

  * **ROC-AUC (0.9983 vs 0.8676)**: Indicates a much better ability to distinguish between good payers and defaulters.
  * **Accuracy (0.98 vs 0.77)**: Shows a higher percentage of correct predictions overall.
  * **Precision (0.9836 vs 0.6197)**: For class 1 (default), the Decision Tree is far more precise, meaning fewer false positives (customers predicted as defaulters who are actually good payers).
  * **Recall (0.9523 vs 0.6984)**: Crucially, for class 1 (default), the Decision Tree has a much higher recall, meaning it correctly identifies a significantly larger proportion of actual defaulters (fewer false negatives). This aligns directly with our primary objective of **decreasing the rate of false negatives** to mitigate financial impact on companies.

The **Confusion Matrix** for the Tuned Decision Tree also highlights its superiority: it made only **1 false positive** (predicting a good payer as a defaulter) and just **3 false negatives** (predicting a defaulter as a good payer). In contrast, the Logistic Regression model had 27 false positives and 19 false negatives.

Therefore, the **Tuned Decision Tree is the superior model** for this project, as it provides a much more accurate and reliable prediction of credit risk, especially in reducing costly false negatives for financial institutions.