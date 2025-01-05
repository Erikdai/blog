import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Daicx666",
    page_icon="🚀",
    layout="wide",
)

# Add CSS for custom styling
st.markdown("""
    <style>
    /* Sidebar fixed and non-collapsible */
    [data-testid="collapsedControl"] {
        display: none;
    }

    /* Sidebar link styles */
    .sidebar-link {
        display: block;
        padding: 10px 15px;
        margin: 3px 0;
        font-size: 18px;
        color: var(--text-color);
        text-align: left;
        background-color: var(--background-color);
        border: none;
        border-radius: 5px;
    }

    .sidebar-link:hover {
        background-color: var(--secondary-background-color);
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
        cursor: pointer;
    }

    .active {
        background-color: #007BFF; /* Blue highlight color */
        font-weight: bold;
        color: white;
    }

    /* Contact links */
    .contact-links {
        display: flex;
        justify-content: center; /* Center the links */
        align-items: center;
        gap: 30px; /* Space between links */
        margin-top: 20px;
        font-size: 16px;
    }
    .contact-links a {
        text-decoration: none;
        color: var(--text-color);
        display: inline-flex;
        align-items: center;
    }
    .contact-links a img {
        margin-right: 2px;
        width: 55px;
        height: 55px;
        border-radius: 50%;
    }
    .contact-links a:hover {
        text-decoration: underline;
        color: #007BFF; /* Blue color on hover */
    }

    /* Main content area */
    .main-content {
        max-width: 1000px;
        margin: 0 auto;
        padding: 20px;
    }

    /* About section layout */
    .about-col {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }

    .about-text {
        text-align: justify;
        font-size: 18px;
        line-height: 1.8;
        margin-top: 20px;
    }

    /* Responsive font size for smaller screens */
    @media (max-width: 768px) {
        .about-text {
            font-size: 16px;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.header("Menu")

    pages = {
        "🏠 Home": "Home",
        "📚 Experience": "Experience",
        "📖 Publications": "Publications",
        "🏆 Awards & Certificates": "Awards&Certificates",
    }

    if "page" not in st.session_state:
        st.session_state.page = "Home"

    for page, module in pages.items():
        is_active = "active" if st.session_state.page == module else ""
        st.markdown(
            f'<div class="sidebar-link {is_active}" onclick="window.location=\'/{module.lower()}.py\';">{page}</div>',
            unsafe_allow_html=True
        )

# Page content (Home page)
st.title("About Me😎")
st.divider()

# Main content section
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Columns for layout
col1, col2 = st.columns([1, 2], gap="medium")

# Left column for profile image
with col1:
    st.image("static/id.jpg", width=225, caption="DingDongJi")
# Right column for detailed bio
# Right column for detailed bio
with col2:
    st.markdown(
        """
        <div class="about-text" style="margin-top: -10px;"> <!-- 调整margin-top向上移动 -->
        Hello! Welcome to my personal page :) I'm Dai, currently an Algorithm Engineer @ Imperial Vision and also a Research Intern @ the IFRC of Zhejiang University Binjiang Institute.
        My areas of interest include <span style="font-weight:bold;">Machine Learning (ML)</span>, <span style="font-weight:bold;">Large Language Models (LLMs)</span>, and <span style="font-weight:bold;">Natural Language Processing (NLP)</span>, <span style="font-weight:bold;">Computer Vision (CV)</span>. I have also conducted some research in <span style="font-weight:bold;">AI for Social Sciences (Cognitive Computing)</span> and <span style="font-weight:bold;">signal Processing (Bearing Fault Detection)</span>.<br>
        </div>
        """,
        unsafe_allow_html=True
    )

# End of main content section
st.markdown(""" """,)
st.divider()
st.markdown('</div>', unsafe_allow_html=True)

# Footer with social links
# st.markdown(""" """,)
st.markdown(
    """
    <div class="contact-links">
        <a href="https://www.kaggle.com/patpan" target="_blank">
            <img src="https://www.dataapplab.com/wp-content/uploads/2016/10/kaggle-logo-transparent-300-768x349.png" alt="Kaggle">Kaggle
        </a>
        <a href="https://www.linkedin.com/in/chengxiaodai" target="_blank">
            <img src="https://static.vecteezy.com/system/resources/previews/016/716/470/non_2x/linkedin-icon-free-png.png" alt="LinkedIn">LinkedIn
        </a>
        <a href="mailto:daicxx1226@gmail.com">
            <img src="https://static.vecteezy.com/system/resources/previews/016/716/465/non_2x/gmail-icon-free-png.png"" alt="Email">Email
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
