import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dữ liệu mẫu
data = {
    'sentence': [
        'slide giáo trình đầy đủ',
        'nhiệt tình giảng dạy, gần gũi với sinh viên.',
        'đi học đầy đủ full điểm chuyên cần',
        'thầy áp dụng công nghệ thông tin và các thiết bị hỗ trợ cho việc giảng dạy',
        'chưa thấy bài hay, có nhiều bài tập ví dụ ngay trên lớp,',
        'giảng viên đảm bảo thời gian lên lớp, tích cực trả lời câu hỏi của sinh viên, thường xuyên',
        'em sẽ nó môn này, nhưng em sẽ học lại ở các học kỳ kế tiếp.',
        'thời lượng học quá dài, không đảm bảo tiếp thu hiệu quả',
        'nội dung màn học có phần thiếu trọng tâm, hầu như là chung chung, khái quát khiới',
        'cần nói rõ hơn bằng cách trình bày lên táng thay vì nhìn vào slide'
    ],
    'label': [2, 2, 2, 0, 0, 2, 1, 0, 0, 0],
    'label_word': ['Positive', 'Positive', 'Positive', 'Negative', 'Negative', 'Positive', 'Neutral', 'Negative', 'Negative', 'Negative']
}
df = pd.DataFrame(data)

# Tạo DataFrame cho biểu đồ
chart_data = pd.DataFrame({'label_word': ['Positive', 'Negative', 'Neutral'], 'count': [2544, 2423, 214]})

st.title("Câu 3")
st.header("MÔ HÌNH PHÂN LOẠI CẢM XÚC TIẾNG VIỆT")

st.subheader("Bộ Dữ Liệu")
st.dataframe(df)


st.subheader("Chi Tiết Bộ Dữ Liệu")

# Tạo biểu đồ bằng matplotlib
fig, ax = plt.subplots()
ax.bar(chart_data['label_word'], chart_data['count'], color=['green', 'brown', 'khaki'])
plt.xlabel("label_word")
plt.ylabel("count")

# Hiển thị biểu đồ trong Streamlit
st.pyplot(fig)