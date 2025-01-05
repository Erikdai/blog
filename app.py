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
    .sidebar-button-container {
        display: flex;
        flex-direction: column;
        align-items: stretch;
    }

    .sidebar-link {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 10px;
        margin: 5px 0;
        font-size: 18px;
        font-weight: normal;
        color: #333; /* Default text color */
        text-align: center;
        background-color: #f5f5f5; /* Default button background color */
        border-radius: 8px;
        width: 100%; /* Ensure full width */
        height: 50px; /* Fixed height */
        transition: all 0.3s ease; /* Smooth transition */
    }

    .sidebar-link:hover {
        background-color: #e0e0e0; /* Background color on hover */
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1); /* Hover shadow */
        cursor: pointer;
    }

    .active {
        background-color: #007BFF; /* Active state background color */
        color: white; /* Active state text color */
        font-weight: bold;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3); /* Shadow for active button */
    }

    /* Contact links */
    .contact-links {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 30px;
        margin-top: 20px;
        font-size: 16px;
    }

    .contact-links a {
        text-decoration: none;
        color: #333;
        display: inline-flex;
        align-items: center;
    }

    .contact-links a img {
        margin-right: 0px;
        width: 60px;
        height: 60px;
        border-radius: 50%;
    }

    .contact-links a:hover {
        text-decoration: underline;
        color: #007BFF;
    }

    /* Main content area */
    .main-content {
        max-width: 1000px;
        margin: 0 auto;
        padding: 20px;
    }

    .about-text {
        text-align: justify;
        font-size: 18px;
        line-height: 1.8;
    }

    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.header("Menu")

    # Page mapping
    pages = {
        "🏠 Home": "Home",
        "📚 Experience": "Experience",
        "📖 Publications": "Publications",
        "🏆 Awards & Certificates": "Awards&Certificates",
    }

    if "page" not in st.session_state:
        st.session_state.page = "Home"

    # Sidebar button container
    st.markdown('<div class="sidebar-button-container">', unsafe_allow_html=True)
    for page_name, page_key in pages.items():
        is_active = "active" if st.session_state.page == page_key else ""
        if st.button(page_name):  # Use button for navigation
            st.session_state.page = page_key
    st.markdown('</div>', unsafe_allow_html=True)

# Main page content
if st.session_state.page == "Home":
    st.title("About me")
    st.divider()

    # Main content section
    st.markdown('<div class="main-content">', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2], gap="medium")

    # Profile image in left column
    with col1:
        st.image("static/id.jpg", width=225, caption="DingDongJi")

    # About me text in right column
    with col2:
        st.markdown(
            """
            <div class="about-text">
            😎 Hello! Welcome to my personal page :) I'm Dai, currently an Algorithm Engineer @ Imperial Vision and also a Research Intern @ the IFRC of Zhejiang University Binjiang Institute.
            My areas of interest include <span style="font-weight:bold;">Machine Learning (ML)</span>, <span style="font-weight:bold;">Large Language Models (LLMs)</span>, and <span style="font-weight:bold;">Natural Language Processing (NLP)</span>, <span style="font-weight:bold;">Computer Vision (CV)</span>. I have also conducted some research in <span style="font-weight:bold;">AI for Social Sciences (Cognitive Computing)</span> and <span style="font-weight:bold;">Signal Processing (Bearing Fault Detection)</span>.
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "Experience":
    st.title("Experience Page")
    st.markdown("Welcome to the Experience Page!")

elif st.session_state.page == "Publications":
    st.title("Publications Page")
    st.markdown("Welcome to the Publications Page!")

elif st.session_state.page == "Awards&Certificates":
    st.title("Awards & Certificates")
    st.divider()

    # Load Markdown content
    try:
        with open("pages/awards_certificates.md", "r", encoding="utf-8") as file:
            md_content = file.read()
        st.markdown(md_content, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("The file 'awards_certificates.md' was not found.")

# Footer with social links
st.markdown(
    """
    <div class="contact-links">
        <a href="https://www.kaggle.com/patpan" target="_blank">
            <img src="https://www.dataapplab.com/wp-content/uploads/2016/10/kaggle-logo-transparent-300-768x349.png" alt="Kaggle" style="height: 45px; margin-right: 7px;">Kaggle
        </a>
        <a href="https://www.linkedin.com/in/chengxiaodai" target="_blank">
            <img src="https://static.vecteezy.com/system/resources/previews/018/930/587/non_2x/linkedin-logo-linkedin-icon-transparent-free-png.png" alt="LinkedIn">LinkedIn
        </a>
        <a href="mailto:your_email@example.com">
            <img src="https://static.vecteezy.com/system/resources/thumbnails/018/972/241/small_2x/3d-message-icon-a-modern-email-concept-on-isolate-background-png.png" alt="Email" style="height: 45px; width: 45px; margin-right: 9px;">Email
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
