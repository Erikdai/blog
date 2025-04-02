import streamlit as st
import streamlit.components.v1 as components

st.title("出海智能助手 Demo")

# 替换为你自己 Coze Bot 的 Web 公共链接
iframe_url = "https://www.coze.cn/space/7488599222121086985/bot/7488600231509131318"  # 你的 Coze 应用网页地址

components.iframe(iframe_url, height=600, scrolling=True)
