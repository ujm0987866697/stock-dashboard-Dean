import streamlit as st

st.set_page_config(page_title="Wall Street Pro")

st.title("🏛️ 華爾街頂級操盤手系統")
st.write("---")
st.success("✅ 系統連線成功！數據加載中...")

# 測試用簡單數據
st.metric(label="台股標的 (2382)", value="270.0", delta="首選")
st.metric(label="美股標的 (PLTR)", value="166.5", delta="強勢")

st.info("老闆，如果你看到這個畫面，請告訴我，我明天早上會推播正式的圖表版代碼。")


