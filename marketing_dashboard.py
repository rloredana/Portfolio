import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data for the dashboard
data = {
    'Metric': [
        'Page Views', 'Unique Visitors', 'Bounce Rate', 'New Leads', 'Conversion Rate',
        'Followers Growth', 'Engagement Rate', 'Open Rate', 'Click-Through Rate',
        'Impressions', 'Cost Per Click', 'Customer Acquisition Cost', 'Lifetime Value'
    ],
    'Current Value': [85000, 45000, 35, 900, 4.8, 4.5, 2.8, 22, 4.2, 450000, 1.2, 45, 480],
    'Goal': [100000, 50000, 40, 1000, 5, 5, 3, 25, 5, 500000, 1.0, 50, 500],
    'Trend': ['Up 5% MoM', 'Down 2% MoM', 'Improved', 'Up 10%', 'Stable', 'Up 4.5%', 'Needs Boost', 'Stable', 'Needs Review', 'Up 8%', 'Reduce Cost', 'Improved', 'On Track']
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Title of the dashboard
st.title("📊 Marketing Performance Dashboard")

# Metrics table
st.subheader("📋 Key Metrics Overview")
st.dataframe(df, use_container_width=True)

# Revenue Growth Chart Data
revenue_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Revenue Growth (%)': [70, 75, 80, 85, 90]
})

# Revenue Growth Line Chart
st.subheader("📈 Revenue Growth Over Time")
fig = px.line(revenue_data, x='Month', y='Revenue Growth (%)', title='Monthly Revenue Growth', markers=True)
fig.update_traces(line=dict(color='#4f46e5', width=3))
st.plotly_chart(fig, use_container_width=True)

# Visual Progress Bars for Goals
st.subheader("🎯 Goal Progress")
for index, row in df.iterrows():
    progress = (row['Current Value'] / row['Goal']) * 100 if row['Goal'] != 0 else 0
    st.write(f"**{row['Metric']}** ({row['Current Value']} / {row['Goal']}) - {row['Trend']}")
    st.progress(min(int(progress), 100))
