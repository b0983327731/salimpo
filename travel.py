import tkinter as tk
from tkinter import messagebox

# --- [10-1] & [10-3] 核心架構：視覺降熵與生存邏輯 ---
class NingpuAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("NINGPU Voyager v9.0 | 寧埔深度導覽")
        self.root.geometry("390x700")  # 模擬手機比例
        self.root.configure(bg='#0055A4')  # 憲法規定：長濱藍

        # 1. 頂部導航欄 (Tier 1: Conversion Hotzone)
        self.header = tk.Frame(self.root, bg='#0055A4', height=60)
        self.header.pack(fill='x')
        self.title_label = tk.Label(self.header, text="AWOS 農場 | 寧埔", 
                                    fg='#F5D105', bg='#0055A4', 
                                    font=("Arial", 18, "bold"), pady=20)
        self.title_label.pack()

        # 2. 英雄視覺區 (多巴胺成癮模型 - 模擬影像)
        self.hero_canvas = tk.Canvas(self.root, bg='#003366', height=250, highlightthickness=0)
        self.hero_canvas.pack(fill='x', padx=10, pady=10)
        self.hero_canvas.create_text(195, 125, text="[ 太平洋 S 彎道景觀 ]\nAWOS 耕作縮時投影", 
                                     fill="white", justify="center")

        # 3. 核心功能區 (第一性原理：預約轉換)
        self.btn_frame = tk.Frame(self.root, bg='#0055A4')
        self.btn_frame.pack(pady=20)

        self.book_btn = tk.Button(self.btn_frame, text="立即預約 AWOS 職人體驗", 
                                  command=self.trigger_booking,
                                  bg='#F5D105', fg='#000000', 
                                  font=("Arial", 12, "bold"), 
                                  padx=20, pady=10, bd=0, cursor="hand2")
        self.book_btn.pack()

        # 4. 景點列表 (視覺降熵：低認知負荷卡片)
        self.list_frame = tk.Frame(self.root, bg='#0055A4')
        self.list_frame.pack(fill='both', expand=True, padx=20)

        nodes = [
            ("AWOS 農場", "自然農法與紅藜文化"),
            ("寧埔休憩區", "180度太平洋海景"),
            ("光榮部落", "阿美族生存智慧遺址")
        ]

        for name, desc in nodes:
            card = tk.Frame(self.list_frame, bg='#003366', pady=10, padx=10, mb=10)
            card.pack(fill='x', pady=5)
            tk.Label(card, text=name, fg='#F5D105', bg='#003366', font=("Arial", 11, "bold")).pack(anchor='w')
            tk.Label(card, text=desc, fg='white', bg='#003366', font=("Arial", 9)).pack(anchor='w')

        # 5. 底部狀態欄 (黑天鵝防禦：系統生存狀態)
        self.status = tk.Label(self.root, text="● 系統運作中 | 離線生存模式已就緒", 
                               fg='#00FF00', bg='#002244', font=("Arial", 8))
        self.status.pack(side='bottom', fill='x')

    def trigger_booking(self):
        # 模擬 [10-2] 客製化凱利博弈矩陣：高價值轉換
        messagebox.showinfo("預約系統", "已鎖定 AWOS 職人體驗名額！\n正在連結長濱衛星 API...")

# --- 啟動程式 ---
if __name__ == "__main__":
    root = tk.Tk()
    app = NingpuAppGUI(root)
    root.mainloop()
