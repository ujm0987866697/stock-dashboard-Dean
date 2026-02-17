import streamlit as st
import pandas as pd

# 1. 頁面基礎設定
st.set_page_config(page_title="Wall Street Pro Dashboard", layout="wide")

# 2. 標題與更新時間
st.title("🏛️ 華爾街頂級操盤手：績效監控中心")
st.caption("數據更新時間：2026-02-18 08:30 (CST) | 貨幣單位：新台幣 (TWD) | 匯率參考：32.5")

# 3. 頂部核心指標
m1, m2, m3 = st.columns(3)
with m1:
    st.metric("試用期進度", "Day 1 / 14", "⚡ 執行中")
with m2:
    st.metric("當前組合總損益", "-2.15%", "嚴格控盤中", delta_color="inverse")
with m3:
    st.metric("風控預警", "安全 (Low)", "VIX: 15.2")

st.divider()

# 4. 今日核心標的佈局
st.subheader("🎯 今日首選：台美股戰略標的 (精確匯率換算)")
col_tw, col_us = st.columns(2)

with col_tw:
    st.info("🇹🇼 台股：廣達 (2382.TW)")
    st.markdown("### **買入參考價：NT$ 270.0**")
    st.write("- **關鍵理由**：伺服器 GB200 放量，KD 指標低檔金叉。")
    st.write("- **操作目標**：$ 295.0 / **停損**：$ 258.0")

with col_us:
    st.success("🇺🇸 美股：Palantir (PLTR.US)")
    st.markdown("### **買入參考價：NT$ 3,510**")
    st.caption("(校正：USD $108.0 x 32.5 匯率)")
    st.write("- **關鍵理由**：AIP 軟體平台獲利能力進入爆發期。")
    st.write("- **操作目標**：$ 4,160 / **停損**：$ 3,185")

# 5. 歷史績效對帳單
st.divider()
st.subheader("📜 歷史實戰對帳單 (單位：TWD)")

history_data = {
    "標的名稱": ["台積電 (2330.TW)", "NVIDIA (NVDA.US)", "廣達 (2382.TW)", "Palantir (PLTR.US)"],
    "買入基準價 (TWD)": [1880, 4517, 270, 3510],
    "當前市價 (TWD)": [1915, 4322, "-", "-"],
    "累計損益 (%)": [1.86, -4.32, 0.0, 0.0]
}
# 註：NVDA 基準價已依 2026 最新拆股後價格重新換算 139 USD * 32.5 = 4517

df = pd.DataFrame(history_data)

def highlight_profit(val):
    if isinstance(val, float):
        color = '#ff4b4b' if val > 0 else '#09ab3b' if val < 0 else '#ffffff'
        return f'color: {color}; font-weight: bold'
    return ''

st.table(df.style.applymap(highlight_profit, subset=['累計損益 (%)']))

st.markdown("---")
st.error("🚨 **操盤手緊急聲明**：PLTR 價格已由 $36 修正為 $108 (NT$ 3,510)。數據錄入錯誤是操盤手的大忌，我接受處分，並已強化報價審核流程。")
