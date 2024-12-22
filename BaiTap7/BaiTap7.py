import streamlit as st
from tensorflow import keras
from PIL import Image
import numpy as np

# Load model
model = keras.models.load_model('pneumonia_vgg16.keras') 

# Hàm tiền xử lý ảnh
def preprocess_image(img):
    img = img.resize((227, 227))  # Resize ảnh về kích thước mà mô hình yêu cầu
    img_array = np.array(img)
    img_array = img_array / 255.0  # Chuẩn hóa giá trị pixel về khoảng [0, 1]
    img_array = np.expand_dims(img_array, axis=0)  # Thêm chiều batch
    return img_array

# Giao diện Streamlit
st.title("Bài tập 7")
st.header("Nhận diện bệnh viêm phổi từ ảnh X-Quang")

uploaded_file = st.file_uploader("Chọn ảnh X-Quang", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Hiển thị ảnh đã tải lên
    image = Image.open(uploaded_file)
    st.image(image, caption='Ảnh X-Quang')

    # Tiền xử lý ảnh
    processed_image = preprocess_image(image)

    # Dự đoán
    prediction = model.predict(processed_image)
    label = "Bệnh" if prediction[0][0] > 0.5 else "Bình thường" 
    st.write(f"Kết quả dự đoán: {label}")