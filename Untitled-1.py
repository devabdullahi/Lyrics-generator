import requests
from bs4 import BeautifulSoup

AZLYRICS_URL = "https://www.azlyrics.com"
BIG_URL = f"{AZLYRICS_URL}/k/kevingates.html"

def scrape_songs(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    # Correctly find song links within the album list div
    song_divs = soup.find_all("div", class_=None)
    song_list = []
    for div in song_divs:
        links = div.find_all("a", href=True)
        for link in links:
            title = link.text.strip()
            song_url = link['href']
            full_link = f"{AZLYRICS_URL}{song_url}" if song_url.startswith("/") else song_url
            song_list.append({"title": title, "link": full_link})

    return song_list

def print_songs(songs):
    for song in songs:
        print(f"TITLE: {song['title']}")
        print(f"LINK: {song['link']}\n")

if __name__ == "__main__":
    songs = scrape_songs(BIG_URL)
    print_songs(songs)
