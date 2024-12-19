import tkinter as tk
from tkinter import ttk
from ..processors.vtt_processor import VTTProcessor
from .widgets import StatusFrame, InputFrame

class VTTConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VTT to Markdown Converter")
        self.root.geometry("600x400")
        
        self.processor = VTTProcessor()
        
        # 創建主框架
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 輸入區域
        self.input_frame = InputFrame(self.main_frame, self.start_processing)
        self.input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # 狀態區域
        self.status_frame = StatusFrame(self.main_frame)
        self.status_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        # 配置網格權重
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)

    def start_processing(self, url, output_folder, custom_filename):
        self.status_frame.start_progress()
        self.processor.process_file(
            url, 
            output_folder, 
            custom_filename,
            status_callback=self.status_frame.update_status,
            completion_callback=self.status_frame.stop_progress
        )