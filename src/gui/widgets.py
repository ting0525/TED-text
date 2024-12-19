import tkinter as tk
from tkinter import ttk, filedialog
import threading

class InputFrame(ttk.Frame):
    def __init__(self, parent, process_callback):
        super().__init__(parent)
        self.process_callback = process_callback
        self.setup_ui()
    
    def setup_ui(self):
        # URL Input
        ttk.Label(self, text="VTT URL:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.url_entry = ttk.Entry(self, width=50)
        self.url_entry.grid(row=0, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Filename Input
        ttk.Label(self, text="MD Filename:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.filename_entry = ttk.Entry(self, width=50)
        self.filename_entry.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Folder selection
        ttk.Label(self, text="Output Folder:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.folder_entry = ttk.Entry(self, width=40)
        self.folder_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)
        self.folder_entry.insert(0, "./")
        
        ttk.Button(self, text="Browse", command=self.browse_folder).grid(
            row=2, column=2, sticky=tk.W, padx=5, pady=5
        )
        
        # Process button
        self.process_button = ttk.Button(
            self, text="Process VTT", command=self.on_process
        )
        self.process_button.grid(row=3, column=0, columnspan=3, pady=20)

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(0, folder_path)

    def on_process(self):
        url = self.url_entry.get().strip()
        output_folder = self.folder_entry.get().strip()
        custom_filename = self.filename_entry.get().strip()
        
        # 在新線程中處理
        thread = threading.Thread(
            target=lambda: self.process_callback(url, output_folder, custom_filename)
        )
        thread.daemon = True
        thread.start()

class StatusFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(
            self, length=300, mode='indeterminate', variable=self.progress_var
        )
        self.progress_bar.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
        
        # Status text
        self.status_text = tk.Text(self, height=10, width=50, wrap=tk.WORD)
        self.status_text.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)

    def update_status(self, message):
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.see(tk.END)

    def start_progress(self):
        self.progress_bar.start(10)

    def stop_progress(self):
        self.progress_bar.stop()