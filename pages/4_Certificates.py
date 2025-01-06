import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Daicx669",
    page_icon="🚀",
    layout="wide",
)

st.title("Certificates📜")
st.divider()

# 自定义证书名字、图片路径以及图片标题
certificates = [
    {"path": "pages/cert1.png", "text": "Certificate 1: Large Language Model Development Engineer", "caption": "Certificate 1"},
    {"path": "pages/cert2.png", "text": "Certificate 2: Agent Engineer I", "caption": "Certificate 2"},
    {"path": "pages/cert3.png", "text": "Certificate 3: Agent Engineer II", "caption": "Certificate 3"},
    {"path": "pages/cert4.png", "text": "Certificate 4: AI Coding Engineer", "caption": "Certificate 4"},
    {"path": "pages/cert5.png", "text": "Certificate 5: Fine-tuning Engineer", "caption": "Certificate 5"},
    {"path": "pages/cert6.png", "text": "Certificate 6: LLM Engineer", "caption": "Certificate 6"},
    {"path": "pages/cert7.png", "text": "Certificate 7: Prompt Engineer", "caption": "Certificate 7"},
    {"path": "pages/cert8.png", "text": "Certificate 8: AI + Data Analytics Competency Certification Certificate", "caption": "Certificate 8"},
    {"path": "pages/cert9.png", "text": "Certificate 9: AI + Programming Competency Certificate", "caption": "Certificate 9"},
    {"path": "pages/cert10.jpg", "text": "Certificate 10: Tencent Cloud Developer Certification - Distributed Database TDSQL ( MySQL Edition)", "caption": "Certificate 10"},
    {"path": "pages/cert11.jpg", "text": "Certificate 11: Tencent Cloud Developer Certification - Cloud Server CVM Developer", "caption": "Certificate 11"},
    {"path": "pages/cert12.jpg", "text": "Certificate 12: Tencent Cloud Developer Certification - Keras-based Traffic Sign Recognition for AI Applications", "caption": "Certificate 12"},
    {"path": "pages/cert13.jpg", "text": "Certificate 13: Itronix Solutions - Artificial Intelligence Certificate", "caption": "Certificate 13"},
    {"path": "pages/cert14.jpg", "text": "Certificate 14: Itronix Solutions - Data Science Professional Certificate", "caption": "Certificate 14"},
    {"path": "pages/cert15.png", "text": "Certificate 15: AI for Product Management", "caption": "Certificate 15"},
]

# 遍历每张证书并显示
for cert in certificates:
    col1, col2 = st.columns([1, 2])  # 定义左右两列

    # 左列：显示自定义 Markdown 文本，并加大字体
    with col1:
        st.markdown(
            f"<div style='font-size: 25px; font-weight: bold;'>{cert['text']}</div>",
            unsafe_allow_html=True
        )

    # 右列：显示证书图片并添加标题
    with col2:
        st.image(cert["path"], caption=cert["caption"], use_container_width=True)  # 显示证书图片及其标题

    st.divider()  # 每个证书之间添加分割线
