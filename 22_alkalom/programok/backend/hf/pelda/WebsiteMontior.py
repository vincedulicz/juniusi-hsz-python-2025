import requests


class WebsiteMonitor:
    def __init__(self, url):
        self.log_file = "monitor.log"
        self.url = url

    def check_status(self):
        try:
            start_time = time.time()
            response = requests.get(self.url)
            response.raise_for_status()
            elapsed_time = time.time() - start_time
            return {"status_code": response.status_code, "elapsed_time": elapsed_time}
        except requests.RequestException as e:
            return {"error", str(e)}

    def is_online(self) -> bool:
        status = self.check_status()
        return status.get("status_code") == 200

    def get_headers(self):
        try:
            response = requests.head(self.url)
            response.raise_for_status()
            return response.headers
        except requests.RequestException as e:
            return {"error", str(e)}

    def log_status(self):
        result = self.check_status()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as file:
            file.write(f'{timestamp} - {self.url} - {result}\n')

def main():
    url = "httpbin.org"

    monitor = WebsiteMonitor()
    monitor.check_status()
    monitor.is_online()
    monitor.get_headers()

    monitor.log_status()

    urls = [url, "google.com"]

    for url in urls:
        monitor.check_status()