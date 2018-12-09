from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)

db = client.get_database()

post_collection = db["posts"]

new_document = {
    "title": "...",
    "author": "Harley",
    "content": "Tôi muốn kể sự thật cho mọi người, mặc dù sẽ chẳng ai tin tôi. Thế giới này thực ra chỉ là một cuốn sách, mỗi người chúng ta đóng một vai trong cuốn sách đó và chẳng ai có thể thay đổi được số phận của mình. Cuốn sách cứ âm thầm đi đến hồi kết đã được định đoạt sẵn, giống như thể mỗi chúng ta đều sẽ chết. Đó là sự thật không thể thay đổi!"
}

post_collection.insert_one(new_document)

client.close()