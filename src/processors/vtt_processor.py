import threading
from ..utils.file_handler import FileHandler
from .markdown_formatter import MarkdownFormatter

class VTTProcessor:
    def __init__(self):
        self.file_handler = FileHandler()
        self.markdown_formatter = MarkdownFormatter()

    def process_file(self, url, output_folder, custom_filename, 
                    status_callback=None, completion_callback=None):
        def _process():
            try:
                # 下載文件
                if status_callback:
                    status_callback(f"Downloading VTT file from {url}...")
                downloaded_file = self.file_handler.download_vtt(url, output_folder)

                # 處理為 Markdown
                if status_callback:
                    status_callback("Converting to Markdown...")
                self.markdown_formatter.convert_to_markdown(
                    downloaded_file, 
                    output_folder, 
                    custom_filename
                )

                if status_callback:
                    status_callback("Processing completed successfully!")

            except Exception as e:
                if status_callback:
                    status_callback(f"Error: {str(e)}")
            finally:
                if completion_callback:
                    completion_callback()

        # 在新線程中執行處理
        thread = threading.Thread(target=_process)
        thread.daemon = True
        thread.start()