import streamlit as st
# Set page configuration
st.set_page_config(
    page_title="Daicx670",
    page_icon="🚀",
    layout="wide",
)

st.title("Awards🏆")
st.divider()

# 自定义证书名字、图片路径以及图片标题
certificates = [
    {"path": "pages/RanDomSeed - LMSYS - Chatbot Arena Human Preference Predictions.png", "text": "Kaggle competition: LMSYS - Chatbot Arena Human Preference Predictions 🥈", "caption": "Award 1"},
    {"path": "pages/RanDomSeed - NeurIPS 2024 - Predict New Medicines with BELKA.png", "text": "Kaggle competition: RanDomSeed - NeurIPS 2024 - Predict New Medicines with BELKA 🥉", "caption": "Award 2"},
    {"path": "pages/RanDomSeed - Google - Fast or Slow_ Predict AI Model Runtime.png", "text": "Kaggle competition: RanDomSeed - Google - Fast or Slow Predict AI Model Runtimet 🥉", "caption": "Award 3"},
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
