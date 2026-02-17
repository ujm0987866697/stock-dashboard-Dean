import streamlit as st
import pandas as pd

# 頁面配置
st.set_page_config(page_title="Wall Street Pro", layout="wide")

# 自定義 CSS 樣式
st.markdown("""
    <style>
    .stMetric { background-color: #1e2129; padding: 15px; border-radius: 10px; color: white; }
    .stAlert { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ 華爾街頂級操盤手：績效監控中心")
st.caption("Last Update: 2026-02-18 08:00 (CST) | 操盤目標：年化報酬率 50%")

# --- 頂部指標 ---
m1, m2, m3 = st.columns(3)
with m1:
    st.metric("試用期進度", "Day 1 / 14", "⚡ Active")
with m2:
    st.metric("當前總報酬", "-2.46%", "Targeting Alpha", delta_color="inverse")
with m3:
    st.metric("風控水位", "Normal", "VIX 15.2")

st.divider()

# --- 核心標的區塊 ---
st.subheader("🎯 今日首選：台美股戰略標的")
col_tw, col_us = st.columns(2)

with col_tw:
    st.info("🇹🇼 台股：廣達 (2382.TW)")
    st.markdown("""
    - **買入參考價：** **$ 270.0**
    - **基本面：** GB200 出貨領先者，伺服器營收佔比超過 50%。
    - **技術面：** 守住 20MA 後帶量上攻，KD 指標剛從低檔金叉。
    - **操作建議：** 目標 295 元，跌破 258 元果斷停損。
    """)

with col_us:
    st.success("🇺🇸 美股：Palantir (PLTR.US)")
    st.markdown("""
    - **買入參考價：** **$ 166.5**
    - **基本面：** AI 軟體商業化第一梯隊，FCF (自由現金流) 增長極其強勁。
    - **技術面：** 突破長達三個月的矩形整理區，目前處於主升段初段。
    - **操作建議：** 目標 $ 185 元，跌破 $ 152 元果斷停損。
    """)

# --- 績效表 ---
st.divider()
st.subheader("📜 歷史績效對帳單")

# 績效數據清單
data = {
    "標的名稱": ["台積電 (2330.TW)", "NVIDIA (NVDA.US)", "廣達 (2382.TW)", "Palantir (PLTR.US)"],
    "買入日期": ["2/11", "2/11", "2/18", "2/18"],
    "初始價格": [1880, 192.45, 270.0, 166.5],
    "當前價格": [1915, 184.14, "WAIT", "WAIT"],
    "當前損益 %": [1.86, -4.32, 0.0, 0.0]
}

df = pd.DataFrame(data)

# 美化顯示
def color_profit(val):
    if isinstance(val, float):
        color = '#ff4b4b' if val > 0 else '#09ab3b' # 台灣紅漲綠跌習慣
        return f'color: {color}; font-weight: bold'
    return ''

st.table(df.style.applymap(color_profit, subset=['當前損益 %']))

st.warning("⚠️ 操盤手紀律：績效不佳即資遣。我不找藉口，只找獲利路徑。")
