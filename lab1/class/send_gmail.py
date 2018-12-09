from gmail import GMail, Message
from random import randint

sickness_list = ["ung thư", "kiết lị", "tiêu chảy"]

#1. Select a sickness randomly 
i = randint(0,len(sickness_list) - 1)
sickness = sickness_list[i]

html_template = '''
<p>Ch&agrave;o sếp,</p>
<p>H&ocirc;m nay thức dậy, em thấy m&igrave;nh mệt mỏi. B&aacute;c sĩ bảo em bị <em><strong>{{reason}}</strong></em> rồi&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /></p>
<p>Sếp cho em nghỉ ốm&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /></p>
<p>&nbsp;</p>
'''

#2. sickness + html_template ==> html_content
# Hint: goole: string replace
html_content = html_template.replace("{{reason}}", sickness)


gmail = GMail("secsosoo@gmail.com","Sectheug1ygir1^^")
msg = Message("hihihihihihihihihihihihihihihihihihihihihihihihi" ,to="c4e.techkidsvn@gmail.com",html=html_content)
gmail.send(msg)

