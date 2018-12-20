from urllib.request import urlopen 
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

url = "https://www.apple.com/itunes/charts/songs/?fbclid=IwAR0ixsJ6cBlCupacTgTlLPlnnVPXa3qPx4myV3bx3JO4QRFJIVgaO4UCVBk"

conn = urlopen(url)
raw_data = conn.read()
page_content = raw_data.decode("utf8")
soup = BeautifulSoup(page_content, "html.parser")


section = soup.find("section", "section chart-grid")
div_list = section.find_all("div", "section-content")

song_list = []
for div in div_list:
    ul = div.ul
    li_list = ul.find_all("li")
    for li in li_list:
        a_name = li.h3.a
        a_artist = li.h4.a
        name = a_name.string 
        artist = a_artist.string
        song = OrderedDict({
            "Name": name,
            "Artist": artist
        })
        song_list.append(song)
   

pyexcel.save_as(records=song_list, dest_file_name="itunes.xlsx") 