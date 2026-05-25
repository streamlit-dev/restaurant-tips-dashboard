import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Tips Dashboard", layout="wide")
st.title("Restaurant Tips Analysis Dashboard 💰")

@st.cache_data
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

df = load_data()

col1, col2, col3 = st.columns(3)
col1.metric("Avg Tip", f"${df['tip'].mean():.2f}")
col2.metric("Avg Total Bill", f"${df['total_bill'].mean():.2f}")
col3.metric("Total Records", len(df))

day = st.sidebar.selectbox("Filter by Day", df['day'].unique())
filtered_df = df[df['day'] == day]

fig1 = px.scatter(filtered_df, x="total_bill", y="tip", color="sex", 
                  title=f"Total Bill vs Tip on {day}")
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.bar(filtered_df, x="time", y="tip", color="smoker",
              title="Tips by Lunch/Dinner")
st.plotly_chart(fig2, use_container_width=True)
