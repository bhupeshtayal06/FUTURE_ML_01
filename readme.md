# 📊 Superstore Sales Forecast & Analysis Dashboard

An interactive **Streamlit dashboard** to analyze historical sales, detect outliers, and **forecast future daily sales** using **Prophet** and **Plotly**.

---

## ✨ Features
- ✅ **Sales Forecasting** with Prophet (including holiday effects)  
- ✅ **Actual vs Forecasted Sales** with confidence intervals  
- ✅ **Interactive Date Range Filters**  
- ✅ **Sales & Profit Distribution** charts  
- ✅ **Category & Sub-category Analysis**  
- ✅ **Profit Outlier Detection** (boxplots)  
- ✅ **Monthly Average Sales Trend**  
- ✅ **Modern UI** powered by Streamlit + Plotly  

---

## 🛠 Tech Stack
- **Python**  
- **Streamlit** (dashboard)  
- **Prophet** (time series forecasting)  
- **Plotly & Plotly Express** (interactive charts)  
- **Pandas** (data wrangling)  

---

## 📂 Project Structure
```
├── app.py                  # Streamlit app
├── code.ipynb
├── daily_sales.csv         # Daily aggregated sales data
├── forecasted_sales.csv    # Prophet model forecast output
├── superstore_sales.csv    # Original raw dataset
└── README.md
```
## 📊 Dashboard Views
- **Actual vs Forecasted Sales** with confidence intervals  
- **Historical Sales Trends** (time series, zoomable)  
- **Sales & Profit Distributions** (histograms, density plots)  
- **Profit Outliers by Category/Sub-category** (boxplots)  
- **Monthly Average Sales Trends** (bar/line)  
- **Category & Sub-category Breakdown** (bar/treemap)  
- **Interactive Date Filters** applied across all views  
## 🧩 Workflow
1. **Data Loading** → Load `superstore_sales.csv` (raw) or `daily_sales.csv` (aggregated).  
2. **Preprocessing** → Parse dates, handle missing values, aggregate to daily totals if required.  
3. **Model Training** → Fit Prophet model with:
   - `ds` = Date  
   - `y` = Sales  
   - Optional **holidays & seasonalities**  
4. **Forecast Generation** → Predict future sales for N days (30/60/90).  
5. **Visualization** → Display results using interactive Plotly charts inside Streamlit.  
6. **Exploration** → Drill down by categories, analyze profit outliers, and view distributions.  
## ✅ Future Enhancements
- Add **Prophet hyperparameter controls** (seasonality, changepoints, holidays).  
- Integrate **cross-validation metrics** (MAE, RMSE, MAPE) inside the dashboard.  
- Support **multi-store / regional filters** for broader analysis.  
- Add **forecast components plot** (trend, seasonality, holiday effects).  
- Implement **anomaly detection** (STL decomposition, Z-score, Isolation Forest).  
- Enable **user uploads** of their own sales CSVs for forecasting.  
- Export **forecast results to CSV/Excel** directly from the app.  

## 📷 Screenshots / Visualizations
Here are some of the interactive charts & insights included in the dashboard:

### 📈 Actual vs Forecasted Daily Sales
![Actual vs Forecasted Daily Sales](assets/Actual_vs_Forecasted_Daily_Sales.png)

### 📉 Historical Sales Trend
![Historical Sales Trend](assets/Historical_Sales_Trend.png)

### 📊 Sales & Profit Distribution
![Sales & Profit Distribution](assets/Sales_Profit_Distribution.png)

### 📦 Profit Outliers by Category
![Profit Outliers by Category](assets/Profit_Outliers_by_Category.png)

### 📅 Monthly Average Sales
![Monthly Average Sales](assets/Monthly_Average_Sales.png)
