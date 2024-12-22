import streamlit as st
from tensorflow import keras
import numpy as np

# Load model
model = keras.models.load_model('/kaggle/input/nmist_model/tensorflow2/default/1/nn_mnist.keras')

# Hàm tiền xử lý văn bản
def preprocess_text(text):
  # Thay thế các ký tự đặc biệt bằng dấu cách
  text = text.replace("<br />", " ")
  text = ''.join([c if c.isalnum() or c.isspace() else ' ' for c in text])
  # Chuyển về chữ thường
  text = text.lower()
  # Tách từ
  words = text.split()
  # Giới hạn độ dài câu
  max_length = 256  # Giả sử model được huấn luyện với max_length = 256
  if len(words) > max_length:
    words = words[:max_length]
  return " ".join(words)

# Giao diện Streamlit
st.title("Bài tập 6")
st.header("Nhận dạng cảm xúc từ câu bình luận phim")

comment = st.text_area("Nhập câu bình luận phim:")

if st.button("Dự đoán"):
  if comment:
    # Tiền xử lý văn bản
    processed_comment = preprocess_text(comment)

    # Tokenize và padding
    tokenizer = keras.preprocessing.text.Tokenizer(num_words=10000, oov_token='<OOV>')
    tokenizer.fit_on_texts([processed_comment])
    sequences = tokenizer.texts_to_sequences([processed_comment])
    padded_sequences = keras.preprocessing.sequence.pad_sequences(sequences, maxlen=256, padding='post', truncating='post')

    # Dự đoán
    prediction = model.predict(padded_sequences)
    label = "Tích cực" if prediction[0][0] > 0.5 else "Tiêu cực"
    st.write(f"Cảm xúc dự đoán: {label}")
  else:
    st.write("Vui lòng nhập câu bình luận phim.")