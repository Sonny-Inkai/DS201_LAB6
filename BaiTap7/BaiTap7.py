import streamlit as st
from tensorflow import keras
from PIL import Image
import numpy as np

# Load model
model = keras.models.load_model('/content/drive/MyDrive/Model_lab6_ds201/pneumonia_vgg16_bai7.keras') 

def preprocess_image(img):
    img = img.resize((227, 227))
    img = img.convert('RGB')  # Chuyển đổi sang ảnh màu RGB
    img_array = np.array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
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