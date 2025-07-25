# 🪔 Diwali Sales Analysis

This project is a comprehensive data analysis and visualization report on a Diwali Sales Dataset using Python. The goal is to extract business insights such as customer purchasing behavior, top-selling products, and revenue trends across different demographics and regions. The project includes data cleaning, preprocessing, exploratory data analysis (EDA), and dashboard-ready visualizations.

---

## 📁 Dataset

**File Name**: `Diwali Sales Data.csv`
**Source**: Internal project data
**Encoding Used**: `unicode_escape`
**Total Records**: \~11,000+

---

## 📌 Key Objectives

* Clean and preprocess raw sales data
* Analyze purchase patterns by gender, age, marital status, occupation, and product category
* Identify top-performing states and products
* Create visual insights for better business decision-making

---

## 🧰 Tools and Libraries Used

* `Pandas` – for data manipulation and cleaning
* `NumPy` – for numerical calculations
* `Matplotlib` – for custom plotting
* `Seaborn` – for attractive statistical visualizations

---

## 🧹 Data Cleaning Steps

* Removed unnecessary columns (`Status`, `unnamed1`)
* Checked for and dropped null values
* Converted data types for better analysis (e.g., `Amount` to `int`)
* Created categorical columns like `AgeGroup`

---

## 📊 Exploratory Data Analysis (EDA)

### 🎯 1. Gender Analysis

* **Finding**: Female buyers were more active and spent more during Diwali.

### 🎯 2. Age Group Distribution

* **Finding**: Majority of buyers fall in the **26-35** age group.
* Combined with gender, it was found that **females in 26-35** group made the most purchases.

### 🎯 3. State-Wise Analysis

* **Top States by Orders**: Uttar Pradesh, Maharashtra, Karnataka
* **Top States by Revenue**: Uttar Pradesh, Maharashtra

### 🎯 4. Marital Status

* **Finding**: Married individuals (especially women) had higher purchasing power.

### 🎯 5. Occupation

* **Finding**: IT professionals and healthcare workers were the most frequent buyers.

### 🎯 6. Product Category

* **Finding**: Top selling categories were **Food, Electronics, and Clothing**

### 🎯 7. Top-Selling Products

* Identified top 10 products by number of orders using `Product_ID`

---

## 📈 Dashboard Section

Visualizations created using `matplotlib` and `seaborn` can be exported and used in interactive dashboards (e.g., Power BI or Tableau). The EDA forms the basis for:

* **Sales Insights Dashboard**
* **Customer Segmentation Analysis**
* **Product Category Performance**

---

## 📌 Business Insights

* Focus marketing on **female customers aged 26-35**
* Invest more in **top-performing states** during Diwali campaigns
* Push **food and electronics** as key categories during seasonal promotions
* Personalized ads to **married professionals in IT and healthcare**

---

## ✅ Future Improvements

* Add time series analysis (if date column available)
* Integrate dashboards with interactive platforms (e.g., Power BI)
* Use ML models for customer segmentation or sales forecasting

---

Here’s the **conclusion** section you can add at the end of your README for the **Diwali Sales Analysis** project:

---

## 🧾 Conclusion

The **Diwali Sales Analysis** project successfully uncovered key business insights from customer sales data. Through detailed exploratory data analysis, we identified the following:

* **Female customers aged 26-35** were the most active and had the highest purchasing power.
* **Uttar Pradesh** and **Maharashtra** emerged as the top contributing states in both sales volume and revenue.
* **Married individuals**, especially women, played a significant role in overall sales.
* The **IT and Healthcare sectors** contributed the most in terms of occupation-based purchases.
* Product categories such as **Food, Electronics, and Clothing** dominated sales during the Diwali season.
* Top-selling products were identified to help focus inventory and marketing strategies.

This analysis provides valuable direction for **targeted marketing**, **inventory planning**, and **strategic sales campaigns** for future Diwali seasons or similar festive events. With further integration of time-series data and customer behavior prediction models, this project can evolve into a powerful decision-support tool for businesses.

---

## ✨ Author

**Priyanshu Ranjan**
B.Tech CSE | Vivekananda Global University

