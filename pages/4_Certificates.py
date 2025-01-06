import streamlit as st

st.title("Certificates📜")
st.divider()

# 自定义证书名字、图片路径以及图片标题
certificates = [
    {"path": "pages/cert1.png", "text": "Certificate 1: My First Certificate of Excellence", "caption": "Certificate 1"},
    {"path": "pages/cert2.png", "text": "Certificate 2: Data Science Bootcamp Completion", "caption": "Certificate 2"},
    {"path": "pages/cert3.png", "text": "Certificate 3: Machine Learning Specialist", "caption": "Certificate 3"},
    {"path": "pages/cert4.png", "text": "Certificate 4: Advanced Python Programming", "caption": "Certificate 4"},
    {"path": "pages/cert5.png", "text": "Certificate 5: AI Fundamentals Certification", "caption": "Certificate 5"},
    {"path": "pages/cert6.png", "text": "Certificate 6: Big Data Analytics Award", "caption": "Certificate 6"},
    {"path": "pages/cert7.png", "text": "Certificate 7: Cloud Computing Essentials", "caption": "Certificate 7"},
    {"path": "pages/cert8.png", "text": "Certificate 8: Cybersecurity Fundamentals", "caption": "Certificate 8"},
    {"path": "pages/cert9.png", "text": "Certificate 9: Deep Learning Engineer", "caption": "Certificate 9"},
    {"path": "pages/cert10.jpg", "text": "Certificate 10: Full Stack Development Bootcamp", "caption": "Certificate 10"},
    {"path": "pages/cert11.jpg", "text": "Certificate 11: Natural Language Processing Pro", "caption": "Certificate 11"},
    {"path": "pages/cert12.jpg", "text": "Certificate 12: Web Development Certification", "caption": "Certificate 12"},
    {"path": "pages/cert13.jpg", "text": "Certificate 13: Blockchain Developer", "caption": "Certificate 13"},
    {"path": "pages/cert14.jpg", "text": "Certificate 14: Project Management Professional", "caption": "Certificate 14"},
]

# 遍历每张证书并显示
for cert in certificates:
    col1, col2 = st.columns([1, 2])  # 定义左右两列

    # 左列：显示自定义 Markdown 文本，并加大字体
    with col1:
        st.markdown(
            f"<div style='font-size: 20px; font-weight: bold;'>{cert['text']}</div>",
            unsafe_allow_html=True
        )

    # 右列：显示证书图片并添加标题
    with col2:
        st.image(cert["path"], caption=cert["caption"], use_container_width=True)  # 显示证书图片及其标题

    st.divider()  # 每个证书之间添加分割线
