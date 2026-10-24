import time
from concurrent.futures import ThreadPoolExecutor
import requests

list_url = [
     "https://www.google.com",
    "https://www.youtube.com",
    "https://www.facebook.com",
    "https://www.wikipedia.org",
    "https://www.amazon.com",
    "https://www.twitter.com",
    "https://www.instagram.com",
    "https://www.linkedin.com",
    "https://www.reddit.com",
    "https://www.netflix.com"
]

def download(url):
    try:
        response = requests.get(url, timeout = 5)
        print(f'Downloaded {url} (size: {len(response.content)} bytes)')
    except Exception as e:
        print(f'Error downloading {url}: {e}')

def main():
    start = time.perf_counter()
    for url in list_url:
        download(url)
    func_time = time.perf_counter() - start

    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers = 10) as executor:
        executor.map(download, list_url)
    fast_time = time.perf_counter() - start

    print("\n" + "="*40)
    print(f'Time without potoks: {func_time:.2f} sec')
    print(f'Time with potoks:   {fast_time:.2f} sec')
    
    if fast_time > 0:
        speed_up = func_time / fast_time
        print(f'Acceleration: X {speed_up:.2f} ')
    print("="*40)

if __name__ == '__main__':
    main()