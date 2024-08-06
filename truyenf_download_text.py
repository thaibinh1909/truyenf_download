import requests
from bs4 import BeautifulSoup

def download_text_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title_tag = soup.find('a', class_='chapter-title')
            title = title_tag['title'] if title_tag else "No title found"
            content_div = soup.find('div', {'id': 'chapter-c'})
            if content_div:
                text = content_div.get_text(separator='\n')
                return title, text
            else:
                print(f"Failed to find the content div for {url}.")
                return title, None
        else:
            print(f"Failed to retrieve the webpage {url}. Status code: {response.status_code}")
            return None, None
    except Exception as e:
        print(f"An error occurred for {url}: {e}")
        return None, None

# Open the file once before the loop starts
with open('downloaded_text_combined.txt', 'w', encoding='utf-8') as file:
    # Loop through the chapters
    for i in range(1, 1312):  # Loop from chapter 1 to 3
        url = f'https://truyenf.com/dai-quan-gia-la-ma-hoang-c/chuong-{i}.html'
        title, text = download_text_from_url(url)
        
        if title and text:
            file.write(f"Chapter {i}: {title}\n\n{text}\n\n")
            print(f"Text for chuong-{i} downloaded and added to file.")
        else:
            print(f"Failed to download text for chuong-{i}.")
