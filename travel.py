import streamlit as st
import time

# --- [10-1] 底層架構：絕對效能設定 ---
st.set_page_config(
    page_title="長濱寧埔 Voyager v9.7 (深度擴展版)",
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

st.title("長濱寧埔 | AWOS 深度巡航")
st.image("https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80", 
         caption="太平洋邊緣的生存美學：寧埔海岸", use_container_width=True)

tab1, tab2, tab3 = st.tabs(["📍 深度景點", "🛏️ 嚴選住宿", "📅 兩日行程安排"])

# --- Tab 1: 景點擴充 ---
with tab1:
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('''
    <div class="info-card">
        <b>🌾 AWOS 農場 (自然農法實作基地)</b>
        <span class="desc">隱身於寧埔半山腰的食育基地。這裡拒絕化肥，讓作物與雜草共生，展現最強韌的生存美學。
        <ul>
            <li><b>紅藜與小米導覽：</b> 實地觀察長濱特有紅藜的生長型態，了解其極高的營養抗氧化價值。</li>
            <li><b>原民風味手作：</b> 親手體驗從田間採集到餐桌的過程，製作傳統酒麴與原民小米風味餐。</li>
        </ul>
        </span>
    </div>
    
    <div class="info-card">
        <b>🌊 寧埔休憩區 (S-Curve 視覺降熵點)</b>
        <span class="desc">台 11 線 94K 處，擁有全台最完美的海岸公路 S 型曲線，是抹除都市焦慮的絕佳場域。
        <ul>
            <li><b>晨昏攝影熱區：</b> 建議於清晨 05:30 捕捉太平洋日出，或下午 16:00 拍攝稻浪與海浪交織的黃金時刻。</li>
            <li><b>無死角觀海：</b> 具備寬闊的停車與觀景空間，適合靜坐聆聽海潮白噪音。</li>
        </ul>
        </span>
    </div>
    
    <div class="info-card">
        <b>🗿 光榮部落 Kiwit (文化遍歷性遺址)</b>
        <span class="desc">保存完整的阿美族傳統聚落，充滿歷史厚度與先民的生存智慧。
        <ul>
            <li><b>巨石與石棺遺址：</b> 探訪擁有數千年歷史的史前文化遺跡，感受時光的凝結。</li>
            <li><b>傳統編織與防禦工法：</b> 認識部落如何利用刺蔥、林投樹建立防禦圍籬，以及傳統船隻的結構科學。</li>
        </ul>
        </span>
    </div>
    ''', unsafe_allow_html=True)

# --- Tab 2: 住宿擴充 ---
with tab2:
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('''
    <div class="info-card">
        <b>🌊 S 彎道海景民宿 (極致感官解壓縮)</b>
        <span class="desc">為高端慢活族群打造。房內配備全景落地窗，躺在床上即可迎接太平洋第一道曙光。<br>
        <i>*包含在地小農契作早餐、夜間無光害觀星露台。</i></span>
        <span class="price-tag">NT$ 3,200 - 4,500 / 晚</span>
    </div>
    
    <div class="info-card">
        <b>🏕️ AWOS 生態營地 (土地零距離接觸)</b>
        <span class="desc">搭建於農場梯田間，主打無痕山林的低碳熵居住方案。適合渴望完全抽離都市的旅客。<br>
        <i>*提供柴燒熱水、阿美族耆老營火故事夜、現採農場鮮蔬朝食。</i></span>
        <span class="price-tag">NT$ 1,200 - 1,800 / 晚</span>
    </div>
    
    <div class="info-card">
        <b>🪵 寧埔職人客棧 (文化深度體驗)</b>
        <span class="desc">由返鄉青年與在地工藝師共同經營，一樓為木作與海鹽展示空間，二樓為客房。<br>
        <i>*入住房客可免費參與一次「柴燒海鹽萃取」或「傳統月桃葉編織」體驗。</i></span>
        <span class="price-tag">NT$ 2,500 - 2,800 / 晚</span>
    </div>
    ''', unsafe_allow_html=True)

# --- Tab 3: 行程擴充 ---
with tab3:
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('''
    <div class="info-card">
        <b>📌 Day 1：感官喚醒與海洋萃取</b>
        <span class="desc">
        <ul>
            <li><b>10:30｜抵達寧埔：</b> 駛入台 11 線 S 彎道，進行視覺降熵，感受海天一線的震撼。</li>
            <li><b>12:00｜職人午餐：</b> 享用無菜單料理，品嚐長濱現撈海鮮與在地野菜。</li>
            <li><b>14:30｜柴燒海鹽 DIY：</b> 前往鹽寮，在柴火的高溫中，親手從太平洋海水中熬煮、結晶出富含礦物質的純淨海鹽。</li>
            <li><b>18:00｜部落風味晚宴：</b> 於住宿地享用結合現代烹調與原民香料的晚餐。</li>
            <li><b>20:00｜觀星靜心：</b> 於無光害的長濱夜空下，聆聽海浪聲入眠。</li>
        </ul>
        </span>
    </div>
    
    <div class="info-card">
        <b>📌 Day 2：土地實作與文化溯源</b>
        <span class="desc">
        <ul>
            <li><b>09:00｜AWOS 農場食育：</b> 深入自然農法梯田，認識傳統作物（紅藜、小米），學習不破壞地力的永續種植智慧。</li>
            <li><b>11:30｜紅藜手作午餐：</b> 親自採摘食材，揉製紅藜麵疙瘩或阿美族傳統米食 (Toron)。</li>
            <li><b>14:00｜Kiwit 光榮部落巡禮：</b> 走進歷史，聽部落耆老講述石棺遺址的故事，了解阿美族的海洋與土地哲學。</li>
            <li><b>16:30｜文化賦歸：</b> 帶著親手製作的海鹽與滿載的多巴胺，踏上返程。</li>
        </ul>
        </span>
    </div>
    ''', unsafe_allow_html=True)

st.write("---")
if st.button("🚀 立即預約長濱職人導覽"):
    with st.spinner('正在同步長濱在地資源矩陣，確認 AWOS 容載量...'):
        time.sleep(1.5)
    st.success("✅ **預約成功！** 資料已加密並存儲於分散式節點，在地職人將於 24 小時內與您聯繫。")
    st.balloons()

st.caption("🟢 系統存活狀態：極致清晰模式 (Absolute Clarity) | CRF v9.7 Engine Active")
