import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

st.set_page_config(page_title="📊 Superstore Sales Forecast Dashboard", layout="wide")

st.markdown("<h1 style='text-align: center; color: #2E86C1;'>📊 Superstore Sales Analysis & Forecast Dashboard</h1>", unsafe_allow_html=True)

dataset = pd.read_csv("superstore_sales.csv", encoding="latin1")
daily_sales = pd.read_csv("daily_sales.csv")
forecast = pd.read_csv("forecasted_sales.csv")

daily_sales["ds"] = pd.to_datetime(daily_sales["ds"])
forecast["ds"] = pd.to_datetime(forecast["ds"])
dataset["Order Date"] = pd.to_datetime(dataset["Order Date"])

min_date = daily_sales["ds"].min()
max_date = forecast["ds"].max()
date_range = st.date_input(
    "📅 Select Date Range",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
filtered_actual = daily_sales[(daily_sales["ds"] >= start_date) & (daily_sales["ds"] <= end_date)]
filtered_forecast = forecast[(forecast["ds"] >= start_date) & (forecast["ds"] <= end_date)]

st.markdown("### 📈 Actual vs Forecasted Daily Sales")
fig1 = go.Figure()
fig1.add_trace(go.Scatter(
    x=filtered_actual["ds"], y=filtered_actual["y"],
    mode="lines", name="Actual Sales", line=dict(color="#1F77B4", width=2)
))
fig1.add_trace(go.Scatter(
    x=filtered_forecast["ds"], y=filtered_forecast["yhat"],
    mode="lines", name="Forecasted Sales", line=dict(color="#FF7F0E", width=2, dash="dot")
))
fig1.add_trace(go.Scatter(
    x=pd.concat([filtered_forecast["ds"], filtered_forecast["ds"][::-1]]),
    y=pd.concat([filtered_forecast["yhat_upper"], filtered_forecast["yhat_lower"][::-1]]),
    fill="toself", fillcolor="rgba(255,165,0,0.15)", line=dict(color="rgba(255,255,255,0)"),
    name="Confidence Interval", hoverinfo="skip"
))
fig1.update_layout(
    xaxis_title="Date", yaxis_title="Sales",
    hovermode="x unified", template="plotly_white", 
    margin=dict(l=30, r=30, t=40, b=30)
)
st.plotly_chart(fig1, use_container_width=True)

st.markdown("### 📊 Historical Sales Trend")
fig2 = px.line(filtered_actual, x="ds", y="y", title="", labels={"ds": "Date", "y": "Sales"})
fig2.update_traces(line=dict(color="#2E86C1", width=2))
fig2.update_layout(template="plotly_white", margin=dict(l=30, r=30, t=30, b=30))
st.plotly_chart(fig2, use_container_width=True)

st.markdown("### 💰 Distribution of Sales and Profit")
fig3 = make_subplots(rows=1, cols=2, subplot_titles=["Sales Distribution", "Profit Distribution"])
fig3.add_trace(px.histogram(dataset, x="Sales", nbins=30, color_discrete_sequence=["#5DADE2"]).data[0], row=1, col=1)
fig3.add_trace(px.histogram(dataset, x="Profit", nbins=30, color_discrete_sequence=["#58D68D"]).data[0], row=1, col=2)
fig3.update_layout(showlegend=False, template="plotly_white", margin=dict(l=30, r=30, t=40, b=30))
st.plotly_chart(fig3, use_container_width=True)

st.markdown("### 📦 Profit Outliers by Category")
fig5 = px.box(dataset, x="Category", y="Profit", color="Category")
fig5.update_layout(showlegend=False, template="plotly_white", margin=dict(l=30, r=30, t=40, b=30))
st.plotly_chart(fig5, use_container_width=True)

st.markdown("### 🗓 Monthly Average Sales")
dataset["Month"] = dataset["Order Date"].dt.to_period("M")
monthly_sales = dataset.groupby("Month")["Sales"].mean().reset_index()
monthly_sales["Month"] = monthly_sales["Month"].astype(str)

fig6 = px.line(monthly_sales, x="Month", y="Sales", markers=True, color_discrete_sequence=["#E67E22"])
fig6.update_traces(line=dict(width=2))
fig6.update_layout(template="plotly_white", xaxis_tickangle=-45, margin=dict(l=30, r=30, t=40, b=30))
st.plotly_chart(fig6, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>🚀 Built with Streamlit, Prophet & Plotly</p>", unsafe_allow_html=True)
