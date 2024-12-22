import streamlit as st

st.title("Câu 2")
st.header("Playground")

# Input prompt
input_prompt = st.text_area("Input prompt", height=100)

# Nút "Submit"
submit_button = st.button("Submit")

# Temperature
temperature = st.slider("Temperature", min_value=0.00, max_value=2.00, value=1.00, step=0.01)

# Top P
top_p = st.slider("Top P", min_value=0.00, max_value=1.00, value=1.00, step=0.01)

# Maximum length
max_length = st.slider("Maximum length", min_value=1, max_value=4000, value=1, step=1)

# Show probabilities
show_probabilities = st.checkbox("Show probabilities")

# Code mẫu
code_example = st.text_area("Code example", "print('Hello world')", height=100)