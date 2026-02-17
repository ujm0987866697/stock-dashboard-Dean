import streamlit as st
import pandas as pd

# 1. 頁面基礎設定
st.set_page_config(page_title="Wall Street Pro Dashboard", layout="wide")

# 2. 專業化視覺風格 (CSS)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1e2129; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    div[data-testid="stExpander"] { border: none; box-shadow: none; }
    </style>
    """, unsafe_allow_html=True)

# 3. 標題與更新時間
st.title("🏛️ 華爾街頂級操盤手：績效監控中心")
st.caption("數據更新時間：2026-02-18 08:00 (CST) | 核心目標：年化報酬率 50%")

# 4. 頂部核心指標
m1, m2, m3 = st.columns(3)
with m1:
    st.metric("試用期進度", "Day 1 / 14", "⚡ 執行中")
with m2:
    # 這裡預設為目前組合的平均概況
    st.metric("當前組合總損益", "-1.23%", "追逐 Alpha 中", delta_color="inverse")
with m3:
    st.metric("風控預警", "安全 (Low)", "VIX: 15.2")

st.divider()

# 5. 今日核心標的佈局
st.subheader("🎯 今日首選：台美股戰略標的")
col_tw, col_us = st.columns(2)

with col_tw:
    st.info("🇹🇼 台股：廣達 (2382.TW)")
    st.markdown("""
    - **買入參考價：** **NT$ 270.0**
    - **核心買進理由**：
        1. **基本面**：GB200 伺服器首波交付名單，業績預計 Q1 觸底回升。
        2. **技術面**：股價站穩季線後溫和放量，MACD 柱狀體翻正。
    - **操作紀律**：
        - **目標價**：$ 295.0
        -
