import streamlit as st

st.title("Certificates 📜")

# 手动加载每张图片
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
    {"path": "pages/cert10.png", "caption": "Certificate 10"},
    {"path": "pages/cert11.png", "caption": "Certificate 11"},
    {"path": "pages/cert12.png", "caption": "Certificate 12"},
    {"path": "pages/cert13.png", "caption": "Certificate 13"},
    {"path": "pages/cert14.png", "caption": "Certificate 14"},
]

for cert in certificates:
    st.subheader(cert["caption"])
    st.image(cert["path"], caption=cert["caption"], use_column_width=True)
    st.divider()
