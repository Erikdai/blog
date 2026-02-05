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
        margin-right: 0px;
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
st.title("😎About me")
st.divider()

# Main content section
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Columns for layout
col1, col2 = st.columns([1, 2], gap="medium")

# Left column for profile image
with col1:
    st.image("static/id.jpg", width=250, caption="DingDongJi")

# Right column for detailed bio
with col2:
    st.markdown(
        """
        <div class="about-text" style="margin-top: -10px; line-height: 1.8; font-family: Arial, sans-serif;">
        <p>
        Hello! Welcome to my personal page :) I'm Dai, currently a Researcher @ Artificial Intelligence Research Institute, China Academy of Information and Communications Technology (CAICT) .
        </p>
        <p>
        My areas of interest include <span style="font-weight:bold; color: #4DB6AC;">Machine Learning (ML)</span>, 
        <span style="font-weight:bold; color: #4DB6AC;">Large Language Models (LLMs)</span>, 
        <span style="font-weight:bold; color: #4DB6AC;">LLM Hallucination</span>, and 
        <span style="font-weight:bold; color: #4DB6AC;">Natural Language Processing (NLP)</span>, as well as 
        <span style="font-weight:bold; color: #4DB6AC;">Computer Vision (CV)</span>. 
        I have also conducted research in <span style="font-weight:bold; color: #4DB6AC;">AI for Social Sciences (Cognitive Computing)</span> and 
        <span style="font-weight:bold; color: #4DB6AC;">Signal Processing (Bearing Fault Detection)</span>.
        </p>
        <p>
        I received a Bachelor of Computer Science with Honors (Merit) from Universiti Tunku Abdul Rahman, Malaysia, in 2024. I will continue my academic journey at the University of Sydney , pursuing a Master's degree in Computer Science.
        </p>
        <p>
        Feel free to connect with me on <a href="https://www.linkedin.com/in/chengxiaodai" target="_blank" style="text-decoration:none; color:#4A90E2; font-style:italic;">LinkedIn</a> or reach out via <a href="mailto:daicxx1226@gmail.com" style="text-decoration:none; color:#4A90E2; font-style:italic;">Email</a>.
        </p>
        </div>



        """,
        unsafe_allow_html=True
    )

# End of main content section
st.markdown(""" """)
st.divider()
st.markdown('</div>', unsafe_allow_html=True)

