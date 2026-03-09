
# Telecom X - Customer Churn Analysis

## Project Overview

Telecom X is facing a high rate of customer churn (service cancellation). Customer churn can significantly impact company revenue and growth. Understanding the factors that lead customers to leave the service is essential for improving retention strategies.

The objective of this project is to analyze customer data to identify patterns and factors associated with churn using Python and data analysis techniques.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter / Google Colab

---

## Dataset

The dataset was obtained from a public API and contains information about Telecom X customers, including:

- Customer demographic information
- Services contracted
- Billing details
- Customer churn status

API source:

https://github.com/ingridcristh/challenge2-data-science-LATAM

---

## Project Steps

### 1. Data Extraction
The dataset was imported from a JSON API and converted into a pandas DataFrame.

### 2. Data Transformation
Nested JSON structures were normalized to create a structured dataset suitable for analysis.

### 3. Data Cleaning
Data quality was verified by checking:

- Missing values
- Duplicate records
- Data types

The column containing total charges was converted to numeric format, and missing values were handled.

### 4. Feature Engineering
A new variable called **Cuentas_Diarias** was created based on monthly charges to estimate the daily cost of the service.

### 5. Exploratory Data Analysis (EDA)
Several visualizations were created to explore customer behavior and identify factors related to churn, including:

- Churn distribution
- Churn by contract type
- Churn by internet service
- Churn by payment method
- Churn analysis using numerical variables such as tenure and monthly charges

---

## Key Insights

The exploratory analysis revealed several important patterns:

- Customers with **month-to-month contracts** show higher churn rates.
- Customers with **shorter tenure** are more likely to cancel their services.
- Higher **monthly charges** may be associated with increased churn.
- Certain payment methods appear to correlate with higher churn rates.

---

## Recommendations

Based on the analysis, Telecom X could consider the following strategies to reduce churn:

- Encourage customers to adopt long-term contracts.
- Improve the onboarding experience for new customers.
- Monitor customers with higher monthly charges more closely.
- Develop predictive models to identify customers at risk of churn.

---

## Future Work

Future improvements for this project could include:

- Building a **machine learning model to predict churn**
- Performing **customer segmentation**
- Implementing **predictive analytics for retention strategies**

---

## Author

Lissett Zúñiga Reyes  
Computer Engineering | Data Science Learner
