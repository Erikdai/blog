import streamlit as st

st.title("Certificates 📜")
st.divider()

# 自定义证书名字和图片路径（Markdown 文本）
certificates = [
    {"path": "pages/cert1.png", "text": "**Certificate 1**: My First Certificate of Excellence"},
    {"path": "pages/cert2.png", "text": "**Certificate 2**: Data Science Bootcamp Completion"},
    {"path": "pages/cert3.png", "text": "**Certificate 3**: Machine Learning Specialist"},
    {"path": "pages/cert4.png", "text": "**Certificate 4**: Advanced Python Programming"},
    {"path": "pages/cert5.png", "text": "**Certificate 5**: AI Fundamentals Certification"},
    {"path": "pages/cert6.png", "text": "**Certificate 6**: Big Data Analytics Award"},
    {"path": "pages/cert7.png", "text": "**Certificate 7**: Cloud Computing Essentials"},
    {"path": "pages/cert8.png", "text": "**Certificate 8**: Cybersecurity Fundamentals"},
    {"path": "pages/cert9.png", "text": "**Certificate 9**: Deep Learning Engineer"},
    {"path": "pages/cert10.jpg", "text": "**Certificate 10**: Full Stack Development Bootcamp"},
    {"path": "pages/cert11.jpg", "text": "**Certificate 11**: Natural Language Processing Pro"},
    {"path": "pages/cert12.jpg", "text": "**Certificate 12**: Web Development Certification"},
    {"path": "pages/cert13.jpg", "text": "**Certificate 13**: Blockchain Developer"},
    {"path": "pages/cert14.jpg", "text": "**Certificate 14**: Project Management Professional"},
]

# 遍历每张证书并显示
for cert in certificates:
    col1, col2 = st.columns([1, 2])  # 定义左右两列

    # 左列：显示自定义 Markdown 文本
    with col1:
        st.markdown(cert["text"])  # 使用 Markdown 文本自定义内容

    # 右列：显示证书图片
    with col2:
        st.image(cert["path"], use_container_width=True)  # 显示证书图片

    st.divider()  # 每个证书之间添加分割线
