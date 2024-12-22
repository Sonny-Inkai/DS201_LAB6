import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Câu 4")
st.header("My first deployed DL model")

st.subheader("Header đây chứ đâu")

st.write("Đây là text")

st.markdown("Markdown đây anh em ơi")

st.latex(r''' a + b = 3''')


st.code('''def hello():
    print("Hello world!")''')

st.subheader("Hiển thị luôn cả chart")

# Tạo dữ liệu mẫu cho biểu đồ
df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

# Vẽ biểu đồ line
st.line_chart(df)