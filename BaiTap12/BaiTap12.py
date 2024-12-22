import streamlit as st
from tensorflow import keras
from PIL import Image
import numpy as np

# Load model
model = keras.models.load_model('gender_mobilenetv2.keras')  # Thay 'gender_mobilenetv2.keras' bằng tên file model của bạn

def preprocess_image(img):
    img = img.resize((227, 227))
    img = img.convert('RGB')  # Chuyển đổi sang ảnh màu RGB
    img_array = np.array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Giao diện Streamlit
st.title("Bài tập 12")
st.header("Dự đoán giới tính từ ảnh chụp")

uploaded_file = st.file_uploader("Chọn ảnh chụp người", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Hiển thị ảnh đã tải lên
    image = Image.open(uploaded_file)
    st.image(image, caption='Ảnh đã tải lên')

    # Tiền xử lý ảnh
    processed_image = preprocess_image(image)

    # Dự đoán
    prediction = model.predict(processed_image)
    gender = "Male" if prediction[0][0] > 0.5 else "Female"  
    st.write(f"Giới tính dự đoán: {gender}")