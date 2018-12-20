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

tieu_de_list = []

# import xlsxwriter
# workbook  = xlsxwriter.Workbook('doanhthu.xlsx')
# worksheet = workbook.add_worksheet()

# Title
head = soup.find("table", id="tblGridData")
tr = head.tr
td_truoc_sau = tr.find("td", "b_r_c")
div = td_truoc_sau.div
a_list = div.find_all("a")


for a in a_list:
    img = a.img 
    
    mui_ten = img["src"]
    truoc_sau = a.string
    print(mui_ten)

    # image_data = BytesIO(urlopen(mui_ten).read())
    # worksheet.insert_image('A1', mui_ten, {'image_data': image_data})

    tieu_de_list.append(truoc_sau)
    # tieu_de_list.append(mui_ten)

td_quy_list = tr.find_all("td", "h_t")
for td_quy in td_quy_list:
    quy = td_quy.string
    # tieu_de_list.append(quy)

td_tang_truong = tr.find("td", "h_t_tt")
tang_truong = td_tang_truong.string
# tieu_de_list.append(td_tang_truong)


# body = soup.find("table", id="tableContent")

pyexcel.save_as(records=tieu_de_list, dest_file_name="doanhthu.xlsx") 

