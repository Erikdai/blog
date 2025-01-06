import streamlit as st

st.title("Certificates 📜")
st.divider()

# 手动加载每张图片及其初始文字
certificates = [
    {"path": "pages/cert1.png", "caption": "Certificate 1"},
    {"path": "pages/cert2.png", "caption": "Certificate 2"},
    {"path": "pages/cert3.png", "caption": "Certificate 3"},
    {"path": "pages/cert4.png", "caption": "Certificate 4"},
    {"path": "pages/cert5.png", "caption": "Certificate 5"},
    {"path": "pages/cert6.png", "caption": "Certificate 6"},
    {"path": "pages/cert7.png", "caption": "Certificate 7"},
    {"path": "pages/cert8.png", "caption": "Certificate 8"},
    {"path": "pages/cert9.png", "caption": "Certificate 9"},
    {"path": "pages/cert10.jpg", "caption": "Certificate 10"},
    {"path": "pages/cert11.jpg", "caption": "Certificate 11"},
    {"path": "pages/cert12.jpg", "caption": "Certificate 12"},
    {"path": "pages/cert13.jpg", "caption": "Certificate 13"},
    {"path": "pages/cert14.jpg", "caption": "Certificate 14"},
]

# 遍历每张证书
for idx, cert in enumerate(certificates):
    col1, col2 = st.columns([1, 2])  # 定义左右两列

    # 左列：显示并可编辑证书名字
    with col1:
        new_caption = st.text_area(f"Edit Certificate Name {idx + 1}", cert["caption"], key=f"cert_{idx}")
        cert["caption"] = new_caption  # 更新证书名字

    # 右列：显示证书图片
    with col2:
        st.image(cert["path"], caption=cert["caption"], use_container_width=True)

    st.divider()  # 每个证书之间添加分割线
