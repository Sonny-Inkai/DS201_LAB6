import streamlit as st

st.title("Bài tập 2")
st.header("Tính toán hai số thực")

# Nhập hai số thực
num1 = st.number_input("Nhập số thứ nhất:", value=0.0)
num2 = st.number_input("Nhập số thứ hai:", value=0.0)

# Tính toán
tong = num1 + num2
hieu = num1 - num2
tich = num1 * num2
if num2 != 0:
    thuong = num1 / num2
else:
    thuong = "Không thể chia cho 0"

# Hiển thị kết quả
st.subheader("Kết quả:")
st.write(f"Tổng: {tong}")
st.write(f"Hiệu: {hieu}")
st.write(f"Tích: {tich}")
st.write(f"Thương: {thuong}")