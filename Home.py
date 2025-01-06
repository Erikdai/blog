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
st.title("About me😎")
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
        <span style="font-size: 18px; font-weight: bold;">Hello! Welcome to my personal page! 😊</span>
        </p>
        <p>
        I'm <span style="font-weight: bold;">Dai</span>, currently an <span style="font-weight: bold;">Algorithm Engineer</span> at 
        <span style="font-weight: bold;">Imperial Vision</span> and a <span style="font-weight: bold;">Research Intern</span> at the 
        <span style="font-weight: bold;">IFRC of Zhejiang University Binjiang Institute</span>.
        </p>
        <p style="font-size: 16px; font-weight: bold; color: #0078D4;">Areas of Interest</p>
        <ul style="margin-left: 20px; list-style: none; padding-left: 0;">
        <li>🌟 <span style="font-weight: bold;">Machine Learning (ML)</span></li>
        <li>🌟 <span style="font-weight: bold;">Large Language Models (LLMs)</span> and their Hallucination Reduction</li>
        <li>🌟 <span style="font-weight: bold;">Natural Language Processing (NLP)</span> and <span style="font-weight: bold;">Computer Vision (CV)</span></li>
        <li>🌟 Exploring <span style="font-weight: bold;">AI for Social Sciences</span> and <span style="font-weight: bold;">Signal Processing</span></li>
        </ul>
        <p>
        I’m passionate about pushing the boundaries of AI and bridging technology with social impact. Currently, I’m diving deeper into 
        <span style="font-weight: bold;">LLM alignment</span> and <span style="font-weight: bold;">multi-modal AI</span>.
        </p>
        <p style="font-size: 16px; font-weight: bold; color: #0078D4;">Achievements</p>
        <ul style="margin-left: 20px; list-style: none; padding-left: 0;">
        <li>📝 Published research on <span style="font-weight: bold;">bearing fault detection</span> using signal processing techniques.</li>
        <li>🚀 Led a project on <span style="font-weight: bold;">LLM hallucination validation</span>, significantly improving accuracy.</li>
        </ul>
        <p>
        Feel free to connect with me on <a href="#" style="text-decoration: none; color: #0078D4;">LinkedIn</a>, explore my projects on 
        <a href="#" style="text-decoration: none; color: #0078D4;">GitHub</a>, or reach out if you share similar interests. 
        Let’s create something amazing together! 🚀
        </p>
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
            <img src="https://www.dataapplab.com/wp-content/uploads/2016/10/kaggle-logo-transparent-300-768x349.png" alt="Kaggle" style="height: 50px; width: 60px; margin-right: 5px;">Kaggle
        </a>
        <a href="https://www.linkedin.com/in/chengxiaodai" target="_blank">
            <img src="https://static.vecteezy.com/system/resources/previews/018/930/587/non_2x/linkedin-logo-linkedin-icon-transparent-free-png.png" alt="LinkedIn">LinkedIn
        </a>
        <a href="mailto:your_email@example.com">
            <img src="https://static.vecteezy.com/system/resources/previews/022/484/516/non_2x/google-mail-gmail-icon-logo-symbol-free-png.png" alt="Email" style="height: 35px; width: 35px; margin-right: 8px;">Email
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
