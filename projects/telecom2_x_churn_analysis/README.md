
--- 

#  Telecom X - Customer Churn Exploratory Data Analysis (EDA)

The exploratory analysis focused on understanding the factors associated with customer churn.

Key steps included:

- Data extraction from JSON API
- Data cleaning and preprocessing
- Handling missing values
- Feature engineering
- Visualization of churn distribution
- Analysis of categorical and numerical variables

Main analyses performed:

- Churn distribution
- Churn by contract type
- Churn by internet service
- Churn by payment method
- Relationship between tenure and churn
- Relationship between total charges and churn

These analyses helped identify important patterns in customer behavior.

---

# Machine Learning Pipeline

The second part of the project focused on building predictive models to identify customers likely to churn.

Main steps included:

### Data Preparation
- Removing irrelevant variables such as customer ID
- Encoding categorical variables using **One-Hot Encoding**
- Checking class imbalance
- Applying **SMOTE** to balance the dataset (optional)
- Splitting the dataset into training and testing sets
- Applying **StandardScaler** when required

---

## Models Implemented

Two classification models were trained:

### Logistic Regression
- Requires feature scaling
- Provides interpretable coefficients
- Suitable for linear relationships

### Decision Tree
- Does not require normalization
- Captures nonlinear relationships
- Provides feature importance metrics

---

## Model Evaluation

The models were evaluated using several classification metrics:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

These metrics allowed comparison of model performance and assessment of how well each model predicts churn.

---

# Key Factors Influencing Churn

The analysis revealed several important variables influencing churn:

- Contract type
- Customer tenure
- Monthly charges
- Total charges
- Internet service features
- Payment method

Customers with **month-to-month contracts**, **shorter tenure**, and **higher monthly charges** show a higher probability of churn.

---

# Strategic Insights

The results indicate that churn is strongly associated with the early stages of the customer lifecycle and contract flexibility. Customers who recently joined the company and are on short-term contracts represent the highest churn risk.

---

# Recommendations

Based on the analysis, Telecom X could reduce churn by:

- Encouraging customers to switch to **long-term contracts**
- Improving the **onboarding experience for new customers**
- Monitoring customers with **higher monthly charges**
- Implementing **predictive churn monitoring systems**
- Creating targeted retention campaigns for high-risk customers

---

# Future Work

Possible improvements for this project include:

- Testing additional models such as **Random Forest, XGBoost, or SVM**
- Performing **hyperparameter tuning**
- Building a **customer churn prediction dashboard**
- Deploying the model for real-time churn prediction

---

# Author

**Lissett Zúñiga Reyes**  
Computer Engineering  
Data Science Learner
