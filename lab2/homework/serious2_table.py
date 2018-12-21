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



# import xlsxwriter
# workbook  = xlsxwriter.Workbook('doanhthu.xlsx')
# worksheet = workbook.add_worksheet()
doanh_thu_list=[]

# Title
head = soup.find("table", id="tblGridData")
trs = head.tr
# td_truoc_sau = trs.find("td", "b_r_c")
# div = td_truoc_sau.div
# a_list = div.find_all("a")

# for a in a_list:
#     img = a.img 
#     mui_ten = img["src"]
    # truoc_sau = a.string
    # chuyen_doi = mui_ten + truoc_sau
    # image_data = BytesIO(urlopen(mui_ten).read())
    # worksheet.insert_image('A1', mui_ten, {'image_data': image_data})

td_quy_list = trs.find_all("td", "h_t")
tieu_de_list = []

for td_quy in td_quy_list:
    quy = td_quy.string
    tieu_de_list.append(quy)

# Body
body = soup.find("table", id="tableContent")
tr_list = body.find_all("tr")
for tr in tr_list:
    td_list = tr.find_all("td", align = "right")
    for td in td_list:
        content = td.string
        for tieu_de in tieu_de_list:
            doanh_thu = OrderedDict({
                tieu_de: content
            })
            # print(tieu_de)
            # print(content)
            doanh_thu_list.append(doanh_thu)
            # print(doanh_thu_list)

# pyexcel.save_as(records=doanh_thu_list, dest_file_name="doanhthu.xlsx") 

