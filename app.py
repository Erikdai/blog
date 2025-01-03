# Streamlit博客应用代码
import streamlit as st

# 设置页面配置
st.set_page_config(
    page_title="个人博客",
    page_icon="📝",
    layout="wide",
)

# 页面标题
st.title("欢迎来到我的个人博客 📝")

# 简介
st.markdown("""
你好！我是 [你的名字]，欢迎来到我的个人博客。
这里我会分享我的学习、生活和项目经验。
""")

# 添加一个侧边栏导航
with st.sidebar:
    st.header("导航")
    page = st.radio("选择页面", ["主页", "博客文章"])

if page == "主页":
    st.subheader("主页")
    st.markdown("当前页面：主页。欢迎来到我的博客主页！这是一个简约风格的 Streamlit 应用。")

elif page == "博客文章":
    st.subheader("博客文章")
    st.markdown("### 我的博客")
    st.markdown("""
    #### 博客文章列表
    1. **文章 1**: 简介内容...
    2. **文章 2**: 简介内容...
    3. **文章 3**: 简介内容...
    """)

# 关于我和联系信息直接展示在底部
st.markdown("""
---
### 关于我
- **名字**: 你的名字
- **职业**: 软件开发工程师
- **爱好**: 编程、阅读、旅行

---
### 联系我
如果你有任何问题或建议，欢迎联系我：
- 邮箱: your_email@example.com
- GitHub: [你的GitHub链接](https://github.com/yourusername)
""")
