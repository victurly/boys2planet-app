import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# โหลดข้อมูล
@st.cache_data
def load_data():
    df = pd.read_csv("scores.csv")
    return df

df = load_data()

# หัวเรื่องเว็บ
st.title("📊 วิเคราะห์คะแนนผู้เข้าแข่งขัน Boys2Planet")

# ตัวเลือกผู้เข้าแข่งขัน
contestants = df['name'].unique()
selected = st.sidebar.selectbox("เลือกผู้เข้าแข่งขัน", contestants)

# แสดงตารางคะแนน
filtered = df[df['name'] == selected]
st.subheader(f"คะแนนของ {selected}")
st.dataframe(filtered, use_container_width=True)

# วาดกราฟคะแนนรายสัปดาห์
st.subheader(f"กราฟคะแนนของ {selected} ตามสัปดาห์")
fig, ax = plt.subplots()
ax.plot(filtered['week'], filtered['score'], marker='o', color='skyblue', linewidth=2)
ax.set_xlabel("สัปดาห์")
ax.set_ylabel("คะแนน")
ax.set_title(f"แนวโน้มคะแนนของ {selected}")
st.pyplot(fig)

# วิเคราะห์เพิ่ม
st.markdown("### สรุปคะแนน")
st.write(f"คะแนนเฉลี่ย: **{filtered['score'].mean():.2f}**")
st.write(f"คะแนนสูงสุด: **{filtered['score'].max()}**")
st.write(f"คะแนนต่ำสุด: **{filtered['score'].min()}**")
