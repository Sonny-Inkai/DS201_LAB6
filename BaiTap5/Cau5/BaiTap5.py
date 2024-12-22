import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load model
model = tf.keras.models.load_model('C:\\Users\\GemiBook\\Downloads\\SONNY\\UIT_HK1_2024_2025\\DS201\\LAB6\\BaiTap5\\Cau5\\nn_mnist.keras')

# Hàm tiền xử lý ảnh
def preprocess_image(img):
  img = img.resize((28, 28))
  img = img.convert('L') 
  img_array = np.array(img)
  img_array = img_array.reshape(1, 28, 28, 1)
  img_array = img_array.astype('float32') / 255.0
  
  return img_array

# Giao diện Streamlit
st.title("Bài tập 5")
st.header("Nhận dạng ảnh chữ số viết tay")

uploaded_file = st.file_uploader("Chọn ảnh chữ số viết tay", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
  # Hiển thị ảnh đã tải lên
  image = Image.open(uploaded_file)
  st.image(image, caption='Ảnh đã tải lên')

  # Tiền xử lý ảnh
  processed_image = preprocess_image(image)

  # Dự đoán
  prediction = model.predict(processed_image).argmax()
  st.write(f"Kết quả dự đoán: {prediction}")