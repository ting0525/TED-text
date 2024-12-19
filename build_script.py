import PyInstaller.__main__
import os

def build_executable():
    # 確保資源目錄存在
    if not os.path.exists('resources'):
        os.makedirs('resources')
    
    PyInstaller.__main__.run([
        'main.py',
        '--name=VTTConverter',
        '--windowed',  # 不顯示控制台窗口
        '--icon=resources/icon.ico',
        '--add-data=resources;resources',  # 包含資源文件
        '--clean',  # 清理臨時文件
        '--noconfirm',  # 覆蓋現有文件而不詢問
        '--onefile',  # 打包成單個文件
    ])

if __name__ == "__main__":
    build_executable()
    
