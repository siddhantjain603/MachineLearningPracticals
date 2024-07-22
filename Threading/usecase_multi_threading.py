import threading
import requests
from bs4 import BeautifulSoup

urls = ['https://scikit-learn.org/stable/modules/linear_model.html',
        'https://scikit-learn.org/stable/modules/lda_qda.html',
        'https://scikit-learn.org/stable/modules/kernel_ridge.html']

def fetch_content(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"Number of characters fetch from {url} is : {len(soup.text)}")


threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Task completed")