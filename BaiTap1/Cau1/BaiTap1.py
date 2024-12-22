import streamlit as st
import random

# Danh sách các từ và nghĩa của chúng
words = {
    "example": "a thing characteristic of its kind or illustrating a general rule",
    "python": "a large heavy-bodied nonvenomous snake occurring throughout the Old World tropics",
    "machine": "an apparatus using or applying mechanical power and having several parts, each with a definite function and together performing a particular task",
    "learning": "the acquisition of knowledge or skills through study, experience, or being taught"
}

def get_random_word():
  """Trả về một từ ngẫu nhiên và nghĩa của nó."""
  word = random.choice(list(words.keys()))
  meaning = words[word]
  return word, meaning

st.title("Câu 1")
st.header("Random Words Generator")

# Hiển thị từ ngẫu nhiên
if "word" not in st.session_state:
  st.session_state.word, st.session_state.meaning = get_random_word()

st.subheader("Random Word")
st.write(st.session_state.word)

st.write("Meaning: ", st.session_state.meaning)

# Nút "Generate"
if st.button("Generate"):
  st.session_state.word, st.session_state.meaning = get_random_word()
  st.rerun()  # Chạy lại ứng dụng để cập nhật giao diện