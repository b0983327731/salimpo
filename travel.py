/**
 * SYSTEM: Ningpu-AWOS Intelligence Voyager (v9.0)
 * ARCHITECTURE: CRF-v9.0 Tactical Matrix
 * MISSION: 絕對效能、認知鎖定、黑天鵝防禦
 */

import React, { useState, useEffect, useCallback } from 'react';
import { TelemetryOracle, CacheManager, DynamicRouter, UIEntropyReducer } from './CRF_Engines';

// --- [10-1] 底層架構：遍歷性與生存優先 ---
const NINGPU_GEO_REGISTRY = {
  AWOS_FARM: { id: 'awos', lat: 23.235, lng: 121.410, tier: 1, type: 'AGRI_TECH' },
  NINGPU_REST: { id: 'rest_area', lat: 23.232, lng: 121.412, tier: 1, type: 'LANDSCAPE' },
  KIWIT_TRIBE: { id: 'kiwit', lat: 23.225, lng: 121.408, tier: 2, type: 'CULTURE' }
};

const NingpuApp = () => {
  const [isOffline, setIsOffline] = useState(!navigator.onLine);
  const [activeNode, setActiveNode] = useState(NINGPU_GEO_REGISTRY.AWOS_FARM);
  const [entropyLevel, setEntropyLevel] = useState(0);

  // [紅皇后監測]：實時監測技術債與數據衰減
  useEffect(() => {
    const monitor = TelemetryOracle.startPulse('RedQueen');
    window.addEventListener('offline', () => setIsOffline(true));
    return () => monitor.stop();
  }, []);

  // --- [10-2] 客製化需求：AWOS 農場商業意圖透視 ---
  const handleBooking = useCallback((type) => {
    // 執行「納什均衡」檢核：確保農場承載力與體驗品質最佳化
    if (TelemetryOracle.predictCapacity('AWOS_FARM') > 0.8) {
      UIEntropyReducer.notify("觸發需求熔斷：目前人潮過多，建議前往寧埔休憩區。");
      return;
    }
    // [第一性原理]：直接進入核心轉換，移除所有中間跳轉
    DynamicRouter.push(`/booking/awos?type=${type}`);
  }, []);

  // --- [10-3] 介面交互：注意力掠奪與視覺降熵 ---
  return (
    <div style={{ backgroundColor: '#0055A4', color: '#FFFFFF', fontFamily: 'Inter, sans-serif' }}>
      {/* Tier 1: Conversion Hotzone - 頂部核心狀態 */}
      <header style={{ padding: '20px', borderBottom: '2px solid #F5D105' }}>
        <h1 style={{ fontSize: '24px', fontWeight: 900 }}>NINGPU | 寧埔：AWOS </h1>
        {isOffline && <span style={{ color: '#FF4444' }}>[生存模式：離線數據已啟用]</span>}
      </header>

      <main>
        {/* [多巴胺成癮模型]：動態感官內容 */}
        <section id="hero-vision" style={{ height: '40vh', position: 'relative' }}>
          <img 
            src="/assets/awos_s_curve_dawn.jpg" 
            alt="AWOS Farm Dawn" 
            style={{ width: '100%', objectFit: 'cover', filter: 'contrast(1.1)' }}
          />
          <div className="cta-overlay" style={{ position: 'absolute', bottom: '10%', right: '5%' }}>
            <button 
              onClick={() => handleBooking('DIY_SALT')}
              style={{ 
                backgroundColor: '#F5D105', 
                color: '#000', 
                padding: '15px 30px', 
                borderRadius: '50px',
                fontWeight: 'bold',
                boxShadow: '0 10px 20px rgba(0,0,0,0.3)'
              }}
            >
              立即預約 AWOS 職人體驗
            </button>
          </div>
        </section>

        {/* [10-4] 資源整合：API 備援矩陣 */}
        <div id="map-container" style={{ height: '30vh' }}>
          <MapComponent 
            center={activeNode} 
            provider={isOffline ? 'OSM_OFFLINE' : 'GOOGLE_MAPS_PREMIUM'} 
            onFailover={() => console.log("黑天鵝防禦啟動：切換至 Mapbox")}
          />
        </div>

        {/* 景點/美食列表：視覺熵控制 */}
        <section style={{ padding: '20px' }}>
          <h2 style={{ color: '#F5D105' }}>深度節點 (Tier-1 Assets)</h2>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '15px' }}>
            <div className="card" onClick={() => setActiveNode(NINGPU_GEO_REGISTRY.AWOS_FARM)}>
              <h3>AWOS 農場</h3>
              <p>自然農法與原民生活</p>
            </div>
            <div className="card" onClick={() => setActiveNode(NINGPU_GEO_REGISTRY.NINGPU_REST)}>
              <h3>寧埔休憩區</h3>
              <p>180度太平洋 S 彎道</p>
            </div>
          </div>
        </section>
      </main>

      {/* 底部導航：零摩擦設計 */}
      <nav style={{ position: 'fixed', bottom: 0, width: '100%', display: 'flex', justifyContent: 'space-around', background: '#003366', padding: '10px 0' }}>
        <button style={{ opacity: 0.9 }}>地圖</button>
        <button style={{ opacity: 0.9 }}>預約</button>
        <button style={{ opacity: 0.9 }}>我的資產</button>
      </nav>
    </div>
  );
};

export default NingpuApp;
