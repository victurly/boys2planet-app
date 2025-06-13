import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# โหลดข้อมูล
@st.cache_data
def load_data():
    df = pd.read_csv('boys2planet_scores.csv')
    return df

df = load_data()

# แสดงหัวเว็บ
st.title('วิเคราะห์คะแนนผู้เข้าแข่งขัน Boys2Planet')

# ตัวเลือกผู้เข้าแข่งขันใน Sidebar
contestant = st.sidebar.selectbox('เลือกผู้เข้าแข่งขัน', df['name'].unique())

# กรองข้อมูลผู้เข้าแข่งขัน
df_contestant = df[df['name'] == contestant]

# แสดงข้อมูลคะแนน
st.write(f"คะแนนของ {contestant}")
st.dataframe(df_contestant)

# สร้างกราฟแสดงคะแนน
fig, ax = plt.subplots()
ax.plot(df_contestant['week'], df_contestant['score'], marker='o')
ax.set_xlabel('สัปดาห์')
ax.set_ylabel('คะแนน')
ax.set_title(f'คะแนนรายสัปดาห์ของ {contestant}')
st.pyplot(fig)
