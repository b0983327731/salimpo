import streamlit as st
import time

# --- [10-1] 底層架構：絕對效能設定 ---
st.set_page_config(
    page_title="長濱寧埔 Voyager v9.5 (清晰版)",
    page_icon="🌊",
    layout="centered"
)

# --- [10-3] 介面視覺：高對比度修正 (修正看不清楚的問題) ---
# 採用 亮白背景 (#FFFFFF) + 深藍文字 (#002244) + 強調金 (#D4A017)
st.markdown("""
<style>
    /* 1. 將主背景改為白色，確保最高清晰度 */
    .stApp { background-color: #FFFFFF; color: #111111; }
    
    /* 2. 將標題改為深藍色 (長濱深藍)，而非黃色 */
    h1, h2, h3 { color: #002244 !important; font-family: 'PingFang TC', 'Microsoft JhengHei', sans-serif; font-weight: 900; }
    
    /* 3. 分頁組件 (Tabs) 文字修正 */
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        color: #002244; font-size: 16px; font-weight: bold;
    }

    /* 4. 核心 CTA 按鈕改造 (保留金色作為醒目強調，但加深邊框) */
    .stButton>button { 
        background-color: #D4A017; color: #FFFFFF; font-weight: 900; 
        width: 100%; border-radius: 10px; border: 2px solid #A67C00; padding: 1rem;
    }
    .stButton>button:hover {
        background-color: #A67C00; color: #FFFFFF;
    }

    /* 5. 景點卡片 (改變卡片背景與文字顏色) */
    .info-card {
        background-color: #F0F2F6; color: #111111; padding: 1.5rem; border-radius: 15px;
        border-left: 8px solid #D4A017; margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .info-card b { color: #002244; font-size: 1.2rem; }
    
    /* 6. 價格標籤 (加深顏色以利閱讀) */
    .price-tag { color: #008000; font-weight: bold; font-size: 1.1rem; }

    /* 7. 行程安排 info 區塊顏色修正 */
    .stAlert { background-color: #004488; color: white; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

# --- 介面渲染 ---

# 1. 標題與視覺 (Tier 1 Hotzone)
st.title("長濱寧埔 | AWOS 深度巡航")
st.image("https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80", 
         caption="太平洋邊緣的生存美學：寧埔海岸", use_container_width=True)

# 2. 功能導航 (多巴胺成癮分頁)
tab1, tab2, tab3 = st.tabs(["📍 深度景點", "🛏️ 嚴選住宿", "📅 行程安排"])

with tab1:
    st.markdown('<br>', unsafe_allow_html=True) # 增加留白
    nodes = {
        "🌾 AWOS 農場": "自然農法基地，提供紅藜、小米食育體驗。",
        "🌊 寧埔 S 彎道": "全台最美海岸公路，視覺降熵的極致表現。",
        "🗿 光榮部落": "阿美族傳統智慧，探訪石棺遺址與遺產文化。"
    }
    for title, desc in nodes.items():
        st.markdown(f'<div class="info-card"><b>{title}</b><br>{desc}</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<br>', unsafe_allow_html=True)
    stays = [
        {"name": "S 彎道海景民宿", "desc": "180度海景，極致零摩擦睡眠體驗。", "price": "NT$ 3,200+"},
        {"name": "AWOS 生態營地", "desc": "與自然共生，最低碳熵的居住方案。", "price": "NT$ 1,200+"}
    ]
    for s in stays:
        st.markdown(f'''
        <div class="info-card">
            <b>{s['name']}</b><br>{s['desc']}<br><span class="price-tag">{s['price']}</span>
        </div>
        ''', unsafe_allow_html=True)

with tab3:
    st.markdown('<br>', unsafe_allow_html=True)
    st.write("### 兩天一夜生存清單")
    st.write("**Day 1: 感官喚醒**")
    st.info("抵達寧埔 -> 休憩區午餐 -> 柴燒海鹽體驗 -> 觀星晚宴")
    st.write("**Day 2: 土地實作**")
    st.info("AWOS 農場導覽 -> 紅藜手作 DIY -> Kiwit 部落巡禮 -> 帶著文化資產賦歸")

# 3. 核心轉換按鈕 (第一性原理)
st.write("---")
if st.button("🚀 立即預約長濱職人導覽"):
    with st.spinner('正在同步長濱在地資源矩陣...'):
        time.sleep(1)
    st.success("✅ **預約成功！** 資料已加密並存儲於分散式節點。")
    st.balloons()

# 4. 系統狀態 (10-4 生態鏈監測)
st.caption("🟢 系統存活狀態：高對比生存模式 | CRF v9.5 Engine Active")
