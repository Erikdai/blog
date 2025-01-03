import streamlit as st
from PIL import Image

# 设置页面配置
st.set_page_config(
    page_title="个人博客",
    page_icon="📝",
    layout="wide",
)

# 添加顶部 Logo 和标题
st.image("https://via.placeholder.com/150", width=150)  # 替换为你的 Logo 图片链接
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
    .custom-text { font-family: 'Agdasima', sans-serif; font-size: 45px; color: cyan; }
    </style>
    <p class="custom-text">Welcome to My Personal Blog</p>
""", unsafe_allow_html=True)

st.divider()

# 布局部分
col1, col2 = st.columns([1, 5], gap="medium")
with col1:
    image = Image.open('your_image.jpg')  # 替换为你的头像图片路径
    st.image(image)

with col2:
    st.markdown('<div style="text-align: justify">你好！我是 [你的名字]，目前是一名软件开发工程师。在这里我将分享我的学习、生活和项目经验。</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify">我专注于开发高效的应用程序，热爱编程、阅读和探索新技术。欢迎大家交流合作！</div>', unsafe_allow_html=True)

st.divider()

# 关于我部分
st.subheader("关于我")
st.markdown('<div style="text-align: justify">我是 [你的名字]，在软件开发行业拥有丰富的经验，热衷于学习新技术和分享知识。</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify">除了编程，我喜欢阅读科幻小说、旅行和摄影，这些爱好让我保持创意和灵感。</div>', unsafe_allow_html=True)

# 侧边栏导航
with st.sidebar:
    st.header("导航")
    st.markdown("""
    - [主页](#)
    - [其他页面](#)
    - [联系我](#)
    """)

# 底部声明
col6, col7, col8 = st.columns([1, 4, 1])
with col7:
    st.markdown('<div style="text-align: center;">I believe in: <span style="color: green; font-weight: bold;">"No dream is too big and no dreamer is too small"</span></div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;">_An effort by_: <span style="color: red;">**Your Name**</span></div>', unsafe_allow_html=True)
