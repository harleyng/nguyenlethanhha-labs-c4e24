from urllib.request import urlopen 
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from io import BytesIO

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

conn = urlopen(url)
raw_data = conn.read()
page_content = raw_data.decode("utf8")
soup = BeautifulSoup(page_content, "html.parser")

doanh_thu = []
table = soup.find("table",id = "tableContent")
tr_list = table.find_all("tr")
for tr in tr_list:
    td_list = tr.find_all("td", "b_r_c")
    for td in td_list:
        td = td.string 
        content = {
            " ": td
        }
        doanh_thu.append(content)

pyexcel.save_as(records=doanh_thu, dest_file_name="doanhthu.xlsx") 

