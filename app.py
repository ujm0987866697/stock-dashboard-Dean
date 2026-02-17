import streamlit as st
import pandas as pd

# 1. 頁面基礎設定
st.set_page_config(page_title="Wall Street Pro Dashboard", layout="wide")

# 2. 標題與更新時間
st.title("🏛️ 華爾街頂級操盤手：績效監控中心")
st.caption("數據更新時間：2026-02-18 08:00 (CST) | 貨幣單位：新台幣 (TWD) | 匯率參考：32.5")

# 3. 頂部核心指標
m1, m2, m3 = st.columns(3)
with m1:
    st.metric("試用期進度", "Day 1 / 14", "⚡ 執行中")
with m2:
    st.metric("當前組合總損益", "-1.23%", "追逐 Alpha 中", delta_color="inverse")
with m3:
    st.metric("風控預警", "安全 (Low)", "VIX: 15.2")

st.divider()

# 4. 今日核心標的佈局
st.subheader("🎯 今日首選：台美股戰略標的 (換算台幣)")
col_tw, col_us = st.columns(2)

with col_tw:
    st.info("🇹🇼 台股：廣達 (2382.TW)")
    st.markdown("### **買入參考價：NT$ 270.0**")
    st.write("- **基本面**：GB200 伺服器首波交付名單。")
    st.write("- **技術面**：股價站穩季線，MACD 翻正。")
    st.write("- **目標價**：$295.0 / **停損價**：$258.0")

with col_us:
    st.success("🇺🇸 美股：Palantir (PLTR.US)")
    st.markdown("### **買入參考價：NT$ 1,186**")
    st.caption("(原價 $36.5 USD x 32.5 匯率)")
    st.write("- **基本面**：AIP 平台企業簽約數翻倍。")
    st.write("- **技術面**：成功突破 $35 關鍵阻力區。")
    st.write("- **目標價**：$1,462 / **停損價**：$1,056")

# 5. 歷史績效對帳單 (全台幣化)
st.divider()
st.subheader("📜 歷史實戰對帳單 (單位：TWD)")

history_data = {
    "標的名稱": ["台積電 (2330.TW)", "NVIDIA (NVDA.US)", "廣達 (2382.TW)", "Palantir (PLTR.US)"],
    "買入基準價": [1880, 6255, 270, 1186],
    "當前市價": [1915, 5985, "-", "-"],
    "累計損益 (%)": [1.86, -4.32, 0.0, 0.0]
}
# 註：NVDA 192.45 * 32.5 = 6254.6 -> 6255
# 註：NVDA 184.14 * 32.5 = 5984.5 -> 5985

df = pd.DataFrame(history_data)

# 美化表格顯示邏輯
def highlight_profit(val):
    if isinstance(val, float):
        color = '#ff4b4b' if val > 0 else '#09ab3b' if val < 0 else '#ffffff'
        return f'color: {color}; font-weight: bold'
    return ''

st.table(df.style.applymap(highlight_profit, subset=['累計損益 (%)']))

st.markdown("---")
st.warning("⚠️ **操盤手筆記**：已統一貨幣為台幣。明早 08:00 將依最新匯率與股價更新。")
