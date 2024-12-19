import os
import requests
from .validators import URLValidator

class FileHandler:
    def __init__(self):
        self.validator = URLValidator()

    def download_vtt(self, url, download_folder):
        # 驗證 URL
        self.validator.validate_vtt_url(url)

        # 創建下載目錄
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        # 下載文件
        filename = url.split("/")[-1]
        download_path = os.path.join(download_folder, filename)
        
        response = requests.get(url)
        response.raise_for_status()

        with open(download_path, "wb") as file:
            file.write(response.content)

        return download_path