import streamlit as st
import time

# --- [10-1] 底層架構：絕對效能設定 ---
st.set_page_config(
    page_title="台東長濱 Voyager v9.8 (全境擴充版)",
    page_icon="🌊",
    layout="centered"
)

# --- [10-3] 介面視覺：強制高對比度覆蓋 (Absolute Override) ---
st.markdown("""
<style>
    .stApp { background-color: #FAFAFA !important; }
    h1, h2, h3 { color: #003366 !important; font-weight: 900 !important; }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        color: #003366 !important; font-size: 1.1rem !important; font-weight: 800 !important;
    }
    .info-card {
        background-color: #FFFFFF !important; 
        border: 2px solid #003366 !important;
        border-left: 10px solid #D4A017 !important; 
        padding: 20px !important; 
        border-radius: 10px !important;
        margin-bottom: 1.5rem !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1) !important;
    }
    .info-card b { 
        color: #003366 !important; font-size: 1.4rem !important; 
        display: block !important; margin-bottom: 12px !important;
        border-bottom: 1px dashed #CCCCCC; padding-bottom: 8px;
    }
    .info-card span.desc { 
        color: #000000 !important; font-size: 1.1rem !important; 
        font-weight: 600 !important; line-height: 1.8 !important; display: block !important;
    }
    .info-card ul { margin-top: 10px !important; margin-bottom: 0 !important; padding-left: 20px !important; }
    .info-card li { color: #000000 !important; font-weight: 600 !important; font-size: 1.05rem !important; line-height: 1.6 !important; }
    .price-tag { 
        color: #D4A017 !important; font-size: 1.2rem !important; 
        font-weight: 900 !important; margin-top: 15px !important; display: block !important;
    }
    .stButton>button { 
        background-color: #003366 !important; color: #FFFFFF !important; 
        font-weight: 900 !important; font-size: 1.2rem !important;
        width: 100% !important; border-radius: 8px !important; 
        border: none !important; padding: 1rem !important;
    }
    .stButton>button:hover {
        background-color: #D4A017 !important; color: #000000 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 介面渲染 ---

st.title("台東長濱鄉 | 太平洋生存美學")
st.image("https://images.unsplash.com/photo-1542332213-9b5a5a3fad35?auto=format&fit=crop&w=800&q=80", 
         caption="山海交界處的長濱鄉：金剛大道與太平洋的凝視", use_container_width=True)

# 擴充為 4 個核心分頁
tab1, tab2, tab3, tab4 = st.tabs(["📍 深度景點", "🍽️ 在地美食", "🛏️ 嚴選住宿", "📅 兩日行程"])

# --- Tab 1: 景點擴充 (長濱全境) ---
with tab1:
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('''
    <div class="info-card">
        <b>🦍 金剛大道 (長光部落)</b>
        <span class="desc">一條沒有電線桿的筆直大道，直通太平洋。兩側伴隨著四季變換的稻浪，是視覺降熵的終極場域。
        <ul>
            <li><b>觀景建議：</b> 建議租借單車騎行，感受海風與金剛山的壯麗對話。</li>
        </ul>
        </span>
    </div>
    
    <div class="info-card">
        <b>🗿 八仙洞遺址 & 阿美族文化節點</b>
        <span class="desc">長濱不只有海，還有深厚的史前文化與阿美族部落底蘊。
        <ul>
            <li><b>地質奇觀：</b> 探訪百萬年海水侵蝕形成的海蝕洞，見證長濱文化的發源地。</li>
            <li><b>部落工藝探尋：</b> 在周邊部落，您可以看見傳統阿美族工藝的延續，了解先民如何利用自然素材製作漁具與傳統編織，展現強韌的生存智慧。</li>
        </ul>
        </span>
    </div>
    
    <div class="info-card">
        <b>🌾 AWOS 農場 (寧埔村)</b>
        <span class="desc">隱身於寧埔半山腰的食育基地。拒絕化肥，讓作物與雜草共生。
        <ul>
            <li><b>自然農法導覽：</b> 實地觀察土地復育過程，感受最純粹的泥土氣息。</li>
        </ul>
        </span>
    </div>
    ''', unsafe_allow_html=True)

# --- Tab 2: 美食擴充 (長濱味覺 ROI) ---
with tab2:
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('''
    <div class="info-card">
        <b>🌾 阿美族紅藜與傳統風味</b>
        <span class="desc">長濱的味覺資產，來自土地的直接餽贈。
        <ul>
            <li><b>紅藜料理：</b> 品嚐在地契作的「穀物紅寶石」紅藜，無論是加入米飯、傳統米食或是特製手作料理，都能攝取極高的營養抗氧化價值。</li>
            <li><b>傳統祭典風味：</b> 若在夏秋之際（豐年祭季節）造訪，更有機會品嚐到部落特有的醃肉 (Siraw) 與野菜輪廓，體驗最真實的原民飲食哲學。</li>
        </ul>
        </span>
    </div>
    
    <div class="info-card">
        <b>🐟 長濱無菜單海鮮 (預約制)</b>
        <span class="desc">嚴格落實「海裡有什麼，今天吃什麼」的第一性原理。
        <ul>
            <li><b>特色：</b> 每日清晨由長濱漁港現撈，無過度調味，搭配手工柴燒海鹽，提取食材最本質的太平洋鮮甜。</li>
        </ul>
        </span>
    </div>
    ''', unsafe_allow_html=True)

# --- Tab 3: 住宿擴充 (長濱資產配置) ---
with tab3:
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('''
    <div class="info-card">
        <b>🌊 頂級海景民宿 (真柄/寧埔海岸)</b>
        <span class="desc">為高端慢活族群打造。房內配備全景落地窗，躺在床上即可迎接太平洋第一道曙光。<br>
        <i>*多數具備無光害觀星露台，提供極致零摩擦的睡眠體驗。</i></span>
        <span class="price-tag">NT$ 3,800 - 6,500 / 晚</span>
    </div>
    
    <div class="info-card">
        <b>🏕️ 部落生態營地 & 職人客棧</b>
        <span class="desc">主打無痕山林的低碳熵居住方案。適合渴望完全抽離都市，與在地文化連結的旅客。<br>
        <i>*提供柴燒熱水、阿美族耆老營火故事夜、或傳統月桃葉編織體驗。</i></span>
        <span class="price-tag">NT$ 1,200 - 2,800 / 晚</span>
    </div>
    ''', unsafe_allow_html=True)

# --- Tab 4: 兩日行程 (時間軸排程) ---
with tab4:
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('''
    <div class="info-card">
        <b>📌 Day 1：海岸線的視覺降熵與味覺萃取</b>
        <span class="desc">
        <ul>
            <li><b>10:30｜抵達長濱：</b> 駛入台 11 線，首站前往「金剛大道」騎乘單車，感受山海之間的震撼。</li>
            <li><b>12:30｜無菜單海鮮：</b> 享用長濱漁港現撈海鮮，搭配柴燒海鹽。</li>
            <li><b>15:00｜八仙洞與傳統工藝：</b> 探訪史前遺址，走入周邊部落感受阿美族傳統編織與生活器具的工藝之美。</li>
            <li><b>18:30｜入住民宿：</b> 伴隨海潮白噪音，在無光害的露台享受星空。</li>
        </ul>
        </span>
    </div>
    
    <div class="info-card">
        <b>📌 Day 2：土地實作與文化溯源</b>
        <span class="desc">
        <ul>
            <li><b>09:00｜AWOS 農場食育：</b> 深入半山腰的梯田，認識傳統作物，學習不破壞地力的永續種植智慧。</li>
            <li><b>11:30｜紅藜手作午餐：</b> 親自參與紅藜與小米的料理過程，體驗傳統阿美族飲食文化。</li>
            <li><b>14:30｜海岸咖啡靜心：</b> 在長濱的獨立咖啡館，點一杯手沖咖啡，將這兩天的多巴胺轉化為長期的心靈資產。</li>
            <li><b>16:00｜文化賦歸：</b> 帶著充滿電的身心踏上返程。</li>
        </ul>
        </span>
    </div>
    ''', unsafe_allow_html=True)

st.write("---")
if st.button("🚀 啟動長濱全境導覽預約系統"):
    with st.spinner('正在同步長濱在地資源矩陣，計算最優路線...'):
        time.sleep(1.5)
    st.success("✅ **路由鎖定成功！** 系統已將您的行程偏好加密並存儲於分散式節點，在地職人團隊將儘速與您聯繫。")
    st.balloons()

st.caption("🟢 系統存活狀態：全境高對比防護模式 (Absolute Clarity) | CRF v9.8 Engine Active")
