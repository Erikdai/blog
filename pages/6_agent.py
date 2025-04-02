import streamlit as st
import streamlit.components.v1 as components

st.title("我的出海智能助手")

coze_html = """
<div id="coze-widget"></div>
<script>
  window.cozeSettings = {
    bot_id: '7488600231509131318',  // <-- 替换成你自己的
    mode: 'embedded',          // 或者 'embedded' 模式
  };
</script>
<script src="https://cdn.coze.cn/web-sdk/v1/coze-web-sdk.umd.js"></script>
"""

components.html(coze_html, height=600)
