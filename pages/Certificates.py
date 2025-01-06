import streamlit as st

st.title("Certificates 📜")
st.divider()

# 自定义证书名字和图片路径
certificates = [
    {"path": "pages/cert1.png", "caption": "My First Certificate of Excellence"},
    {"path": "pages/cert2.png", "caption": "Data Science Bootcamp Completion"},
    {"path": "pages/cert3.png", "caption": "Machine Learning Specialist"},
    {"path": "pages/cert4.png", "caption": "Advanced Python Programming"},
    {"path": "pages/cert5.png", "caption": "AI Fundamentals Certification"},
    {"path": "pages/cert6.png", "caption": "Big Data Analytics Award"},
    {"path": "pages/cert7.png", "caption": "Cloud Computing Essentials"},
    {"path": "pages/cert8.png", "caption": "Cybersecurity Fundamentals"},
    {"path": "pages/cert9.png", "caption": "Deep Learning Engineer"},
    {"path": "pages/cert10.jpg", "caption": "Full Stack Development Bootcamp"},
    {"path": "pages/cert11.jpg", "caption": "Natural Language Processing Pro"},
    {"path": "pages/cert12.jpg", "caption": "Web Development Certification"},
    {"path": "pages/cert13.jpg", "caption": "Blockchain Developer"},
    {"path": "pages/cert14.jpg", "caption": "Project Management Professional"},
]

# 遍历每张证书并显示
for cert in certificates:
    col1, col2 = st.columns([1, 2])  # 定义左右两列

    # 左列：显示证书名字
    with col1:
        st.subheader(cert["caption"])  # 左侧显示自定义的证书名字

    # 右列：显示证书图片
    with col2:
        st.image(cert["path"], caption=cert["caption"], use_container_width=True)

    st.divider()  # 每个证书之间添加分割线
