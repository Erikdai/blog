import streamlit as st
import requests

# 设置页面配置
st.set_page_config(
    page_title="AI 对话助手",
    page_icon="🤖",
    layout="wide",
)

# 添加 CSS 样式
st.markdown("""
    <style>
    .main-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .chat-container {
        width: 80%;
        max-width: 800px;
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #ddd;
        border-radius: 10px;
        background-color: #f9f9f9;
    }
    .chat-bubble {
        margin: 10px 0;
        padding: 10px;
        border-radius: 10px;
    }
    .user-message {
        background-color: #dcf8c6;
        align-self: flex-end;
    }
    .bot-message {
        background-color: #fff;
        align-self: flex-start;
    }
    </style>
""", unsafe_allow_html=True)

# 主页面内容
st.title("🤖 AI 对话助手")
st.divider()

# 聊天记录
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# 显示聊天记录
def display_chat_history():
    for chat in st.session_state['chat_history']:
        message_type = 'user-message' if chat['role'] == 'user' else 'bot-message'
        st.markdown(f'<div class="chat-bubble {message_type}">{chat["content"]}</div>', unsafe_allow_html=True)

# 获取 AI 回复
def get_ai_response(user_input):
    api_key = "sk-jpxbaplottoxmhedolxybplftmvmkigyuqlcqpioaqppmqxr"
    api_url = "https://api.silicflow.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-ai/DeepSeek-R1-Distill-Llama-8B",
        "messages": st.session_state['chat_history'] + [{"role": "user", "content": user_input}],
        "temperature": 0.7
    }
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return "抱歉，我无法处理您的请求。"

# 用户输入
user_input = st.text_input("请输入您的消息：", key="user_input")
if st.button("发送"):
    if user_input:
        st.session_state['chat_history'].append({"role": "user", "content": user_input})
        ai_response = get_ai_response(user_input)
        st.session_state['chat_history'].append({"role": "assistant", "content": ai_response})
        st.session_state['user_input'] = ""  # 清空输入框

# 显示聊天记录
display_chat_history()
