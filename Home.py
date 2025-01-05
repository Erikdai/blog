import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Daicx666",
    page_icon="🚀",
    layout="wide",
)

# Add CSS for styling the footer icons
st.markdown("""
    <style>
    /* Footer contact links styles */
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
        margin-right: 8px;
        width: 45px;
        height: 45px;
        border-radius: 50%; /* Makes the icons circular */
    }
    .contact-links a:hover {
        text-decoration: underline;
        color: #007BFF; /* Blue color on hover */
    }
    </style>
""", unsafe_allow_html=True)

# Main Page (Home)
st.title("About me")
st.divider()

# Main content section
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Columns for layout
col1, col2 = st.columns([1, 2], gap="medium")

# Left column for profile image
with col1:
    st.image("static/id.jpg", width=225, caption="DingDongJi")

# Right column for detailed bio
with col2:
    st.markdown(
        """
        <div class="about-text" style="margin-top: -10px;">
        😎 Hello! Welcome to my personal page :) I'm Dai, currently an Algorithm Engineer @ Imperial Vision and also a Research Intern @ the IFRC of Zhejiang University Binjiang Institute.
        My areas of interest include <span style="font-weight:bold;">Machine Learning (ML)</span>, <span style="font-weight:bold;">Large Language Models (LLMs)</span>, and <span style="font-weight:bold;">Natural Language Processing (NLP)</span>, <span style="font-weight:bold;">Computer Vision (CV)</span>. I have also conducted some research in <span style="font-weight:bold;">AI for Social Sciences (Cognitive Computing)</span> and <span style="font-weight:bold;">Signal Processing (Bearing Fault Detection)</span>.
        </div>
        """,
        unsafe_allow_html=True
    )

# End of main content section
st.markdown(""" """)
st.divider()
st.markdown('</div>', unsafe_allow_html=True)

# Footer with social links
st.markdown(
    """
    <div class="contact-links">
        <a href="https://www.kaggle.com/patpan" target="_blank">
            <img src="https://www.dataapplab.com/wp-content/uploads/2016/10/kaggle-logo-transparent-300-768x349.png" alt="Kaggle">Kaggle
        </a>
        <a href="https://www.linkedin.com/in/chengxiaodai" target="_blank">
            <img src="https://static.vecteezy.com/system/resources/previews/018/930/587/non_2x/linkedin-logo-linkedin-icon-transparent-free-png.png" alt="LinkedIn">LinkedIn
        </a>
        <a href="mailto:your_email@example.com">
            <img src="https://static.vecteezy.com/system/resources/thumbnails/018/972/241/small_2x/3d-message-icon-a-modern-email-concept-on-isolate-background-png.png" alt="Email">Email
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
