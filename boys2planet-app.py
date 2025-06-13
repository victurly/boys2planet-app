import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# โหลดข้อมูลจาก CSV
@st.cache_data
def load_data():
    return pd.read_csv("scores.csv")

df = load_data()

# หัวเว็บ
st.title("📊 วิเคราะห์คะแนนผู้เข้าแข่งขัน Boys2Planet")

# เลือกชื่อผู้เข้าแข่งขัน
contestant = st.sidebar.selectbox("เลือกผู้เข้าแข่งขัน", df["name"].unique())

# กรองข้อมูลเฉพาะคนนั้น
filtered = df[df["name"] == contestant]

# แสดงตารางคะแนน
st.subheader(f"คะแนนของ {contestant}")
st.dataframe(filtered)

# วาดกราฟ
st.subheader(f"กราฟคะแนนรายสัปดาห์ของ {contestant}")
fig, ax = plt.subplots()
ax.plot(filtered["week"], filtered["score"], marker="o", color="orange")
ax.set_xlabel("สัปดาห์")
ax.set_ylabel("คะแนน")
ax.set_title(f"คะแนนของ {contestant}")
st.pyplot(fig)
