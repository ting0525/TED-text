import tkinter as tk
import sys
import os
from src.gui.main_window import VTTConverterApp

def resource_path(relative_path):
    """獲取資源的絕對路徑"""
    try:
        # PyInstaller 創建臨時文件夾 _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

def main():
    root = tk.Tk()
    
    # 設置應用圖標
    try:
        icon_path = resource_path(os.path.join("resources", "icon.ico"))
        root.iconbitmap(icon_path)
    except Exception as e:
        print(f"Warning: Could not load icon: {e}")
    
    app = VTTConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()