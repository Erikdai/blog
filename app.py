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

    /* 动态获取 Streamlit 的主题颜色 */
    .sidebar-link {
        display: block;
        padding: 10px 15px;
        margin: 3px 0;
        font-size: 18px;
        color: var(--text-color); /* 动态文字颜色 */
        text-align: left;
        background-color: var(--background-color); /* 动态背景颜色 */
        border: none;
        border-radius: 5px;
    }

    .sidebar-link:hover {
        background-color: var(--secondary-background-color); /* 鼠标悬停时使用 Streamlit 次级背景色 */
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3); /* 鼠标悬停时添加高亮阴影 */
        cursor: pointer;
    }

    .active {
        background-color: var(--primary-color); /* 激活状态使用主题的主色调 */
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.divider()

# 侧边栏导航
with st.sidebar:
    st.header("Menu")

    pages = {
        "🏠 Home": "Home",
        "📚 Experience": "Experience",
        "📖 Publications": "Publications",
        "📜 Certificates": "Certificates",
        "🏆 Awards": "Awards",
        "📞 Contact": "Contact"
    }

    if "page" not in st.session_state:
        st.session_state.page = "Home"

    for page, module in pages.items():
        is_active = "active" if st.session_state.page == module else ""
        st.markdown(
            f'<div class="sidebar-link {is_active}" onclick="window.location=\'/{module.lower()}.py\';">{page}</div>',
            unsafe_allow_html=True
        )

# 页面内容（默认显示主页内容）
st.title("Home")
st.markdown('<div style="text-align: justify">你好！我是 [你的名字]，目前是一名软件开发工程师。在这里我将分享我的学习、生活和项目经验。</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify">我专注于开发高效的应用程序，热爱编程、阅读和探索新技术。欢迎大家交流合作！</div>', unsafe_allow_html=True)

# 底部声明
col6, col7, col8 = st.columns([1, 4, 1])
with col7:
    st.markdown('<div style="text-align: center;">I believe in: <span style="color: green; font-weight: bold;">"No dream is too big and no dreamer is too small"</span></div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;">_An effort by_: <span style="color: red;">**Your Name**</span></div>', unsafe_allow_html=True)
