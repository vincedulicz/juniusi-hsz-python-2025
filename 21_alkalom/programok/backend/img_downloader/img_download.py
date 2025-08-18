import requests
from abc import ABC, abstractmethod
import os

class Downloader(ABC):
    @abstractmethod
    def download(self, url: str, save_path: str):
        pass

class ImageDownloader(Downloader):
    def download(self, url: str, save_path: str):
        try:
            response = requests.get(url, stream=True, timeout=10)
            response.raise_for_status()
            with open(save_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    if chunk:
                        file.write(chunk)
                print("kép letöltve", save_path)
        except requests.exceptions.Timeout:
            print("timeout")
        except requests.exceptions.HTTPError as http_err:
            print(http_err)
        except Exception as err:
            print(err)

class Config:
    IMAGE_DIR = "letoltott_kep"

class ImageDownloaderApp:
    def __init__(self, downloader: Downloader, config: Config):
        self.downloader = downloader
        self.config = config
        self._ensure_directory()

    def _ensure_directory(self):
        if not os.path.exists(self.config.IMAGE_DIR):
            os.makedirs(self.config.IMAGE_DIR)
            print("mappa létrehozva", {self.config.IMAGE_DIR})

    def download_image(self, url: str):
        file_name = url.split('/')[-1]
        save_path = os.path.join(self.config.IMAGE_DIR, file_name)
        self.downloader.download(url, save_path)

def main():
    downloader = ImageDownloader()
    config = Config()
    app = ImageDownloaderApp(downloader, config)

    image_url = "https://prooktatas.hu/assets/img/prooktatas-programozo-kepzes-online.png"
    app.download_image(image_url)


main()
